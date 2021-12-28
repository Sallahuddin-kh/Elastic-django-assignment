import ageofempires.ElasticClient.Client as Client
import ageofempires.ElasticClient.index_config as conf

class Unit():

    def __init__(self):
        """
        Constructor creates an instance with elasticsearch client
        """
        self.client = Client.Client()

    def bulk_index(self, data:list):
        """
        Inserts data into Unit index
        """
        self.client.index_data(data)

    def make_index(self):
        """
        Creates the Unit index
        """
        settings = conf.get_index_settings()
        mappings = conf.get_index_mappings('units')
        self.client.create_index('units', settings, mappings)

    def get_objects(self):
        """
        Retrieves the Unit objects from
        the index
        """
        return self.client.get_data('units')
