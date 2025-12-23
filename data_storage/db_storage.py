import pandas as pd
from sqlalchemy import create_engine
from .storage_base import StorageBase

class DBStorage(StorageBase):
    """
    Store processed chunks into a SQL database.
    """

    def __init__(self, connection_string: str, table_name: str, if_exists="append"):
        """
        Args:
            connection_string (str): SQLAlchemy connection string, e.g.,
                'sqlite:///patients.db' or 'postgresql://user:pass@localhost/dbname'
            table_name (str): Name of the table to write into
            if_exists (str): Behavior if table exists ('append', 'replace', 'fail')
        """
        self.engine = create_engine(connection_string)
        self.table_name = table_name
        self.if_exists = if_exists

    def write_chunk(self, df: pd.DataFrame):
        """
        Write DataFrame chunk to database table.
        """
        df.to_sql(self.table_name, self.engine, if_exists=self.if_exists, index=False)
        # After first write, always append
        self.if_exists = "append"
        print(f"✅ Chunk written to DB table: {self.table_name}")
