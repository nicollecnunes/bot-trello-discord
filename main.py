import Author
import Greetings
import MembersId
import Trello

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">>", case_insensitive = True)

@client.event
async def on_ready():
  print("Bot Online")

@client.command()
async def ola(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

async def oi(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

async def eai(ctx):
    await ctx.send(Greetings.DigaOi(ctx))

async def ei(ctx):
    await ctx.send(Greetings.DigaOi(ctx))


@client.command()
async def tarefa(ctx, name):
    name_author = Author.GetName(ctx)
    id_member_trello = MembersId.GetMemberId(name)
    if (id_member_trello != "error"):
        response = Trello.GetCardsMemberIsOn(id_member_trello)
        #acha a tarefa e manda a mensagem
        await ctx.send(f"{name_author}, você precisa fazer as seguintes tarefa: \n {response}")
    else:
        await ctx.send(f"Poxa, {name_author}, eu não te conheço ainda! Peça para alguém da VP te cadastrar no BOT :)")
    

client.run('BOT-TOKEN-HERE')