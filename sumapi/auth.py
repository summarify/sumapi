import requests
from .config import URL
from json import JSONDecodeError
from requests.exceptions import ConnectionError

def auth(username, password):
    """
        With this function, you will receive the token you need to define while using the API.

        Parameters
        ----------
        username : str
            Your API Username
        password : str
            Your API Password

        Returns
        -------
        dict:
            access_token: Your API Access Token
            token_type: Your Token Type

        Examples
        --------
        from sumapi.auth import auth

        token = auth(username='<your_username>', password='<your_password')
    """
    login_data = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(URL["tokenURL"], data=login_data).json()
    except JSONDecodeError:
        response = requests.post(URL["tokenURL"], data=login_data).json()
    except (ConnectionError) as e:
        raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


    return response
