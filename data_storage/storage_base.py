from abc import ABC, abstractmethod
import pandas as pd

class StorageBase(ABC):
    """
    Base class/interface for all storage classes.
    """

    @abstractmethod
    def write_chunk(self, df: pd.DataFrame):
        """
        Write a chunk of processed DataFrame to the storage.

        Args:
            df (pd.DataFrame): Chunk to store.
        """
        pass
