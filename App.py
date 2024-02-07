from flask import Flask, request
from flask_restful import Resource, Api
from notion_client import Client
import os
from flask_cors import CORS

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

# Initialize Notion client
token = os.getenv('TOKEN')
root_uuid = os.getenv('ROOT_UUID')

if not token:
    token = input("Enter Notion integration token: ")
if not root_uuid:
    root_uuid = input("Enter root UUID: ")

client = Client(auth=token)

class RetrieveBlock(Resource):
    def get(self, block_id):
        return client.blocks.retrieve(block_id=block_id)

class UpdateBlock(Resource):
    def post(self, block_id):
        block_data = request.get_json()
        return client.blocks.update(block_id=block_id, **block_data)

class AppendChildBlocks(Resource):
    def post(self, block_id):
        children = request.get_json()
        return client.blocks.children.append(block_id=block_id, children=children)

class QueryDatabase(Resource):
    def get(self, database_id):
        filter = request.args.get('filter')
        sorts = request.args.get('sorts')
        payload = {"database_id": database_id}
        if filter is not None:
            payload["filter"] = filter
        if sorts is not None:
            payload["sorts"] = sorts
        return client.databases.query(**payload)

class RetrievePage(Resource):
    def get(self, page_id):
        return client.pages.retrieve(page_id=page_id)

class UpdatePageProperties(Resource):
    def post(self, page_id):
        properties = request.get_json()
        return client.pages.update(page_id=page_id, properties=properties)

class HomePage(Resource):
    def get(self):
        return client.pages.retrieve(root_uuid)

class Help(Resource):
    def get(self):
        help_text = (
            "Available methods in the Notes class:\n"
            "- retrieve_block(block_id): Retrieve a block using its ID.\n"
            "- update_block(block_id, block_data): Update a block with new data.\n"
            "- append_child_blocks(block_id, children): Append child blocks to a parent block.\n"
            "- query_database(database_id, filter=None, sorts=None): Query a database.\n"
            "- retrieve_page(page_id): Retrieve a page using its ID.\n"
            "- update_page_properties(page_id, properties): Update page properties.\n"
            "For more detailed information on each method, please refer to the Notion API documentation."
        )
        return help_text

# Add resources to the API
api.add_resource(RetrieveBlock, '/retrieve_block/<block_id>')
api.add_resource(UpdateBlock, '/update_block/<block_id>')
api.add_resource(AppendChildBlocks, '/append_child_blocks/<block_id>')
api.add_resource(QueryDatabase, '/query_database/<database_id>')
api.add_resource(RetrievePage, '/retrieve_page/<page_id>')
api.add_resource(UpdatePageProperties, '/update_page_properties/<page_id>')
api.add_resource(HomePage, '/homepage')
api.add_resource(Help, '/help')

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
