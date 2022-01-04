import requests

class HTTPClient():
    """
    Client to perform all HTTP and requests related
    tasks.
    """
    def get(url:str):
        """
        Gets the data from the remote API
        return the data in json format.
        """
        response_data = requests.get(url)
        return response_data.json()
