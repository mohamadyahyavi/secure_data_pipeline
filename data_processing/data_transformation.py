# data_processing/data_transformation.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform data transformations on the dataframe.

    Steps:
    - Scale numerical columns using StandardScaler
    - Optional: Add more transformations
    """
    if df.empty:
        print("❌ Warning: DataFrame is empty in transform_data")
        return df

    # Select numeric columns safely and convert to list
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_cols:
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    else:
        print("⚠️ No numeric columns to scale")

    return df
