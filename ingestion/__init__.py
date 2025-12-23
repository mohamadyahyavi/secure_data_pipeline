"""
Ingestion module for reading large structured data files
(CSV, JSON Lines, Parquet in future).
This __init__.py allows importing readers directly from ingestion:
    from ingestion import CSVReader, JSONReader, BaseReader
"""

# Explicit relative imports
from .base_reader import BaseReader
from .csv_reader import CSVReader
from .json_reader import JSONReader

# Make them available when importing * from ingestion
__all__ = [
    "BaseReader",
    "CSVReader",
    "JSONReader",
]

# Optional: simple sanity check to verify package loads
if __name__ == "__main__":
    print("Ingestion package loaded successfully")
    print(f"Available readers: {__all__}")
