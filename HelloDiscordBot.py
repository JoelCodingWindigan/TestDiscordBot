import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    print("The Bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am fucked")


token = 'MTE5OTc5MTM5OTk1Mjk3ODA2MA.GWx2Ty.cYzHqOQzYJLnubNG1MW8HFn3kltJkya5QydmGY'
client.run(token)
