import slack
import os
from pathlib import Path
from dotenv import load_dotenv

# Load the Token from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
# Using WebClient in slack, there are other clients built-in as well !!
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# connect the bot to the channel in Slack Channel
client.chat_postMessage(channel='#cps-847-course', text='Send Message Demo2321')

#change
