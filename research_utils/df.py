import pandas as pd


def get_max_key_len(df: pd.DataFrame):
    max_length = max(len(key) for key in df.keys())
    return max_length

def proportional_sample(df: pd.DataFrame, label_name: str, frac: float, min_samples_per_class: int = 0):
    sampled_dfs = []

    for label, value in sorted(df[label_name].value_counts().to_dict().items(), key=lambda item: item[1]):
        tmp_df = df[df[label_name] == label]

        if len(tmp_df) > min_samples_per_class:
            n_samples = max(min_samples_per_class, int(frac * len(tmp_df)))
        else:
            n_samples = len(tmp_df)

        tmp_df = tmp_df.sample(n=n_samples, random_state=42)
        sampled_dfs.append(tmp_df)

    sample_df = pd.concat(sampled_dfs, ignore_index=True)
    return sample_df

def sample_with_labels(df: pd.DataFrame, label_name: str, labels: dict, random_state: int=42, shuffle: bool=True) -> pd.DataFrame:
    """
    Get the sampled DataFrame using each number of Label classes. 

    Parameters: 
    - df (pandas.DataFrame): Input DataFrame.
    - label_name (str): The name of label column.
    - labels (dict): Dictionary using the input DataFrame's keys as keys and the number of each sample as values for output.
    - random_state (int): Random state value for pandas.DataFrame.sample function. 
    - shuffle (bool): Flag for shuffling of output DataFrame. 

    Returns: 
    pd.DataFrame: DataFrame sampled with a given number of data for each class. 

    Raise: 
    - no raises here. 

    Example: 
    >>> sampled_df = sample_with_labels(df, 'Label', labels={
            'label1': 10, 
            'label2': 20, 
        })

    You can also use a 'ratio' to get the partially sampled DataFrame.  
    >>> frac = 0.5
        sampled_df = sample_with_labels(df, 'Label', labels={
            key: int(value * frac) for key, value in dict(df['Label'].value_counts()).items()
        })
    """
    
    tmp_df_list = []
    for key in labels:
        tmp_df = df[df[label_name] == key]
        tmp_df_list.append(tmp_df.sample(n=labels[key], random_state=random_state))
        print(f"Sampled {key}: {labels[key]}")
    
    result_df = pd.concat(tmp_df_list, ignore_index=True)

    if shuffle:
        result_df = result_df.sample(frac=1).reset_index(drop=True)

    print(f"Finally sampled DataFrame: {result_df.shape}")
    return result_df