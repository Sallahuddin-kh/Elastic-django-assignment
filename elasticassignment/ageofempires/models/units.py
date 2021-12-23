from elasticsearch.helpers import bulk
from django.conf import settings
from ageofempires.Elastic_search.elastic_client import elastic_client

class Units():

    elastic_client = elastic_client()

    def __get_settings():
        return {
            "index":{
                    "number_of_shards": settings.NUMBER_OF_SHARDS,
                    "number_of_replicas": settings.NUMBER_OF_REPLICAS
            }
        }

    def __get_mappings():
        return {
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

    def make_index():
        request_body = {
            "settings" : Units.__get_settings(),
            'mappings': Units.__get_mappings()
        }
        print("creating 'units' index...")
        es  = elastic_client.make_connection()
        es.indices.create(index = 'units', body = request_body)

    def populate_index(url:str):
        return_list = elastic_client.get_data(url)
        units = return_list['units']
        units_list = []
        es  = elastic_client.make_connection()
        for unit in units:
            if 'range' in unit:
                unit['structure_range'] = unit['range']
                del unit['range']
            uni = {
                "_index" : "units",
                "_source" : unit
            }
            units_list.append(uni)
        batch_size = 20
        for i in range(0, len(units_list), batch_size):
            bulk(es, units_list[i:i+batch_size])
