from django.shortcuts import render
import requests
from requests.exceptions import ConnectionError,HTTPError,Timeout,TooManyRedirects
import json
from elasticsearch import Elasticsearch
from .models import Civilization
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk



def civilizations(request):
    return render(request, 'ageofempires/civilizations.html' )