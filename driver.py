# Get current day

import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Let the script take commandline arguments about which string to use as the search query
import sys
import os

# Get the first argument passed to the script
# This is the search query

# import Scraper class
from scraperobj import Scraper

# create Scraper object
scraper = Scraper(datetime.datetime.today())

scraper.run(['MongaBay','InsideClimateNews', 'Grist','ENN'])
scraper.getArticles()
uri = "mongodb+srv://scraper:getNEWS@newscluster.kkx3kzx.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api= ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

scraper.upload(client,'flairai')

