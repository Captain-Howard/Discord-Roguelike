import discord
import level_generation
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

def blocks(infile, bufsize=1024):
    while True:
        try:
            data=infile.read(bufsize)
            if data:
                yield data
            else:
                break
        except:
            print("Error has occurred")

@client.event
async def on_message(input):
    if input.content == "test":
        await input.channel.send("The test is working.")
    await client.process_commands(input)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def create_map(ctx):
    gen = level_generation.Generator()
    gen.gen_level()
    gen.gen_tiles_level()
    i = 1
    with open('level.txt', 'r') as f:
        for c in blocks(f, 64):
            message = "Row " + str(i) + " complete!"
            await ctx.channel.send(message)
            print(c)
            i += 1

    await ctx.send('Map Created!')


text_file = open("Info.txt", "r")
client_secret = text_file.read(59)
client.run(client_secret)
