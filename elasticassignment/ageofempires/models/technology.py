import ageofempires.ElasticClient.Client as Client
import ageofempires.ElasticClient.index_config as conf

class Technology():

    def __init__(self):
        self.client = Client.Client()

    def bulk_index(self, data:list):
        self.client.index_data(data)

    def make_index(self):
        settings = conf.get_index_settings()
        mappings = conf.get_index_mappings('technologies')
        self.client.create_index('technologies',settings,mappings)

    def get_objects(self):
        return self.client.get_data('technologies')