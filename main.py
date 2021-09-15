#importacoes locais
import Author
import Greetings
import MembersId
import Trello
import Help

#importacoes externas
import discord
from decouple import config
from discord.ext import commands


#configuracao do padrao que vem antes do comando e da nao diferenciacao entre maiusculas e minusculas
client = commands.Bot(command_prefix = ">>", case_insensitive = True)

#retorno no terminal para avisar que o bot esta rodando
@client.event
async def on_ready():
  print("Bot Online")

#varias opcoes de greetings
@client.command()
async def ola(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

@client.command()
async def oi(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

@client.command()
async def eai(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

@client.command()
async def ei(ctx):
    await ctx.send(Greetings.DigaOi(ctx))


#solicitacao que busca no trello o id do autor e suas tarefas pendentes
@client.command()
async def tarefa(ctx, name):
    name_author = Author.GetName(ctx)
    id_member_trello = MembersId.GetMemberId(name)
    if (id_member_trello != "error"):
        response = Trello.GetCardsMemberIsOn(id_member_trello)
        #acha a tarefa e manda a mensagem
        if (response == ""):
            await ctx.send(f"{name_author}, você já fez todas as suas tarefas!")
        else:
            await ctx.send(f"{name_author}, você precisa fazer as seguintes tarefas: \n {response}")
    else:
        await ctx.send(f"Poxa, {name_author}, eu não te conheço ainda! Peça para alguém da VP te cadastrar no BOT :)")
    

@client.command()
async def helpme(ctx):
    await ctx.send(Help.SendHelpMessage(ctx))

#inicia o bot
token = config("TOKENSECRETO")
client.run(token)