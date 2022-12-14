from flask import Flask,render_template,url_for,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from ChatBot import chatbot

# Creating flask app object
app = Flask(__name__)


# define predict function here only 
@app.route('/')
def home():
	return render_template('index.html')

@app.route("/get")
def get_bot_response():
    new_query= request.args.get('msg')
    return str(chatbot.get_response(new_query))

  
 
if __name__ == '__main__':
	app.run(debug=True) 



    