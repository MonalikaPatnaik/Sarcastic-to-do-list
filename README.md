# CBIGDTUW15 : Sarcastic-to-do-list
## A whatsapp bot that will keep track of our to-do list and if we slack in completing any of our tasks, it will send us sarcastic memes.
Code for a basic whatsapp bot: 

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(_name_)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hi! How are you?')
    return str(resp)


if _name_ == '_main_':
    app.run(port=4000)
    
[PROJECT OVERVIEW](https://www.canva.com/design/DAFHWDW81lY/dLTNvzwSJbewl13yqHKhRg/edit?utm_content=DAFHWDW81lY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
