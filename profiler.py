import pandas as pd

def profile_dataframe(df):
    profile = {}

    for col in df.columns:
        col_data = df[col]
        profile[col] = {
            "Data Type": str(col_data.dtype),
            "Nulls": col_data.isnull().sum(),
            "Unique Values": col_data.nunique(),
            "Sample Values": col_data.dropna().unique()[:5].tolist()
        }

        if pd.api.types.is_numeric_dtype(col_data):
            profile[col].update({
                "Min": col_data.min(),
                "Max": col_data.max(),
                "Mean": col_data.mean(),
                "Std": col_data.std()
            })

    return profile
