from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request, jsonify

app = Flask(__name__)

english_bot = ChatBot("SimpleBot")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = english_bot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run()