from django.conf import settings

def get_index_settings():
    """
    Creates the settings of index as a dictionary
    """
    return {
        "index":{
            "number_of_shards" : settings.NUMBER_OF_SHARDS,
            "number_of_replicas" : settings.NUMBER_OF_REPLICAS
        }
    }

def get_index_mappings(index_name:str):
    """
    Creates the mappings as a dictionary
    receives the name of the index and returns
    the mappings accordingly from helping methods.
    """
    if index_name == 'civilizations':
        return get_civilization_mappings()
    elif index_name == 'structures':
        return get_structure_mappings()
    elif index_name == 'technologies':
        return get_technology_mappings()
    elif index_name == 'units':
        return get_unit_mappings()
    else:
        return None

def get_civilization_mappings():
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

def get_structure_mappings():
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

def get_technology_mappings():
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

def get_unit_mappings():
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
