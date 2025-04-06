import pandas as pd

def load_data(csv_path):
    """
    Loads CSV event log data from a given path.
    Splits into features (X) and label (y).
    """
    df = pd.read_csv(csv_path)
    if "label" not in df.columns:
        raise ValueError("Expected a 'label' column in dataset.")
    
    X = df.drop(columns=["label"])
    y = df["label"]
    return X, y
