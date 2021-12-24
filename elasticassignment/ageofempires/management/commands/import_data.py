from django.core.management.base import BaseCommand
import ageofempires.models.civilization as Civilization
import ageofempires.models.structure as Structure
import ageofempires.models.technology as Technology
import ageofempires.models.unit as Unit
from django.conf import settings
import ageofempires.HTTPClient.HTTPClient as HTTPClient

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-i', '--import_name', type=str, help='Define the index to insert data')

    def handle(self, *args, **kwargs):
        import_name = kwargs['import_name']
        if import_name:
            if import_name == 'civilizations':
                self.index_civilizations()
            elif import_name == 'structures':
                self.index_structures()
            elif import_name == 'technologies':
                self.index_technologies()
            elif import_name == 'units':
                self.index_units()
            else:
                self.stdout.write(import_name + ' index not recognized')
        else:
            self.index_civilizations()
            self.index_structures()
            self.index_technologies()
            self.index_units()

    def index_civilizations(self):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['CIVILIZATIONS']
        data_list = HTTPClient.HTTPClient.get(url)
        civ_instance = Civilization.Civilization()
        civilizations = data_list['civilizations']
        civilization_list = []
        for civlization in civilizations:
            civ = {
                "_index" : "civilizations",
                "_source" : civlization
            }
            civilization_list.append(civ)
        batch_size = 20
        for i in range(0, len(civilization_list), batch_size):
            civ_instance.bulk_index(civilization_list[i:i+batch_size])

    def index_structures(self):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['STRUCTURES']
        data_list = HTTPClient.HTTPClient.get(url)
        str_instance = Structure.Structure()
        structures = data_list['structures']
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
        batch_size = 20
        for i in range(0, len(structures_list), batch_size):
            str_instance.bulk_index(structures_list[i:i+batch_size])

    def index_technologies(self):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['TECHNOLOGIES']
        data_list = HTTPClient.HTTPClient.get(url)
        tech_instance = Technology.Technology()
        technologies = data_list['technologies']
        technologies_list = []
        for technology in technologies:
            tech = {
                "_index" : "technologies",
                "_source" : technology
            }
            technologies_list.append(tech)
        batch_size = 20
        for i in range(0, len(technologies_list), batch_size):
            tech_instance.bulk_index(technologies_list[i:i+batch_size])

    def index_units(self):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['UNITS']
        data_list = HTTPClient.HTTPClient.get(url) 
        unit_instance = Unit.Unit()
        units = data_list['units']
        units_list = []
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
            unit_instance.bulk_index(units_list[i:i+batch_size])
