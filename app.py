import os
import subprocess
import importlib
from flask import Flask, jsonify
from notion_client import Client  # Added for clearer import

app = Flask(__name__)

# Globally initialize the client variable. It will be set in the connect() function.
client = None

def check():
    try:
        importlib.import_module('notion_client')
        return "notion_client package is already installed."
    except ImportError:
        return "notion_client package is not installed. Please install it using the appropriate method."

def install():
    try:
        subprocess.run(['./Installer.sh'], check=True)
        return "Installer script executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def connect():
    try:
        global client  # Use the global client variable
        token = os.getenv('TOKEN')  # Corrected method to get environment variable
        client = Client(auth=token)
        subprocess.run(['b4a', 'configure', 'accountkey'])

        key = os.getenv('ACCOUNTKEY')  # Corrected method to get environment variable
        subprocess.run([key])
        return os.getenv('APP_ID')  # Corrected method to get environment variable
    except Exception as e:
        return f"Error: {e}"

def get_notion_page() -> dict:
    """
    Retrieve a specific Notion page using the ROOT_UUID.
    """
    try:
        root = os.getenv('ROOT_UUID')  # Corrected method to get environment variable
        # Ensure that the client variable is correctly used here
        page = client.pages.retrieve(page_id=root)
        return page
    except Exception as e:
        return {"error": str(e)}

@app.route('/check')
def check_route():
    return check()

@app.route('/install')
def install_route():
    return install()

@app.route('/connect')
def connect_route():
    return connect()

@app.route('/')
def home():
    # Use the Notion API to fetch a page's content
    page_content = get_notion_page()
    # You could further process page_content here to extract and format the information you need
    # For simplicity, returning the raw response or error message
    return jsonify(page_content)

@app.route('/b4a/<command>')
def parsecli(command):
    try:
        subprocess.run(['b4a', command], check=True)
        return f"Command '{command}' executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{command}': {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
