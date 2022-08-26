import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bot", methods=['POST'])
def bot_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    incoming_msg = request.values.get('Body','').lower()

    # Create reply
    resp = MessagingResponse()
    msg=resp.message()
    
           
    if incoming_msg=='y':
        text="Great,let's do this!\nBefore we begin, let me introduce you to our creators:)\nIntro of creators\nLet's get started now\nPlease enter your to do list for today along with the deadlines for your task(in the form MM DD YEAR)."
        msg.body(text)
              
        
    elif incoming_msg=='n':
        msg.body("Okay then, I'll go and sit in the corner now waiting for you to change your mind!\nTill then, goodbye! ")  
    else:
        for words in incoming_msg.split():
         if words.isalnum()==True and words.isalpha()==False:
        
           text1="Congratulations Bestie, you have successfully made your todo-list for today!\nNow all you gotta do is complete the tasks. That must be easy, right?\nand if you fail to do so..\n*I'll be there for youuu*:))"
        
           msg.body(text1) 
           break
        else:
         msg.body("Hey there\nGood to see thay you've come to cure your procrastination.\nMy name is bot and I'm your robo-bestie.\nLet me tell you a little about myself before we dive deep into the real bussiness!\nI am built to help you out with completing your tasks for the day.\nBut that does not sound fun,right?\nThat is why I will be sending you regular memes as a reminder to complete your tasks or I might even start to roast you a bit along the way;)\nEnter y if you want to say 'let's do this'\nEnter n if you are out.")      
    
    

    return str(resp)
    

if __name__ == "__main__":
    app.run(debug=True)
    