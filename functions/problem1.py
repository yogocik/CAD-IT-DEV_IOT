# Salary conversion apps

import pandas as pd
from flask import Flask
from utils.processing import load_json, join_data
from utils.api import fetch_data

def get_currency_rates(from_currency: str, to_currency: str) -> object:
    """Fetch currency data from remote endpoint.

    Parameters:
    from_currency (str)         : source currency
    to_currency  (str)          : target currency
    
    Returns:
    json data (object)
    """
    currency_key = '{}_{}'.format(from_currency.upper(), to_currency.upper())
    api_key = '652db892b2e8f4c9c8fc'
    url_req = 'https://free.currconv.com/api/v7/convert?q={}&compact=ultra&apiKey={}'.format(
        currency_key, api_key)
    data = fetch_data(url_req)
    return data

def get_endpoint_usage():
    """Fetch API request frequency."""
    api_key = '652db892b2e8f4c9c8fc'
    url_req = f'https://free.currconv.com/others/usage?apiKey={api_key}'
    data = fetch_data(url_req)
    return data

def input_converted_salary(data: pd.DataFrame, source_col: str,
                currency_data: dict) -> pd.DataFrame:
    """Fetch currency data from remote endpoint.

    Parameters:
    from_currency (str)         : source currency
    to_currency  (str)          : target currency
    
    Returns:
    json data (object)
    """
    rates = list(currency_data.values())[0]
    converted_col = list(currency_data.keys())[0].split('_')[0]
    data['salaryIn{}'.format(converted_col)] = data[source_col].map(lambda x: x / rates)
    return data

def fetch_and_convert_salary(url_endpoint: str,
                            convertion_currency : str,
                            col_selection: list = [],
                            is_json : bool = False) -> object:
    """Fetch and convert data from endpoint.

    Parameters:
    url_endpoint   (str)          : remote endpoint
    col_selection  (str)          : selected columns or information
    is_json        (boolean)      : json-type output option
    
    Returns:
    Data object (JSON or DataFrame)
    """
    data = fetch_data(url_endpoint, is_dataframe = True)
    salary_data = load_json('JSON/salary_data.json', 'array')
    joined_data = join_data(data, salary_data, how='inner', join_key='id')
    currency_rates = get_currency_rates(convertion_currency, 'IDR')
    converted_salary_data = input_converted_salary(joined_data, 'salaryInIDR',
                                                    currency_rates)
    if len(col_selection) > 0:
        converted_salary_data = converted_salary_data[col_selection]
    if is_json:
        converted_salary_data = converted_salary_data.to_json(orient='records')
    return converted_salary_data
