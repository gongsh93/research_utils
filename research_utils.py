import pandas as pd

def get_max_key_len(df: pd.DataFrame):
    max_length = max(len(key) for key in df.keys())
    return max_length


def check_invalid_values(df: pd.DataFrame, label_name: str):
    f_string_space = 16

    # Input dataset shape overview
    print(f"Original dataset shape: {df.shape}")

    # Generate masks
    # Mask for NaN value
    mask_nan_none  = df.isnull()
    # Mask for Infinity value
    mask_inf       = df.replace([np.inf, -np.inf], np.nan).isnull()
    # Mask for Null String
    mask_empty_str = (df == "")

    # Merge mask
    mask_invalid   = mask_nan_none | mask_inf | mask_empty_str

    # Get row indexes including any of invalid values
    invalid_rows = df[mask_invalid.any(axis=1)]

    # Count invalid values per column
    invalid_values_per_column = mask_invalid.sum()

    print(f"Number of rows including invalid value for each columns:")
    total_invalid_values = 0
    for column in df.keys():
        if invalid_values_per_column[column] != 0:
            print(f"{column:{f_string_space}}: {invalid_values_per_column[column]} ({invalid_values_per_column[column]/len(df)*100:.4}%)")
            total_invalid_values += invalid_values_per_column[column]
    
    # Early return for clean dataset
    if total_invalid_values == 0:
        print("This dataset includes no invalid values.")
        return None
    else:
        print("") # Just for space 

    # Count invalid values per Label's classes
    invalid_rows[label_name].value_counts()
    invalid_rows_per_class = invalid_rows[label_name].value_counts()
    # Prepare total number of each Label classes for ratio comparison
    total_num_per_class = df[label_name].value_counts()


    print(f"Number of rows including invalid value for each label class:")
    for key in invalid_rows_per_class.keys():
        print(f"{key:{f_string_space}}: {invalid_rows_per_class[key]} ({invalid_rows_per_class[key]/total_num_per_class[key]*100:.4}% of {total_num_per_class[key]})")
    print("") # Just for space 

    # Count total number of invalid rows 
    total_invlid_rows = 0
    for key in invalid_rows_per_class.keys():
        total_invlid_rows += invalid_rows_per_class[key]

    print(f"Input dataset has {total_invlid_rows} invalid rows.")

    return invalid_rows


def original_dataset_check(df: pd.DataFrame, label: str = None):
    report = {
        "all_columns": df.columns,
        "columns": [col for col in df.columns if col != label], 
        "label": label, 
    }

    max_col_len = 0
    if column in df.columns:
        if len(column) > max_col_len:
            max_len = len(column)
    
    for column in df.columns:
        print(f"{column:<{max_len}} has {df[column].isna().sum()} invalid values.")