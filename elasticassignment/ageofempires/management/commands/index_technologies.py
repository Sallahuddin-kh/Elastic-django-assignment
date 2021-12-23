from django.core.management.base import BaseCommand
import ageofempires.models.technologies as Technologies
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = settings.AOE_BASE_URL + settings.AOE_ENDPOINTS['TECHNOLOGIES']    
        Technologies.Technologies.make_index()
        Technologies.Technologies.populate_index(url)
