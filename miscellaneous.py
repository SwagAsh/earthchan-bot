import discord
import random
from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def hello(self, cxt):
        hello = [
            'Hello',
            'Hi',
            'Kon\'nichiwa',
            'Hola',
            'Bonjour',
            'Guten Tag',
            'Zdravstvuyte'
        ]
        await cxt.send(':wave: **' + random.choice(hello) + f', {cxt.author.mention}!**')

    @commands.command()
    async def dm(self, cxt):
        await cxt.author.send('Sup. I slid into your DMs.')

    @commands.command(aliases = ['spamdm'])
    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.has_permissions(view_audit_log=True)
    async def nuke(self, cxt, member : discord.Member, message='nuke\'d'):

        await cxt.send(f':boom: Okay, nuking {member} now... :boom:')
    
        tactical = await member.create_dm()
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)
        await tactical.send(message)

        await cxt.send(':raised_hand: Now wait **2 Hours** before using this command again! :alarm_clock:')
    @nuke.error
    async def nuke_error(self, cxt, error):   
        if isinstance(error, commands.CommandOnCooldown):
            msg = ':octagonal_sign: Hey, you can use this command again in **{:.0f}s**'.format(error.retry_after)
            await cxt.send(msg)
        else:
            raise error

def setup(client):
    client.add_cog(Miscellaneous(client))