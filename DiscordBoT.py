import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send("Cog ready to fire")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog already on fire")
    except commands.ExtensionNotFound:
        await ctx.send("Cog went missing")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Undecked cog")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Cog ready to fire")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Never heard of this🤔")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Command Missing Required Arguments")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Add Token Here
client.run("Discord_Token_Goes_Here")
