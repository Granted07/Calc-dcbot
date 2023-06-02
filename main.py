from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from discord.ui import view
import threading
import logging

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.reactions = True
bot = discord.Bot(intents=intents)

load_dotenv()

@bot.event
async def on_ready():
    activity=discord.Activity(type=discord.ActivityType.listening, name="/calculator")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('On and ready')

@bot.slash_command(name="calculator", description="shall summon a calculator :yum:")
async def calculator(ctx):
    msg = "Answers will display here"
    calc = discord.Embed(title="```" + msg + "```" , color=0x2f3136)
    r1 = discord.ui.View()
    r2 = discord.ui.View()
    ACbutton = discord.ui.Button(label="AC", style = discord.ButtonStyle.danger)
    bracket1 = discord.ui.Button(label="(", style = discord.ButtonStyle.primary)
    bracket2 = discord.ui.Button(label=")", style = discord.ButtonStyle.primary)
    backspace = discord.ui.Button(label="<=", style = discord.ButtonStyle.primary)
    num1 = discord.ui.Button(label="1", style = discord.ButtonStyle.secondary)
    num2 = discord.ui.Button(label="2", style = discord.ButtonStyle.secondary)
    num3 = discord.ui.Button(label="3", style = discord.ButtonStyle.secondary)
    div = discord.ui.Button(label="/", style = discord.ButtonStyle.primary)
    r1.add_item(ACbutton)
    r1.add_item(bracket1)
    r1.add_item(bracket2)
    r1.add_item(backspace)
    r2.add_item(num1)
    r2.add_item(num2)
    r2.add_item(num3)
    r2.add_item(div)
    await ctx.respond(embed=calc, view=r1)
    await ctx.send(view=r2)

tok = os.getenv('TOKEN')
bot.run(tok)