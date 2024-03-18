import pandas as pd

def get_max_key_len(df: pd.DataFrame):
    max_length = max(len(key) for key in df.keys())
    return max_length
