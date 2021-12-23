from django.core.management.base import BaseCommand
import ageofempires.models.structures as Structures
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['STRUCTURES']
        Structures.Structures.make_index()
        Structures.Structures.populate_index(url)
