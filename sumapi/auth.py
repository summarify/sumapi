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
            access_token: str
                Your API Access Token
            token_type: str
                Your Token Type

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
        response = requests.post(URL["tokenURL"], data=login_data)
        response_json = response.json()
    except JSONDecodeError:
        return response
    except (ConnectionError) as e:
        raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

    if "detail" in response_json.keys():
        if response_json['detail'] == 'Incorrect username or password':
            raise ValueError("There is an error in the login information. Try again by checking your username and password.")

    return response_json
