# Python, Dialogflow, Twilio, Whatsapp Chatbot

### Create Python Virtual Environment 
#### Install virtual environment
```console
pip install virtualenv
```

#### Create a virtual environment
```console
virtualenv -p python3 chatbot_env
```
###### You can give any name you want instead of **`chatbot_env`**

#### Activate virtual environment 
###### Linux, Mac OS
```console
cd ./chatbot_env
```

```console
source bin/activate
```
###### Windows
```console
cd chatbot_env\
```
```console
 Scripts\activate
```

#### Installing requirements from **requirements.txt** file
```console
pip install -r requirements.txt
```
 
 To configure Dialogflow api with flask follow this [doc.](https://medium.com/zenofai/creating-chatbot-using-python-flask-d6947d8ef805)
 
 To configure Twilio api with Whatsapp follow this [doc.](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio)
