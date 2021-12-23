from elasticsearch.helpers import bulk
from django.conf import settings
from ageofempires.Elastic_search.elastic_client import elastic_client

class Civilizations():

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
                    "army" : {"type" : "text"},
                    "civilization_bonus" : {"type" : "text"},
                    "id" : {"type" : "integer"},
                    "name" : {"type" : "text"},
                    "team_bonus" : {"type" : "text"},
                    "unique_tech" : {"type" : "text"},
                    "unique_unit" : {"type" : "text"}
            }
        }

    def make_index():
        request_body = {
            "settings" : Civilizations.__get_settings(),
            'mappings' : Civilizations.__get_mappings()
        }
        print("creating 'civilization' index...")
        es  = elastic_client.make_connection()
        es.indices.create(index = 'civilization', body = request_body)

    def populate_index(url:str):
        return_list = elastic_client.get_data(url)
        civilizations = return_list['civilizations']
        civilization_list = []
        es  = elastic_client.make_connection()
        for civlization in civilizations:
            civ = {
                "_index" : "civilization",
                "_source" : civlization
            }
            civilization_list.append(civ)
        batch_size = 20
        for i in range(0, len(civilization_list), batch_size):
            bulk(es, civilization_list[i:i+batch_size])
