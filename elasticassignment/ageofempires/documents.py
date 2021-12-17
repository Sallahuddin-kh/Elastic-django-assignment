# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Civilization, Unit, Structure, Technology

@registry.register_document
class CivilizationDocument(Document):
    class Index:
        name = 'civilization'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
         model = Civilization
         fields = [
            'id',
            'name',
            'army',
            'unique_unit',
            'unique_tech',
            'team_bonus',
            'civilization_bonus',
         ]

@registry.register_document
class UnitDocument(Document):
    class Index:
        name = 'units'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
         model = Unit
         fields = [
                'id',
                'name',
                'description', 
                'expansion',
                'age',
                'created_in',
                'build_time',
                'reload_time',
                'attack_delay',
                'movement_rate',
                'line_of_sight',
                'hit_points',
                'attack',
                'armor',
                'attack_bonus',
                'armor_bonus',
                'search_radius',
                'accuracy',
                'blast_radius',
                'structure_range',
         ]

@registry.register_document
class StructureDocument(Document):
    class Index:
        name = 'structures'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
         model = Structure
         fields = [
            'id',
            'name',
            'description',
            'expansion',
            'age',
            'build_time',
            'hit_points',
            'line_of_sight',
            'armor',
            'reload_time',
            'attack',
            'special',
            'structure_range',
         ]

@registry.register_document
class TechnologyDocument(Document):
    class Index:
        name = 'technologies'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
         model = Technology
         fields = [
            'id',
            'name',
            'description',
            'expansion',
            'age',
            'develops_in',
            'build_time',
            'applies_to',
         ]