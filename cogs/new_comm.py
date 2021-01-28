import discord
from discord.ext import commands, tasks
import os
import startbot

class New_Commands(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.send_onready_message.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready TeamBoT")

    @commands.command(aliases=["Ping"])
    async def ping(self,ctx):
        await ctx.send(f"🏓   {round(self.client.latency)*1000}ms")

    @commands.command(aliases=["hello","hola","namaste"])
    async def hi(self,ctx):
        await ctx.send('Namaste🙏🏻 {0.display_name}.'.format(ctx.author))

    @commands.command(aliases=["timetable"])
    async def tt(self,ctx):
        list=[]
        for filename in os.listdir('./LogIn'):
            if not filename.endswith('.py'):
                handle = open(os.path.join('LogIn',filename))
                file = handle.read()
                for i in file.splitlines():
                    str=i.replace("="," ")
                    str=str.replace("->"," ")
                    list.append(str)
                handle.close()
        await ctx.send("📅Time Table")
        for i in range(len(list)):
            await ctx.send(list[i])

    @commands.command(aliases=["add_timetable","add_to_timetable"])
    async def add_tt(self,ctx,*,details):
        list=[]
        details = details.split(',')
        if len(details)!=4:
            await ctx.send("Wrong number of arguments ❌")
        else:
            await ctx.send("📅Time Table")
            for filename in os.listdir('./LogIn'):
                if not filename.endswith('.py'):
                    handle = open(os.path.join('LogIn',filename),'a')
                    handle.write(details[0]+'->'+details[1]+'='+details[2]+'='+details[3]+'\n')
                    handle.close()
                    handle = open(os.path.join('LogIn',filename))
                    file = handle.read()
                    for i in file.splitlines():
                        str=i.replace("="," ")
                        str=str.replace("->"," ")
                        list.append(str)
                    handle.close()
            for i in range(len(list)):
                await ctx.send(list[i])

    @commands.command(aliases=["del_timetable","delete_from_timetable","delete_timetable"])
    async def del_tt(self,ctx,*,details):
        list=[]
        flag=0
        details = details.split(',')
        if len(details)!=4:
            await ctx.send("Wrong number of arguments ❌")
        else:
            for filename in os.listdir('./LogIn'):
                if not filename.endswith('.py'):
                    with open(os.path.join('LogIn',filename),'r') as handle:
                        lines = handle.readlines()
                    with open(os.path.join('LogIn',filename),'w') as handle:
                        for line in lines:
                            if line.strip('\n')!=(details[0]+'->'+details[1]+'='+details[2]+'='+details[3]):
                                handle.write(line)
                            else:
                                flag=1
                    handle.close()
                    handle = open(os.path.join('LogIn',filename))
                    file = handle.read()
                    for i in file.splitlines():
                        str=i.replace("="," ")
                        str=str.replace("->"," ")
                        list.append(str)
                    handle.close()
            if flag==0:
                await ctx.send("No such entry ❌")
            else:
                await ctx.send("📅Time Table")
                for i in range(len(list)):
                    await ctx.send(list[i])

    @tasks.loop(seconds = 60)
    async def send_onready_message(self):
    #Add your channel ID number
      channel = self.client.get_channel("Channel ID number goes here")
      await channel.send(tst.status())

    @send_onready_message.before_loop
    async def before_send(self):
      await self.client.wait_until_ready()
      return

def setup(client):
    client.add_cog(New_Commands(client))
