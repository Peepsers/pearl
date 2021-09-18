import discord
from discord.ext import commands

class reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="des vidéos de chien", url="https://www.youtube.com/watch?v=wl4m1Rqmq-Y"))
        print('🤖 Bot Discord connecté au(x) serveur(s)')

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if self.client.user.mentioned_in(message):
            bot_message = 'Je vais te boter le cul si tu me mentionnes encore, ' + message.author.name + ' !'
            await message.channel.send(bot_message)
        
        msg = message.content
        if msg.lower() == "cringe":
            await message.delete()
            await message.channel.send("https://tenor.com/view/dies-of-cringe-cringe-gif-20747133")  # ,delete_after=5

        if msg.lower() == "bonne nuit" or message.content.lower() == "a plus" or message.content.lower() == "au revoir" or message.content.lower() == "https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220":
            await message.channel.send("https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220")

        if msg.lower() == "you":
            await message.delete()
            await message.channel.send('https://cdn.discordapp.com/attachments/751532937094103132/847173219961405490'
                                       '/image0.gif')

def setup(client):
    client.add_cog(reactions(client))
