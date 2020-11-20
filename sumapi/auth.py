import requests
from .config import URL
from json import JSONDecodeError



def auth(username, password):
    login_data = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(URL["tokenURL"], data=login_data).json()
    except JSONDecodeError:
        response = requests.post(URL["tokenURL"], data=login_data).json()
    return response
