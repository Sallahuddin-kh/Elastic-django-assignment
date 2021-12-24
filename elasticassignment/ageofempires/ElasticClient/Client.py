import elasticsearch
from django.conf import settings
from elasticsearch.helpers import bulk

class Client:

    def __init__(self):
        self.__connection = self.__make_connection()
    
    def __make_connection(self):
        return elasticsearch.Elasticsearch([settings.CONFIG])

    def get_data(self, index_name):
        res = self.__connection.search(index= index_name, query={"match_all": {}},size = 1000)
        return res

    def create_index(self,index_name,settings,mappings):
        request_body = {
            "settings" : settings,
            'mappings' : mappings
        }
        print("creating index...")
        self.__connection.indices.create(index = index_name, body = request_body)

    def index_data(self,data):
        print("Indexing data...")
        bulk(self.__connection, data)
