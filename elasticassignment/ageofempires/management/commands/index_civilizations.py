from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
import requests

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response_data = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations")
        return_list = response_data.json()
        civilizations = return_list['civilizations']
        civilization_list = []
        for civlization in civilizations:
            civ = {
                "_index": "civilization",
                "_source": civlization
            }
            civilization_list.append(civ)
        bulk(connections.get_connection(),civilization_list,20)
