import elasticsearch
from django.conf import settings
from elasticsearch.helpers import bulk

class Client:
    """
    Client makes the connection with the elasticsearch
    and performs all the related tasks.
    """
    def __init__(self):
        self.__connection = self.__make_connection()
    
    def __make_connection(self):
        """
        Establishes connection with elasticsearch 
        according to the CONFIG settings provided in
        settings.py
        """
        return elasticsearch.Elasticsearch([settings.CONFIG])

    def get_data(self, index_name:str):
        """
        Gets data from the elastic index.
        index_name is the name of the index from
        which has to retrieved
        """
        res = self.__connection.search(index= index_name, query={"match_all": {}}, size = 1000)
        return res

    def create_index(self,index_name:str,settings:dict,mappings:dict):
        """
        Creates a new index in elasticsearch
        index_name is the name of new index
        settings are the settings for the index
        and mappings are the mappings for the index.
        """
        request_body = {
            "settings" : settings,
            'mappings' : mappings
        }
        print("creating index "+ index_name)
        self.__connection.indices.create(index = index_name, body = request_body)

    def index_data(self,data:list):
        """
        Puts the data recieved in elasticsearch
        Index information has to be included in 
        data list.
        """
        print("Indexing data into " + str(data[1]["_index"]))
        bulk(self.__connection, data)
