# Function for process data further
import pandas as pd
import json


def load_json(json_url: str, attribute_target: str) -> object:
    """Load data from local json file.

    Parameters:
    json_url (str)         : local directory (relative or absolute path)
    attribute_target (str) : interested attribute in json
    
    Returns:
    Dataframe (object)
    """
    with open(json_url) as f:
        data = json.load(f)
        final_data = pd.DataFrame.from_dict(data[attribute_target])
        return final_data


def join_data(left_data: pd.DataFrame, right_data: pd.DataFrame, join_key: str = None,
            left_key: str = None, right_key: str = None, how: str = 'inner'):
    """Data join and clean duplicate columns.
    
    Parameters:
    left_data (object)         : Dataframe
    right_data (object)        : Dataframe
    join_key (str)             : Join key for merging
    left_key (str)             : Join key from left_data
    right_key (str)            : Join key from right_data
    how (str)                  : Type of merging
    
    Returns:
    Dataframe (object)
    """
    result = left_data.merge(
        right_data,
        how=how,
        on=join_key,
        left_on=left_key,
        right_on=right_key
    )
    result.columns = \
        result.columns.str.replace('_x', '')
    result = \
        result.loc[:, ~result.columns.str.endswith('_y')]
    return result