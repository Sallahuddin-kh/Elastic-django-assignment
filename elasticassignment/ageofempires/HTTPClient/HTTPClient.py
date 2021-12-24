import requests

class HTTPClient():

    def get(url:str):
        response_data = requests.get(url)
        return response_data.json()
