import ageofempires.ElasticClient.Client as Client
import ageofempires.ElasticClient.index_config as conf
from abc import abstractmethod

class BaseModel():

    @abstractmethod
    def set_index_name(self):
        """
        Abstract method must be implemented in child classes
        """
        pass

    def __init__(self):
        """
        Constructor creates an instance with elasticsearch client
        """
        self.client = Client.Client()

    def bulk_index(self, data:list):
        """
        Inserts data into index
        """
        self.client.index_data(data)

    def make_index(self):
        """
        Creates the index
        """
        settings = conf.get_index_settings()
        mappings = conf.get_index_mappings(self.index_name)
        self.client.create_index(self.index_name, settings, mappings)

    def get_objects(self):
        """
        Retrieves the objects from the index
        """
        return self.client.get_data(self.index_name)
