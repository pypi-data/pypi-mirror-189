# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Collection Reader Node

This is a SQL Query Execution Plan Node.

This Node primarily is used for reading NoSQL sources like MongoDB and Firestore.
"""
import time

from typing import Iterable

import pyarrow

from opteryx.connectors.capabilities import PredicatePushable
from opteryx.models import QueryProperties
from opteryx.operators import BasePlanNode
from opteryx.models.columns import Columns


class CollectionReaderNode(BasePlanNode):
    def __init__(self, properties: QueryProperties, **config):
        """
        The Collection Reader Node is responsible for reading the relevant documents
        from a NoSQL document store and returning a Table/Relation.
        """
        super().__init__(properties=properties)

        self._alias = config.get("alias")

        dataset = config["dataset"]
        self._dataset = ".".join(dataset.split(".")[:-1])
        self._collection = dataset.split(".")[0]

        if self._dataset == "":
            self._dataset = self._collection

        self._reader = config.get("reader")()

        # pushed down selection/filter
        self._selection = config.get("selection")

        self._disable_selections = "NO_PUSH_SELECTION" in config.get("hints", [])

    @property
    def config(self):  # pragma: no cover
        if self._alias:
            return f"{self._dataset} => {self._alias}"
        return f"{self._dataset}"

    @property
    def name(self):  # pragma: no cover
        return "Collection Reader"

    @property
    def can_push_selection(self):
        return (
            isinstance(self._reader, PredicatePushable) and not self._disable_selections
        )

    def push_predicate(self, predicate):
        if self.can_push_selection:
            return self._reader.push_predicate(predicate)
        return False

    def execute(self) -> Iterable:
        metadata = None

        row_count = self._reader.get_document_count(self._collection)

        for pyarrow_page in self._reader.read_documents(self._collection):
            start_read = time.time_ns()
            if not isinstance(pyarrow_page, pyarrow.Table):
                pyarrow_page = pyarrow.Table.from_pylist(pyarrow_page)

            self.statistics.time_data_read += time.time_ns() - start_read
            self.statistics.rows_read += pyarrow_page.num_rows
            self.statistics.bytes_processed_data += pyarrow_page.nbytes
            self.statistics.document_pages += 1

            if metadata is None:
                pyarrow_page = Columns.create_table_metadata(
                    table=pyarrow_page,
                    expected_rows=row_count,
                    name=self._dataset,
                    table_aliases=[self._alias],
                    disposition="collection",
                    path=self._dataset,
                )
                metadata = Columns(pyarrow_page)
                self.statistics.collections_read += 1
            else:
                pyarrow_page = metadata.apply(pyarrow_page)

            yield pyarrow_page
