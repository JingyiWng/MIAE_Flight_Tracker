import requests
from api.config import settings
ROOT_URL = settings.ROOT_URL

def states_accessor():

    # Go thru the doc api examples
    url = f"{ROOT_URL}/api/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())

## The API function below is deprecated
# def tracks_accessor():
#     url = f"https://opensky-network.org/api/tracks/all?icao24=3c4b26&time=0"
#     r = requests.get(url)
#     if not r.ok:
#         raise RuntimeError(r.json())
#     print(r.json())


def flight_accessor():
    url = f"{ROOT_URL}/api/flights/all?begin=164114"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())