import pandas as pd
from pathlib import Path
from .storage_base import StorageBase

class CSVStorage(StorageBase):
    """
    Store processed chunks as a CSV file.
    """

    def __init__(self, file_path: str, mode: str = "a", header: bool = True):
        self.file_path = Path(file_path)
        self.mode = mode
        self.header = header

    def write_chunk(self, df: pd.DataFrame):
        """
        Append chunk to CSV.
        """
        df.to_csv(self.file_path, mode=self.mode, index=False, header=self.header)
        # After first write, header should not repeat
        self.header = False
        print(f"✅ Chunk written to CSV: {self.file_path}")
