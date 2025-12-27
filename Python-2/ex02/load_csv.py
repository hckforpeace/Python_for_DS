import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", data.shape)
        return data
    except (FileNotFoundError, PermissionError, Exception) as error:
        print(error)
        return None
