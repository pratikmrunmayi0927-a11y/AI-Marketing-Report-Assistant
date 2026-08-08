import pandas as pd

def clean_data(df):

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Remove extra spaces from text values
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert numeric columns
    numeric_cols = [
        "Impressions",
        "Clicks",
        "Spend",
        "Conversions",
        "Revenue"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df