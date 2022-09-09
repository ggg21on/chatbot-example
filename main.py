from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim gosto, eu programo em Python',
           'Qual o seu nome?','TW bot :)', 'Qual o melhor time do mundo?', 'Corinthians.', 'Quantos mundiais o Palmeiras possui?', 'Nenhum.',]

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Sinto muito, ainda não sei responder esta pergunta :(')
