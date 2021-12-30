from ageofempires.models.civilization import Civilization
from ageofempires.models.structure import Structure
from ageofempires.models.technology import Technology
from ageofempires.models.unit import Unit
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Command creates all the indexes at once.
    No parameter required.
    >> python manage.py create_indexes
    """
    def handle(self, *args, **kwargs):
        try:
            civilization_instance = Civilization()
            structure_instance = Structure()
            technology_instance = Technology()
            unit_instance = Unit()
            civilization_instance.make_index()
            structure_instance.make_index()
            technology_instance.make_index()
            unit_instance.make_index()
        except Exception as e:
            print(f"INDEX CREATION FAILED. {e}")
