# Python, Dialogflow, Twilio, Whatsapp Chatbot

### Create Python Virtual Environment 
#### Install virtual environment

`pip install virtualenv`

#### Create a virtual environment

`virtualenv -p python3 chatbot_env`

###### you can give any name you want instead of **chatbot_env**

#### Activate virtual environment 
###### Linux Mac OS
`
cd ./chatbot_env
source bin/activate
`
###### Windows
`
cd ./chatbot_env
 Scripts/activate
`

#### Installing requirements from requirements.txt file
`
pip install -r requirements.txt
`
 
 To configure Dialogflow api with flask follow this [doc.](https://medium.com/zenofai/creating-chatbot-using-python-flask-d6947d8ef805)
 
 To configure Twilio api with Whatsapp follow this [doc.](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio)
