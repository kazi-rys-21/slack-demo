import slack
import os
from pathlib import Path
from dotenv import load_dotenv
# Import Flask
from flask import Flask,request,Response
import requests

# Handles events from Slack
from slackeventsapi import SlackEventAdapter

# Load the Token from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Configure your flask application
app = Flask(__name__)
# Configure SlackEventAdapter to handle events
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

# Using WebClient in slack, there are other clients built-in as well !!
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# connect the bot to the channel in Slack Channel
#client.chat_postMessage(channel='#cps-847-course', text='Send Message Demo')

# Get Bot ID
BOT_ID = client.api_call("auth.test")['user_id']

message_counts = {}

@ app.route('/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)
    client.chat_postMessage(
        channel=channel_id, text=f"Message: {message_count}")
    print(message_counts)
    return Response(), 200

url='https://geek-jokes.sameerkumar.website/api'
@app.route('/joke', methods=['GET','POST'])
def joke():
    data = request.form
    channel_id = data.get('channel_id')
    response = requests.request("GET", url)
    print(response.text)
    client.chat_postMessage(channel=channel_id, text=response.text)
    return Response(), 200

# handling Message Events
@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event',{})
    user_id = event.get('user')

    if BOT_ID != user_id:
        if user_id in message_counts:
            message_counts[user_id] += 1
        else:
            message_counts[user_id] = 1



# Run the webserver micro-service
if __name__ == "__main__":
    app.run(debug=True)