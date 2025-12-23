# config/settings.py
"""
Configuration settings for the secure_data_pipeline project.
"""

import os

# Base output directory
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# Paths
CSV_PATH = r"C:\Users\Mohammad\Downloads\patients.csv"

# Chunk size for reading large files
CHUNK_SIZE = 100_000

# Output file paths
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "patients.csv")
OUTPUT_PARQUET = os.path.join(OUTPUT_DIR, "patients.parquet")

# Database settings
DB_URI = f"sqlite:///{os.path.join(OUTPUT_DIR, 'patients.db')}"
DB_TABLE = "patients"

# Optional: Add more configs like logging level, parallelism, etc.
