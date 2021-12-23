from django.core.management.base import BaseCommand
import ageofempires.models.civilizations as Civilizations
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = settings.AOE_BASE_URL + settings.DATA_URLS['CIVILIZATIONS']
        Civilizations.Civilizations.make_index()
        Civilizations.Civilizations.populate_index(url)
