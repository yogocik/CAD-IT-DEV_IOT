# Function for data request or connection
import requests
from functools import lru_cache, wraps
from datetime import datetime, timedelta
import pandas as pd

def timed_lru_cache(seconds: int, maxsize: int = 1000):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache

@timed_lru_cache(300)
def fetch_data(url_link: str, is_dataframe: bool = False) -> object:
    """Fetch data from remote server via endpoint.

    Parameters:
    url_link (str)         : endpoint url
    is_dataframe (boolean) : result data type
    
    Returns:
    Data object (JSON or DataFrame)
    """
    data = requests.get(url_link)
    if data.status_code != 200:
        print(f'Error retrieving data ({data.status_code})')
        result = None
    else:
        print(f'Successful data retrival')
        result = data.json()
    if is_dataframe:
        result = pd.DataFrame.from_dict(result)
    return result