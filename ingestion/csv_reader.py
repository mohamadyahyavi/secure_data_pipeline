import pandas as pd
from typing import Iterator
from .base_reader import BaseReader


class CSVReader(BaseReader):
    """
    Reader for large CSV files using chunk-based reading.
    """

    def read_chunks(self) -> Iterator[pd.DataFrame]:
        try:
            for chunk in pd.read_csv(
                self.file_path,
                chunksize=self.chunk_size,
                low_memory=False
            ):
                yield chunk

        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {self.file_path}")

        except pd.errors.ParserError as e:
            raise ValueError(f"CSV parsing error: {e}")

        except Exception as e:
            raise RuntimeError(f"Unexpected error while reading CSV: {e}")
