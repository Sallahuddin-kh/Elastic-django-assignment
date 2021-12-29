from ageofempires.ElasticClient.Client import Client
import ageofempires.ElasticClient.index_config as conf
from abc import ABC, abstractmethod

class BaseModel(ABC):

    def __init__(self):
        """
        Constructor creates an instance with elasticsearch client
        Sets up the index_name variable accordingly.
        """
        self.client = Client()
        self.index_name = self.get_index_name()

    @abstractmethod
    def get_index_name(self):
        """
        Abstract method must be implemented in child classes
        """
        raise NotImplementedError("Subclasses should Implement set_index_name")

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
