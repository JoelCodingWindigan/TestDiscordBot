import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

#hashmap used to keep track of how often a user says hello world

my_hashmap = {}
@client.event
async def on_ready():
    print("The Bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am fucked")

#count_message needs to take a message parameter
async def count_message(message):
    if message.content.lower() == 'hello world':
         user_id = str(message.author.id)

        # Increment the count for the user or set it to 1 if it doesn't exist
         my_hashmap[user_id] = my_hashmap(user_id, 0) + 1

        # Send a reply with the updated count
         await message.channel.send(f'Hello World count for {message.author.name}: {my_hashmap[user_id]}')

    await bot.process_commands(message)

token = 'MTE5OTc5MTM5OTk1Mjk3ODA2MA.GR3Baj.2dJ8chsLwLMz3S4zoGDwxedDfHDOYFneTcMTiQ'
client.run(token)
