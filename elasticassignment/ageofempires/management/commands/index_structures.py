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
                    "armor" : {"type" : "text"},
                    "attack" : {"type" : "integer"},
                    "build_time" : {"type" : "integer"},
                    "description" : {"type" : "text"},
                    "expansion" : {"type" : "text"},
                    "hit_points" : {"type" : "integer"},
                    "id" : {"type" : "integer"},
                    "line_of_sight" : {"type" : "integer"},
                    "name" : {"type" : "text"},
                    "reload_time" : {"type" : "double"},
                    "special" : {"type" : "text"},
                    "structure_range" : {"type" : "text"}
                }    
            }
        }
        print("creating 'structures' index...")
        es.indices.create(index = 'structures', body = request_body)
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
