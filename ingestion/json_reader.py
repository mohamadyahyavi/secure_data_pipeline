import pandas as pd
from typing import Iterator
from .base_reader import BaseReader


class JSONReader(BaseReader):
    """
    Reader for large JSON Lines (.jsonl) files.

    Each line must contain a valid JSON object.
    """

    def read_chunks(self) -> Iterator[pd.DataFrame]:
        try:
            for chunk in pd.read_json(
                self.file_path,
                lines=True,
                chunksize=self.chunk_size
            ):
                yield chunk

        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {self.file_path}")

        except ValueError:
            raise ValueError(
                "Invalid JSON format. "
                "Ensure the file is in JSON Lines format."
            )

        except Exception as e:
            raise RuntimeError(f"Unexpected error while reading JSON: {e}")
