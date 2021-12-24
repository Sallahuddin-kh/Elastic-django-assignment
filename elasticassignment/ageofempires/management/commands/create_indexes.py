import ageofempires.models.civilization as Civilization
import ageofempires.models.structure as Structure
import ageofempires.models.technology as Technology
import ageofempires.models.unit as Unit
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        civ_intance = Civilization.Civilization()
        struc_instance = Structure.Structure()
        tech_instance = Technology.Technology()
        uni_instance = Unit.Unit()
        civ_intance.make_index()
        struc_instance.make_index()
        tech_instance.make_index()
        uni_instance.make_index()
