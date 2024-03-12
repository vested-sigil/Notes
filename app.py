from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from notion_client import Client
import os
import subprocess

# Use the Environs module for better environment variable management
from environs import Env
env = Env()
env.read_env()

# Flask app initialization
app = Flask(__name__)
CORS(app)
api = Api(app)

# Notion client initialization using environment variables
NOTION_KEY = env.str("NOTION_KEY")
NOTION_PAGE_ID = env.str("NOTION_PAGE_ID")
client = Client(auth=NOTION_KEY)

# Login route
@app.route('/login', methods=['POST'])
def login():
    subprocess.run("./installer.sh")
    account_key = os.getenv('ACCOUNT_KEY')
    result = subprocess.run(["b4a", "configure", "accountkey", account_key], capture_output=True, text=True)
    if result.returncode == 0:
        return jsonify({"status": "success", "message": "Command executed successfully."}), 200
    else:
        return jsonify({"status": "error", "message": "Command failed with exit code", "error": result.stderr}), 500

# Define your API resources here
class RetrieveBlock(Resource):
    def get(self, block_id):
        return client.blocks.retrieve(block_id=block_id)

# Add other resources similarly

# Add resources to the API
api.add_resource(RetrieveBlock, '/retrieve_block/<block_id>')
# Add other resources similarly

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)

