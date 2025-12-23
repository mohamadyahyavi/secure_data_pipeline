print(">>> TEST FILE EXECUTED <<<")
from ingestion import CSVReader

CSV_PATH = r"C:\Users\Mohammad\Downloads\patients.csv"

def main():
    reader = CSVReader(
        file_path=CSV_PATH,
        chunk_size=100_000  # process 100k rows at a time
    )

    total_rows = 0

    for i, chunk in enumerate(reader.read_chunks()):
        print(f"Chunk {i + 1}")
        print(f"Rows in chunk: {len(chunk)}")
        print(f"Columns: {list(chunk.columns)}")
        print("-" * 40)

        total_rows += len(chunk)

        # Stop early (sanity test)
        if i == 1:
            break

    print(f"Processed rows so far: {total_rows}")


if __name__ == "__main__":
    main()
