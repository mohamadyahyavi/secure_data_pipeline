import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform data cleaning on the dataframe.

    Steps:
    - Drop rows with any NaN values
    - Remove duplicate rows
    - Optional: Add more cleaning rules if needed
    """
    if df.empty:
        print("❌ Warning: DataFrame is empty in clean_data")
        return df

    # Drop rows with any NaN values
    df_cleaned = df.dropna()

    # Remove duplicate rows
    df_cleaned = df_cleaned.drop_duplicates()

    # Example: Ensure numeric columns are actually numeric
    numeric_cols = df_cleaned.select_dtypes(include=['object']).columns
    for col in numeric_cols:
        try:
            df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='ignore')
        except Exception as e:
            print(f"⚠️ Could not convert column {col} to numeric: {e}")

    return df_cleaned
