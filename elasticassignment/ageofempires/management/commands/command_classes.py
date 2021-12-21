from abc import abstractmethod
from elasticsearch.helpers import bulk
import requests
import elasticsearch
from django.conf import settings

class AOElasticsearch:

    def make_connection():
        return elasticsearch.Elasticsearch([settings.CONFIG])

    def getAPIdata(url:str):
        response_data = requests.get(url)
        return response_data.json()

    @abstractmethod
    def make_index():
        pass

    @abstractmethod
    def populate_index(url:str):
        pass


class Civilizations(AOElasticsearch):

    es = AOElasticsearch.make_connection()

    def make_index():
        request_body = {
            "settings" : {
                "index":{
                    "number_of_shards": settings.NUMBER_OF_SHARDS,
                    "number_of_replicas": settings.NUMBER_OF_REPLICAS
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
        Civilizations.es.indices.create(index = 'civilization', body = request_body)

    def populate_index(url:str):
        return_list = AOElasticsearch.getAPIdata(url)
        civilizations = return_list['civilizations']
        civilization_list = []
        for civlization in civilizations:
            civ = {
                "_index": "civilization",
                "_source": civlization
            }
            civilization_list.append(civ)
        bulk(Civilizations.es, civilization_list, 20)


class Structures(AOElasticsearch):
    es = AOElasticsearch.make_connection()
    def make_index():
        request_body = {
            "settings" : {
                "index":{
                    "number_of_shards": settings.NUMBER_OF_SHARDS,
                    "number_of_replicas": settings.NUMBER_OF_REPLICAS
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
        Structures.es.indices.create(index = 'structures', body = request_body)

    def populate_index(url:str):
        return_list = AOElasticsearch.getAPIdata(url)
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
        bulk(Structures.es, structures_list, 20)


class Technologies(AOElasticsearch):

    es = AOElasticsearch.make_connection()

    def make_index():
        request_body = {
            "settings" : {
                "index":{
                    "number_of_shards": settings.NUMBER_OF_SHARDS,
                    "number_of_replicas": settings.NUMBER_OF_REPLICAS
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
        Technologies.es.indices.create(index = 'technologies', body = request_body)

    def populate_index(url:str):
        return_list = AOElasticsearch.getAPIdata(url)
        technologies = return_list['technologies']
        technologies_list = []
        for technology in technologies:
            tech = {
                "_index": "technologies",
                "_source": technology
            }
            technologies_list.append(tech)
        bulk(Technologies.es,technologies_list,20)


class Units(AOElasticsearch):

    es = AOElasticsearch.make_connection()

    def make_index():
        request_body = {
            "settings" : {
                "index":{
                    "number_of_shards": settings.NUMBER_OF_SHARDS,
                    "number_of_replicas": settings.NUMBER_OF_REPLICAS
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
        Units.es.indices.create(index = 'units', body = request_body)

    def populate_index(url:str):
        return_list = AOElasticsearch.getAPIdata(url)
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
        bulk(Units.es,units_list,20)
