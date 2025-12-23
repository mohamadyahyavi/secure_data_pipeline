import pandas as pd
from pathlib import Path
from .storage_base import StorageBase

class ParquetStorage(StorageBase):
    """
    Store processed chunks as Parquet file.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def write_chunk(self, df: pd.DataFrame):
        """
        Append chunk to Parquet using append mode (PyArrow required).
        """
        # If file exists, append; else, create new
        if self.file_path.exists():
            df.to_parquet(self.file_path, engine="pyarrow", index=False, append=True)
        else:
            df.to_parquet(self.file_path, engine="pyarrow", index=False)
        print(f"✅ Chunk written to Parquet: {self.file_path}")
