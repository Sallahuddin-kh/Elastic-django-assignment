import requests
import elasticsearch
from django.conf import settings

class elastic_client:

    def make_connection():
        return elasticsearch.Elasticsearch([settings.CONFIG])

    def get_data(url:str):
        response_data = requests.get(url)
        return response_data.json()
