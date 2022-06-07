from flask import Flask, request
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from twilio.twiml.messaging_response import MessagingResponse
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  'private_key.json'

DIALOGFLOW_PROJECT_ID = 'project_id'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def root():
    return "WhatsApp Chatbot"

@app.route('/api/getMessage', methods=['POST'])
def home():
    message=request.form.get('Body')
    mobnum=request.form.get('From')
    session_client = dialogflow.SessionsClient()
    session = session_client. session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types. TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow. types. QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result. intent_detection_confidence)
    print("Fulfillment text:", response.query_result. fulfillment_text)
    # sendMessage(mobnum, response.query_result. fulfillment_text)
    return response.query_result. fulfillment_text


def sendMessage(mobnum, message):
    print("Mobile number : ",mobnum)
    print("Message is : ",message)
    url = "https://api.twilio.com/2010-04-01/Accounts/AC3b4e9356a0acfb55cceeece7f5752f19/Messages.json"
    payload = {'From': 'whatsapp:+14123456789',
    'Body': message,
    'To': mobnum}
    headers = {
        'Authorization': 'Basic <token>'
    }
    response = requests.request('POST', url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
    return ""

if __name__ == '__main__':
    app.run()
