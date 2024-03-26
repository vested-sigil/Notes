import configparser
import os
import subprocess
import importlib
from flask import Flask, jsonify

app = Flask(__name__)

def check():
    try:
        importlib.import_module('notion_client')
        return "notion_client package is already installed."
    except ImportError:
        return "notion_client package is not installed. Please install it using the appropriate method."

def install():
    try:
        subprocess.run(['./installer.sh'], check=True)
        return "Installer script executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

class CfgMgr:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def initcon(self, TOKEN, ROOT_UUID, ACCOUNTKEY, APP_ID):
        """
        Initialize the configuration file with default values.
        """
        if os.path.exists(self.config_file):
            return "Error: Config already initiated. Try keycon."
        else:
            self.config['DEFAULT'] = {'TOKEN': TOKEN,
                                      'ROOT_UUID': ROOT_UUID,
                                      'ACCOUNTKEY': ACCOUNTKEY,
                                      'APP_ID': APP_ID}
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
            return "Config file initiated successfully."

def actkey():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'KEYS' in config and 'ACCOUNTKEY' in config['KEYS']:
        return config['KEYS']['ACCOUNTKEY']
    else:
        return "Error: ACCOUNTKEY not found in config.ini file or config.ini file doesn't exist."

def get_root():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'KEYS' in config and 'ROOT_UUID' in config['KEYS']:
        return config['KEYS']['ROOT_UUID']
    else:
        return "Error: ROOT_UUID not found in config.ini file or config.ini file doesn't exist"

def get_app():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'KEYS' in config and 'APP_ID' in config['KEYS']:
        return config['KEYS']['APP_ID']
    else:
        return "Error: APP_ID not found in config.ini file or config.ini file doesn't exist"

def get_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'KEYS' in config and 'TOKEN' in config['KEYS']:
        return config['KEYS']['TOKEN']
    else:
        return "Error: TOKEN not found in config.ini file or config.ini file doesn't exist."

def connect():
    try:
        from notion_client import Client
        token = get_token()
        client = Client(auth=token)
        subprocess.run(['b4a', 'configure', 'accountkey'])

        key = actkey()
        subprocess.run([key])
        return get_app()
    except Exception as e:
        return f"Error: {e}"

def get_notion_page() -> dict:
    """
    Retrieve a specific Notion page using the ROOT_UUID.
    """
    try:
        root = get_root()
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

@app.route('/setup/<TOKEN>/<ROOT_UUID>/<ACCOUNTKEY>/<APP_ID>')
def setup(TOKEN, ROOT_UUID, ACCOUNTKEY, APP_ID):
    return CfgMgr().initcon(TOKEN, ROOT_UUID, ACCOUNTKEY, APP_ID)

@app.route('/')
def home():
    # Use the Notion API to fetch a page's content
    page_content = get_notion_page()
    # You could further process page_content here to extract and format the information you need
    # For simplicity, returning the raw response or error message
    return jsonify(page_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
