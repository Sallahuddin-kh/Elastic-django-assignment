from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
import requests

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response_data = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/structures")
        return_list = response_data.json()
        structures = return_list['structures']
        structures_list = []
        for structure in structures:
            if 'range' in structure:
                structure['structure_range'] = structure['range']
                del structure['range']
            struc = {
                "_index": "structures",
                "_source": structure
            }
            structures_list.append(struc)
        bulk(connections.get_connection(),structures_list)
