import Greetings

def SendHelpMessage(ctx):
    ola = Greetings.DigaOi(ctx)
    help = "Eu ainda estou em desenvolvimento! Mas os meus comandos são os seguintes: \n >>oi\n>>tarefa [nomedapessoa]\n\nMeu código-fonte está na conta da VP no https://replit.com/ e também no GitHub https://github.com/nicollecnunes/bot-trello-discord"
    message = ola + "\n" + help
    return message

