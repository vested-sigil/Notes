# Flask setup
from flask import Flask, jsonify
import os
from notion_client import Client

app = Flask(__name__)

# Notion client setup
TOKEN = os.getenv('TOKEN')
ROOT_UUID = os.getenv('ROOT_UUID')
client = Client(auth=TOKEN)

def get_notion_page() -> dict:
    """
    Retrieve a specific Notion page using the ROOT_UUID.
    """
    try:
        page = client.pages.retrieve(page_id=ROOT_UUID)
        return page
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    # Use the Notion API to fetch a page's content
    page_content = get_notion_page()
    # You could further process page_content here to extract and format the information you need
    # For simplicity, returning the raw response or error message
    return jsonify(page_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
