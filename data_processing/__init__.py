"""
Data processing module for transforming and cleaning the ingested data.
This module includes functions for:
    - Data cleaning
    - Data transformation
    - Feature engineering
"""

# Import specific functions from processing modules
from .data_cleaning import clean_data
from .data_transformation import transform_data
from .feature_engineering import engineer_features

__all__ = [
    "clean_data",
    "transform_data",
    "engineer_features",
]
if __name__ == "__main__":
    print("✅ data_processing package loaded successfully")
    print(f"Available functions: {__all__}")