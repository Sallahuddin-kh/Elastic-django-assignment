import ageofempires.ElasticClient.Client as Client
import ageofempires.ElasticClient.index_config as conf

class Civilization():
    """
    Model class to manage the civilization data.
    """
    def __init__(self):
        """
        Constructor creates an instance with elasticsearch client
        """
        self.client = Client.Client()

    def bulk_index(self, data:list):
        """
        Inserts data into civilization index
        """
        self.client.index_data(data)

    def make_index(self):
        """
        Creates the civilization index
        """
        settings = conf.get_index_settings()
        mappings = conf.get_index_mappings('civilizations')
        self.client.create_index('civilizations' , settings , mappings)

    def get_objects(self):
        """
        Retrieves the civilization objects from
        the index
        """
        return self.client.get_data('civilizations')
