import json
import os
import glob

# Connect Python file to MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sylviajacoby:Ellaella$2@cluster0.3cfxdom.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Connect Python to a specific database
from pymongo.database import Database
db = client["HackDuke"]

# Define the directory containing your text files
text_files_directory = '/users/sylviajacoby/Documents/fortheprogram/textfiles'
print(text_files_directory)

# Delete all existing documents in the collection
db["documents"].delete_many({})

# Iterate over the files in the directory
for filename in glob.glob(f"{text_files_directory}/*.txt"):
    print(filename)
    with open(filename, "r") as file:
        content = file.read()
        # Insert content into MongoDB collection
        db["documents"].insert_one({"filename": filename, "content": content})


