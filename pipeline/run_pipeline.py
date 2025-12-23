# pipeline/run_pipeline.py
from ingestion.csv_reader import CSVReader
from data_processing.data_cleaning import clean_data
from data_processing.data_transformation import transform_data
from data_processing.feature_engineering import engineer_features
from data_storage.csv_storage import CSVStorage
from data_storage.parquet_storage import ParquetStorage
from data_storage.db_storage import DBStorage
from config import settings
from utils.helpers import log
import os

def run_pipeline():
    log("Pipeline started")

    # Prepare storage
    os.makedirs("output", exist_ok=True)
    csv_storage = CSVStorage(settings.OUTPUT_CSV)
    parquet_storage = ParquetStorage(settings.OUTPUT_PARQUET)
    db_storage = DBStorage(settings.DB_URI, settings.DB_TABLE)

    # Initialize ingestion
    reader = CSVReader(file_path=settings.CSV_PATH, chunk_size=settings.CHUNK_SIZE)
    total_rows = 0

    for i, chunk in enumerate(reader.read_chunks()):
        log(f"Processing chunk {i+1} with {len(chunk)} rows")

        # Data processing
        chunk_clean = clean_data(chunk)
        chunk_trans = transform_data(chunk_clean)
        chunk_feat = engineer_features(chunk_trans)

        # Storage
        csv_storage.write_chunk(chunk_feat)
        parquet_storage.write_chunk(chunk_feat)
        db_storage.write_chunk(chunk_feat)

        total_rows += len(chunk_feat)

        # Stop early for sanity test (remove for full run)
        if i == 1:
            break

    log(f"Pipeline completed. Total rows processed: {total_rows}")

if __name__ == "__main__":
    run_pipeline()
