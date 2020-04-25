import discord
import random
import os
from discord.ext import commands

earthchan = commands.Bot(command_prefix = ';')

t = open("token.txt", "r")

earthchan.remove_command('help')

@earthchan.event
async def on_ready():
    await earthchan.change_presence(status=discord.Status.online, activity=discord.Streaming(name='welcome people!', url='https://www.youtube.com/watch?v=VFuBTK2wAHU'))

@earthchan.event
async def on_guild_join(guild):
    channel = earthchan.get_channel(678308902038667318)
    embed=discord.Embed(title="Hello guys! EarthChan here.", description="I am a multipurpose bot who is still a work in progress, but i can still do a lot of things! try using the ;help command to see what i can do! Some fun facts about me: I was programmed in python entirely by SwagAsh#3759. Pretty cool right?", colour = discord.Colour.blurple())
    embed.set_author(name="EarthChan")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/695628979071352872/702575494679363604/2Q.png")
    await channel.send(embed=embed)

@earthchan.command()
async def load(cxt, extension):
    earthchan.load_extension(f'categories.{extension}')

@earthchan.command()
async def unload(cxt, extension):
    earthchan.unload_extension(f'categories.{extension}')

for filename in os.listdir('./categories'):
    if filename.endswith('.py'):
        earthchan.load_extension(f'categories.{filename[:-3]}')

@earthchan.command(aliases = ['askme', 'question'])
async def ask(cxt, question):
    response = [
    'Yes :)',
    'No :|',
    'Of *course* :grin:',
    'Definitely :smile:',
    '__Highly Probable__ :grinning:',
    '*No chance* :unamused:',
    '**Don\'t keep your hopes high** :pensive:',
    'Never gonna happen!',
    'That\'s not possible! :laughing:', 
    'I dunno ¯\\_(ツ)_/¯',
    'Ask later :sleeping:'
    ]
    await cxt.send(random.choice(response))

@earthchan.command()
async def compliment(cxt, member : discord.Member):
    comps = [
        f'Hey, {member}, you are awesome!',
        f'You got nice lookin\' hair there, {member}.',
        f'{member}, you made my day!',
        f'Man, {member} has such a big brain!',
        f'You\'re probably the most wholesome person i met, {member}.',
        f'Thank you for existing, {member}.',
        f'The only thing that would make you any worse is if you weren\'t you, {member}',
        f'If there was a perfect person in this world, it just might be {member}'
    ]
    await cxt.send(random.choice(comps))

@earthchan.command(aliases = ['nickname'])
@commands.has_permissions(manage_nicknames=True)
async def nick(cxt, member : discord.Member, nick=None):
    await member.edit(nick=nick)
    await cxt.send(f':white_check_mark: **Ok, {member} now has the nickname {nick}!** :pencil2:')

@earthchan.command(aliases = ['stats'])
async def ping(cxt):
    steat = discord.Embed(
        title = ':ping_pong: **Pong!**',
        description = f'{round(earthchan.latency*1000)}ms',
        colour = discord.Colour.purple()
    )
    await cxt.send(embed=steat)

@earthchan.command()
async def invite(cxt):
    await cxt.author.send(f'{cxt.author.mention} **Here is the link for the EarthChan Testing server!** https://discord.gg/dAm265y')

@earthchan.command()
async def help(cxt):
    help = discord.Embed(
        title = ':arrow_forward: **Commands**',
        description = '(WIP) _Categories: Miscellaneous, Moderation,None._ A list of commands (So Far) for the EarthChan bot.',
        colour = discord.Colour.dark_green()
    )    
    help.set_footer(text='Join the EarthChan Beta Testers discord server by sending a dm to SwagAsh#3759')
    help.set_image(url='https://cdn.discordapp.com/attachments/702629328596238440/702682112330825748/sVv5Lo1R_400x400-removebg-preview_1_75.png')
    help.set_author(name='EarthChan Help Command')
    help.set_thumbnail(url='https://cdn.discordapp.com/attachments/702629328596238440/702680083927924767/LWjsNvDY_400x400.png')
    help.add_field(name=':white_small_square: hello', value='Says hello to whoever sent the command. Usage: ;hello')
    help.add_field(name=':white_small_square: clear', value='Clears the last certain amount of messages. Usage: ;clear <amount>')
    help.add_field(name=':white_small_square: dm', value='Sends you a direct Message. Usage: ;dm')
    help.add_field(name=':white_small_square: kick', value='(requires admin role) Kicks a member from the server. Usage: ;kick <member>')
    help.add_field(name=':white_small_square: ban', value='(requires admin role) Bans a member from the server. Usage: ;ban <member>')
    help.add_field(name=':white_small_square: unban', value='(requires admin role) Unbans a member from the server. Usage: ;unban <banned user>')
    help.add_field(name=':white_small_square: ask', value='Ask a question to get a random answer (like 8ball). Usage: ;ask <question>')
    help.add_field(name=':white_small_square: compliment', value='Show how much you appreciate someone by giving them a nice compliment. Usage: ;compliment <member>')
    help.add_field(name=':white_small_square: nick', value='(Requires manage nicknames permission) Changes your nickname or other peoples nicknames. Usage: ;nick <member> <nickname>')
    help.add_field(name=':white_small_square: nuke', value='(2 hour limit) Spam a user with direct messages. Usage: ;nuke <member> <message>')
    help.add_field(name=':white_small_square: ping', value='Shows the latency for the bot to respond. Usage: ;ping')
    help.add_field(name=':white_small_square: invite', value='Join our official testing server! Usage: ;invite')
    help.add_field(name=':white_small_square: help', value='shows this embed. Usage: ;help')

    await cxt.send(embed=help)


earthchan.run(t.read())
