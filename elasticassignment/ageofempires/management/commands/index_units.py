from django.core.management.base import BaseCommand
from django.conf import settings
import ageofempires.models.units as Units

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['UNITS']
        Units.Units.make_index()
        Units.Units.populate_index(url)
