from abc import ABC, abstractmethod
from typing import Iterator
import pandas as pd


class BaseReader(ABC):
    """
    Abstract base class for all data readers.

    Reads large files in chunks to avoid memory overload.
    """

    def __init__(self, file_path: str, chunk_size: int = 100_000):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be a positive integer")

        self.file_path = file_path
        self.chunk_size = chunk_size

    @abstractmethod
    def read_chunks(self) -> Iterator[pd.DataFrame]:
        """
        Yield pandas DataFrames chunk by chunk.
        """
        raise NotImplementedError
