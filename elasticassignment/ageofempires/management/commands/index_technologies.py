from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
import requests

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response_data = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/technologies")
        return_list = response_data.json()
        technologies = return_list['technologies']
        technologies_list = []
        for technology in technologies:
            tech = {
                "_index": "technologies",
                "_source": technology
            }
            technologies_list.append(tech)
        bulk(connections.get_connection(),technologies_list,20)
