import json
import os

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


# Define the directory containing your text files
text_files_directory = "/path/to/your/text/files"

# Iterate over the files in the directory
for filename in os.listdir(text_files_directory):
    if filename.endswith(".txt"):  # Assuming the files have a .txt extension
        with open(os.path.join(text_files_directory, filename), "r") as file:
            content = file.read()

            # Insert content into MongoDB collection
            db["your-collection-name"].insert_one({"filename": filename, "content": content})

