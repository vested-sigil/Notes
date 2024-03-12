from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from notion_client import Client
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve environment variables
TOKEN = os.getenv('TOKEN')
ROOT_UUID = os.getenv('ROOT_UUID')
ACCOUNT_KEY = os.getenv('ACCOUNT_KEY')
APPID = os.getenv('APPID')

# Flask app initialization
app = Flask(__name__)
CORS(app)
api = Api(app)

# Notion client initialization using environment variables
client = Client(auth=TOKEN)

# Login route
@app.route('/login', methods=['POST'])
def login():
    subprocess.run("./installer.sh", check=True)
    result = subprocess.run(["b4a", "configure", "accountkey", ACCOUNT_KEY], capture_output=True, text=True, check=True)
    return jsonify({"status": "success", "message": "Command executed successfully."}), 200

# Define your API resources here
class RetrieveBlock(Resource):
    def get(self, block_id):
        return client.blocks.retrieve(block_id=block_id)

# Add resources to the API
api.add_resource(RetrieveBlock, '/retrieve_block/<block_id>')

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
