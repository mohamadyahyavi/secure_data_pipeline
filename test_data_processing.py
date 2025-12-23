print(">>> test_data_processing.py STARTED <<<")

import os
import pandas as pd
from ingestion.csv_reader import CSVReader
from data_processing.data_cleaning import clean_data
from data_processing.data_transformation import transform_data
from data_processing.feature_engineering import engineer_features

# Path to your test CSV file
CSV_PATH = r"C:\Users\Mohammad\Downloads\patients.csv"

def test_data_processing():
    # Step 1: Check if the file exists
    print("Checking if CSV file exists...")
    if not os.path.exists(CSV_PATH):
        print(f"❌ CSV file not found at: {CSV_PATH}")
        return
    else:
        print(f"✅ CSV file exists: {CSV_PATH}")

    # Step 2: Try reading the first 5 rows with pandas (sanity check for CSV format)
    try:
        print("\nAttempting to read the first 5 rows with pandas...")
        df_preview = pd.read_csv(CSV_PATH, nrows=5)
        print("✅ Pandas preview (first 5 rows):")
        print(df_preview)
    except Exception as e:
        print(f"❌ Pandas failed to read CSV: {e}")
        return

    # Step 3: Initialize CSVReader with the test file
    try:
        print("\nInitializing CSVReader...")
        reader = CSVReader(file_path=CSV_PATH, chunk_size=100_000)

        found_chunk = False
        total_rows = 0

        # Step 4: Process data in chunks
        for i, chunk in enumerate(reader.read_chunks()):
            found_chunk = True
            print(f"\n✅ Processing Chunk {i + 1}...")
            print(f"Rows in chunk: {len(chunk)}")
            print(f"Columns: {list(chunk.columns)}")

            # Step 5: Data cleaning
            chunk_cleaned = clean_data(chunk)
            print(f"Cleaned rows: {len(chunk_cleaned)}")

            # Step 6: Data transformation
            chunk_transformed = transform_data(chunk_cleaned)
            print(f"Transformed rows: {len(chunk_transformed)}")

            # Step 7: Feature engineering
            chunk_final = engineer_features(chunk_transformed)
            print(f"Final rows (with new features): {len(chunk_final)}")

            total_rows += len(chunk_final)

            # Optional: Check specific processing outcomes
            if 'age_group' in chunk_final.columns:
                print("✅ 'age_group' feature successfully added.")

            # Stop early (after first chunk) for sanity test
            break

        if not found_chunk:
            print("❌ No chunks were read from the CSV file.")
        else:
            print(f"\n✅ Total rows processed: {total_rows}")

    except Exception as e:
        print(f"❌ Error during CSVReader or data processing: {e}")

if __name__ == "__main__":
    test_data_processing()
