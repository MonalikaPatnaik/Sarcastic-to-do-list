# CBIGDTUW15 : Sarcastic-to-do-list
## A whatsapp bot that will keep track of our to-do list and if we slack in completing any of our tasks, it will send us sarcastic memes.
### Tech Stack
[**Twilio**](https://www.twilio.com/docs)
**What is Twilio and why do we use this?**
 Twilio is a cloud communication platform as a service (CPaaS). It helps software developers create customer experiences via building blocks—APIs. 
It lets you build cross-channel messaging across the likes of SMS, WhatsApp and Chat.

**How to use Twilio?**
1.  Get Twilio Credentials.
2.  Create an account. Since the cost of Twilio depends on your usage, charging is determined by use case. You can also get started with a free trial.
3.  Get the API. Go to “Account Details” to do so.
4.  Choose a Twilio phone number.
5.  Get a messaging SID.
6.  Find Twilio API at RapidAPI.com or go to the Twilio Package Page.
7.  Make connections by using your credentials.
8.  Access Code Snippets through logging in to RapidAPI.
9.  Customize Fields and Language and select the code you need.

[**Ngrok**](https://ngrok.com/docs) - Ngrok allows anyone to access a website hosted on our local server. A url is generated under the Ngrok domain that can then be shared with anyone. Using Ngrok only requires a basic installation and sign up followed by a one-line command ( ./ngrok <protocol> <port>),once the website on the local host is ready for deployment. The service is free and suits our requirement at least while we're still developing the product.

[**Flask**](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a Python web framework which we will be using to create a web application that responds to our incoming messages. We will be using flask and not Python scripts directly because Whatsapp is installed on the phone while our application will be on the laptop so we need a web server that can connect both, and flask provides that. Also we won’t be using Django here as it comes with a lot of prewritten code that we do not require.

 **Code for a basic whatsapp bot:** 

from flask import Flask, request <br/>
import requests <br/>
from twilio.twiml.messaging_response import MessagingResponse <br/>
app = Flask(_name_) <br/>
@app.route('/bot', methods=['POST']) <br/>
def bot():<br/>
    incoming_msg = request.values.get('Body', '').lower() <br/>
    resp = MessagingResponse()<br/>
    msg = resp.message()<br/>
    msg.body('Hi! How are you?')<br/>
    return str(resp) <br/>
if _name_ == '_main_': <br/>
    app.run(port=4000) <br/>
    
[**PROJECT OVERVIEW**](https://www.canva.com/design/DAFHWDW81lY/dLTNvzwSJbewl13yqHKhRg/edit?utm_content=DAFHWDW81lY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
