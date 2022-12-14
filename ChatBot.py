from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# create chatbot
chatbot= ChatBot('chatbot')        # will name by bot as norman

# We will give our chtabot to the trainer to train the bot with our dataset
trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train("C:\\Users\\Manjula\\Desktop\\pychatenv\\pyct38venv\\BankFAQs.yml")  


print("< Training Completed >")

# lets see how our chatbt replies to our questions 
# reply= chatbt.get_response("hello")
# print(reply) 
# print("Hello! How may I help you today?")

# while True:
#     bot_input= chatbot.get_response(input("Enter your query >> "))
#     print('Bot: ', bot_input) 


# we will go for a flask app to chat on the web page(refer app.py)


