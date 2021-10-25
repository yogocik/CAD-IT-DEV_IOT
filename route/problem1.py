from flask import Blueprint
from functions.problem1 import fetch_and_convert_salary, get_endpoint_usage


problem1 = Blueprint('problem1', __name__)

@problem1.route("/")
def Welcome():
    return "This is initial page of salary converter endpoint"

@problem1.route('/convert_salary')
@problem1.route('/convert_salary/<string:convert_to>')
def get_converted_salary(convert_to: str = 'USD'):
    """Get request endpoint for salary conversion."""
    data = fetch_and_convert_salary('http://jsonplaceholder.typicode.com/users',
        col_selection=['id', 'name', 'username', 'email', 'address',
        'phone', 'salaryInIDR', 'salaryIn{}'.format(convert_to)], is_json=True,
        convertion_currency=convert_to)
    return data

@problem1.route('/api_calls')
def get_api_request_freq():
    """Get request endpoint for api request number."""
    info_api = get_endpoint_usage()
    return info_api