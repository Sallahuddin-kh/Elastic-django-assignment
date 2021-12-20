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
                    "age" : {"type" : "text"},
                    "applies_to" : {"type" : "text"},
                    "build_time" : {"type" : "integer"},
                    "description" : {"type" : "text"},
                    "develops_in" : {"type" : "text"},
                    "expansion" : {"type" : "text"},
                    "id" : {"type" : "integer"},
                    "name" : {"type" : "text"}
                }    
            }
        }
        print("creating 'technologies' index...")
        es.indices.create(index = 'technologies', body = request_body)
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
