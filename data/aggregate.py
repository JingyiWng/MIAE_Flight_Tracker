import pandas as pd
from pathlib import Path

def forming_dataset() -> pd.DataFrame:
    pass

def fixed_data_set() -> pd.DataFrame:
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path("/Users/jingyi/Desktop/MIAE_Python/MIAE_Flight_Tracker/data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list
