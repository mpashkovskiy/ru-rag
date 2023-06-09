import csv
from typing import Dict, List, Optional

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class CustomCSVLoader(BaseLoader):
    def __init__(
        self,
        file_path: str,
        source_column: str,
        csv_args: Optional[Dict] = None,
        encoding: Optional[str] = None,
    ):
        self.file_path = file_path
        self.source_column = source_column
        self.encoding = encoding
        self.csv_args = csv_args or {}

    def load(self) -> List[Document]:
        docs = []
        with open(self.file_path, newline="", encoding=self.encoding) as csvfile:
            csv_reader = csv.DictReader(csvfile, **self.csv_args)  # type: ignore
            for i, row in enumerate(csv_reader):
                metadata = {
                    k.strip(): v.strip()
                    for k, v in row.items()
                    if k != self.source_column
                }
                metadata["row"] = i
                metadata["file_path"] = self.file_path
                try:
                    docs.append(
                        Document(
                            page_content=row[self.source_column], metadata=metadata
                        )
                    )
                except KeyError:
                    raise ValueError(
                        f"Source column '{self.source_column}' not found in CSV file."
                    )
        return docs
