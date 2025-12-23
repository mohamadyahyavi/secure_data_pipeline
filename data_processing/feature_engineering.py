import pandas as pd
from datetime import datetime

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering for the patient dataset.

    Adds:
    - 'age' calculated from 'date_of_birth'
    - 'age_group' categorical feature
    """
    if df.empty:
        print("❌ Warning: DataFrame is empty in engineer_features")
        return df

    if 'date_of_birth' in df.columns:
        # Ensure 'date_of_birth' is datetime
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

        # Compute 'age'
        today = pd.Timestamp.today()
        df['age'] = today.year - df['date_of_birth'].dt.year - (
            (today.month, today.day) < (df['date_of_birth'].dt.month, df['date_of_birth'].dt.day)
        )

        # Create 'age_group' feature
        df['age_group'] = pd.cut(
            df['age'],
            bins=[0, 18, 30, 40, 50, 60, 100],
            labels=['<18', '18-30', '30-40', '40-50', '50-60', '60+']
        )
    else:
        print("❌ 'date_of_birth' column missing, cannot compute age or age_group")

    return df
