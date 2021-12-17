from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
import requests

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response_data = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/units")
        return_list = response_data.json()
        units = return_list['units']
        units_list = []
        for unit in units:
            if 'range' in unit:
                unit['structure_range'] = unit['range']
                del unit['range']
            uni = {
                "_index": "units",
                "_source": unit
            }
            units_list.append(uni)
        bulk(connections.get_connection(),units_list)
