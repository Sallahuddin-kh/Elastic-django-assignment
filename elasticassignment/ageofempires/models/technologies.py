from elasticsearch.helpers import bulk
from django.conf import settings
from ageofempires.Elastic_search.elastic_client import elastic_client

class Technologies():

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
                    "applies_to" : {"type" : "text"},
                    "build_time" : {"type" : "integer"},
                    "description" : {"type" : "text"},
                    "develops_in" : {"type" : "text"},
                    "expansion" : {"type" : "text"},
                    "id" : {"type" : "integer"},
                    "name" : {"type" : "text"}
            }    
        }


    def make_index():
        request_body = {
            "settings" : Technologies.__get_settings(),
            'mappings': Technologies.__get_mappings()
        }
        print("creating 'technologies' index...")
        es  = elastic_client.make_connection()
        es.indices.create(index = 'technologies', body = request_body)

    def populate_index(url:str):
        return_list = elastic_client.get_data(url)
        technologies = return_list['technologies']
        technologies_list = []
        es  = elastic_client.make_connection()
        for technology in technologies:
            tech = {
                "_index" : "technologies",
                "_source" : technology
            }
            technologies_list.append(tech)
        batch_size = 20
        for i in range(0, len(technologies_list), batch_size):
            bulk(es, technologies_list[i:i+batch_size])
