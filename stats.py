import  discord
from discord.ext import commands
class StatsAndData(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases = ['latency'])
    async def ping(cxt):
        steat = discord.Embed(
            title=':ping_pong: **Pong!**',
            description=f'{round(earthchan.latency * 1000)}ms',
            colour=discord.Colour.purple()
        )
        await cxt.send(embed=steat)
def setup(client):
    client.add_cog(StatsAndData(client))