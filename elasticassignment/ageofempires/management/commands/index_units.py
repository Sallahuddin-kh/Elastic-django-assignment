from django.core.management.base import BaseCommand
import ageofempires.management.commands.command_classes as command_classes

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        command_classes.Units.make_index()
        command_classes.Units.populate_index("https://age-of-empires-2-api.herokuapp.com/api/v1/units")
