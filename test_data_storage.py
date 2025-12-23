import pandas as pd
from data_storage.csv_storage import CSVStorage
from data_storage.parquet_storage import ParquetStorage
from data_storage.db_storage import DBStorage

# Sample DataFrame
df = pd.DataFrame({
    "patient_id": [1, 2, 3],
    "age": [34, 56, 28],
    "gender": ["M", "F", "M"]
})

print(">>> test_data_storage.py STARTED <<<")

# ---------- Test CSV Storage ----------
csv_storage = CSVStorage("test_output.csv")
csv_storage.write_chunk(df)

# ---------- Test Parquet Storage ----------
parquet_storage = ParquetStorage("test_output.parquet")
parquet_storage.write_chunk(df)

# ---------- Test DB Storage (SQLite example) ----------
db_storage = DBStorage("sqlite:///test_patients.db", "patients")
db_storage.write_chunk(df)

print("✅ All storage tests completed")
