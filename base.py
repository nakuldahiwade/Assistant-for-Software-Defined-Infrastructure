from chatterbot.adapters.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot import ChatBot
from flask import Flask

app = Flask(__name__)

class CustomLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(CustomLogicAdapter, self).__init__(kwargs)

    def can_process(self, statement):
        # Return true if the statement contains the search text
        return 'Search for' in statement.text

    def process(self, statement, search_text):
        text =  search_text # ... something you return based on your search
        response = Statement(text)
        confidence = 0.5
        return confidence, response

class Session(object):
    def __init__(self, **kwargs):
        self.falvor = kwargs.get('flavor')
        self.image = kwargs.get('image')
        self.name = kwargs.get('name')


class OpenStackBot(ChatBot):
    def __init__(self, corpus):
        trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
        chatbot = super(OpenStackBot, self).__init__(self, trainer)
        chatbot.train(corpus)