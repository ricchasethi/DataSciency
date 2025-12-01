import pandas as pd
from zipfile import ZipFile

def read_data(filepath)->pd.DataFrame:
    dfs = []
    with ZipFile(filepath, 'r') as zip_ref:
        for f in zip_ref.namelist():
            print(f"Reading {f}...")
            with zip_ref.open(f) as file:
                df = pd.read_csv(file, parse_dates=['event_time'])
                dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df