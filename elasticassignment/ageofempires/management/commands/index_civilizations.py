from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
import requests
import elasticsearch

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        config = {
            'host': '127.0.0.1'
        }
        es = elasticsearch.Elasticsearch([config])
        request_body = {
            "settings" : {
                "index":{
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                }
            },
            'mappings': {
                'properties': {
                    "army" : {"type" : "text"},
                    "civilization_bonus" : {"type" : "text"},
                    "id" : {"type" : "integer"},
                    "name" : {"type" : "text"},
                    "team_bonus" : {"type" : "text"},
                    "unique_tech" : {"type" : "text"},
                    "unique_unit" : {"type" : "text"}
                }
            }
        }
        print("creating 'civilization' index...")
        es.indices.create(index = 'civilization', body = request_body)
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
