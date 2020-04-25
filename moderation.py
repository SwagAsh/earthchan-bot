import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, cxt, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await cxt.send(f'Okay. {member} has been kicked from the server.')

    @commands.command(aliases = ['foreverkick'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, cxt, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await cxt.send(f'{member} has been banned from the server. Bye Bye!')

    @commands.command(aliases = ['unforeverkick'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, cxt, *, member):
        banned_users = await cxt.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await cxt.guild.unban(user)
                await cxt.send(f'Ok! {user} can now rejoin the server!')
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, cxt, amount=5):
        await cxt.channel.purge(limit=amount)
        await cxt.send(f':wastebasket: **Removed {amount} messages!** :thumbsup:')

def setup(client):
    client.add_cog(Moderation(client))