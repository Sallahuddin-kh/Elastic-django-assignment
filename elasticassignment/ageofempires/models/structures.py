from elasticsearch.helpers import bulk
from django.conf import settings
from ageofempires.Elastic_search.elastic_client import elastic_client

class Structures():

    elastic_client = elastic_client()

    def __get_settings():
        return {
            "index":{
                    "number_of_shards" : settings.NUMBER_OF_SHARDS,
                    "number_of_replicas" : settings.NUMBER_OF_REPLICAS
            }
        }

    def __get_mappings():
        return {
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

    def make_index():
        request_body = {
            "settings" : Structures.__get_settings(),
            'mappings' : Structures.__get_mappings()
        }
        print("creating 'structures' index...")
        es  = elastic_client.make_connection()
        es.indices.create(index = 'structures', body = request_body)

    def populate_index(url:str):
        return_list = elastic_client.get_data(url)
        structures = return_list['structures']
        structures_list = []
        es  = elastic_client.make_connection()
        for structure in structures:
            if 'range' in structure:
                structure['structure_range'] = structure['range']
                del structure['range']
            struc = {
                "_index": "structures",
                "_source": structure
            }
            structures_list.append(struc)
        batch_size = 20
        for i in range(0, len(structures_list), batch_size):
            bulk(es, structures_list[i:i+batch_size])
