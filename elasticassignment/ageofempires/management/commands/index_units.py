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
                    "accuracy" : {"type" : "text"},
                    "age" : {"type" : "text"},
                    "armor" : {"type" : "text"},
                    "armor_bonus" : {"type" : "text"},
                    "attack" : {"type" : "integer"},
                    "attack_bonus" : {"type" : "text"},
                    "attack_delay" : {"type" : "double"},
                    "blast_radius" : {"type" : "double"},
                    "build_time" : {"type" : "integer"},
                    "created_in" : {"type" : "text"},
                    "description" : {"type" : "text"},
                    "expansion" : {"type" : "text"},
                    "hit_points" : {"type" : "integer"},
                    "id" : {"type" : "integer"},
                    "line_of_sight" : {"type" : "integer"},
                    "movement_rate" : {"type" : "double"},
                    "name" : {"type" : "text"},
                    "reload_time" : {"type" : "double"},
                    "search_radius" : {"type" : "integer"},
                    "structure_range" : {"type" : "text"}
                } 
            }
        }
        print("creating 'units' index...")
        es.indices.create(index = 'units', body = request_body)
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
