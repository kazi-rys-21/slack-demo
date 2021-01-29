import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

data = {'text':'Test Webhooks'}

# Load the Webhook from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

webhook = os.environ['WEB_HOOK']
requests.post(webhook,json.dumps(data))


