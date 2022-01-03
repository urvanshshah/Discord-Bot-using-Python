## Discord-Bot-using-Python


import discord
from discord import member
from discord.ext import commands
import requests
import json
import os
import random

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "=", intents=intents)

@client.command()
@commands.is_owner()
async def load(ctx,extension):
#    if(ctx.guild.owner == ctx.author):
        client.load_extension(f'cogs.{extension}')
        await ctx.send('{extension} loaded')
#    else:
#        await ctx.reply(f'Oops! You cannot use this command.')

@client.command()
@commands.is_owner()
async def unload(ctx,extension):
#    if(ctx.guild.owner == ctx.author):
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} unloaded')
#    else:
#        await ctx.reply(f'Oops! You cannot use this command.')
    
@client.command()
@commands.is_owner()
async def reload(ctx,extension):
#    if(ctx.guild.owner == ctx.author):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} reloaded')
#    else:
#        await ctx.reply(f'Oops! You cannot use this command.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@client.event
async def on_ready():
    print("The Bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the urru bot")

@client.command()
async def bye(ctx):
    await ctx.send("GoodBye, I will take your leave")

@client.command()
async def kem_cho(ctx):
    await ctx.send("Hu Majama, what about you:)")

@client.command()
async def joke(ctx):
    joke_list = ['Today a man knocked on my door and asked for a small donation toward the local swimming pool. I gave him a glass of water.',
                'Maybe if we start telling people their brain is an app, they will want to use it', 
                'I got a new pair of gloves today, but they are both lefts, which on the one hand is great, but on the other, it is just not right.',
                'People who take care of chickens are literally chicken tenders',
                'It was an emotional wedding. Even the cake was in tiers',
                'The future, the present, and the past walk into a bar. Things got a little tense',
                'Last night my girlfriend was complaining that I never listen to her… or something like that',
                'A told my girlfriend she drew her eyebrows too high. She seemed surprised',
                'I failed math so many times at school, I cannot even count',
                'Why was six afraid of seven? Because seven eight nine',
                'What do fish say when they hit a concrete wall? Dam!']
    random_joke = random.choice(joke_list)
    await ctx.send(f'Here is a joke : {random_joke}')

@client.command()
async def fun_fact(ctx):
    fun_fact_list = ['It is Impossible to Hum While You Hold Your Nose',
                    'Bees Can Detect Bombs and Rabbits cannot puke',
                    'According to recent research, the human nose can distinguish at least a trillion different odors',
                    'The word “strengths” is the longest word in the English language with only one vowel.',
                    'Hair and nails grow faster during pregnancy',
                    'The wood frog can hold its pee for up to eight months']
    random_fun_fact = random.choice(fun_fact_list)
    await ctx.send(f'Here is a fun fact : {random_fun_fact}')

    

@client.command()
async def slap(ctx, member:discord.Member):
    await ctx.send(f'{ctx.author.mention} slaps {member.mention} :wave:')


punch_gifs = ['https://c.tenor.com/BoYBoopIkBcAAAAM/anime-smash.gif',
            'https://c.tenor.com/EvBn8m3xR1cAAAAC/toradora-punch.gif',
            'https://c.tenor.com/s0bU-NO1QIQAAAAM/anime-punch.gif',
            'https://c.tenor.com/n7LKoJVrwM8AAAAC/anime-punch.gif',
            'https://c.tenor.com/3CUBZHrDUvUAAAAC/punch-combo.gif']

@client.command()
async def punch(ctx , member:discord.Member):
    embed = discord.Embed(title = 'Punched You!',
                            colour = (discord.Colour.random()), 
                            description = f'{ctx.author.mention} Punches :right_fist: {member.mention}')
    embed.set_image(url = (random.choice(punch_gifs)))
    await ctx.send(embed = embed)


hug_gifs = ['https://c.tenor.com/dIvoDyyk5LIAAAAC/anime-hug-sweet.gif',
            'https://c.tenor.com/2bWwi8DhDsAAAAAC/hugs-and-love.gif',
            'https://c.tenor.com/83QLplerW8sAAAAC/anime-hug.gif',
            'https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif',
            'https://c.tenor.com/ek1fEuNncMAAAAAC/hug-anime.gif']

@client.command()
async def hug(ctx , member:discord.Member):
    embed = discord.Embed(title = 'Hugging You!',
                            colour = (discord.Colour.random()), 
                            description = f'{ctx.author.mention} Hugges :hugging: {member.mention}')
    embed.set_image(url = (random.choice(hug_gifs)))
    await ctx.send(embed = embed)


beat_gifs = ['https://c.tenor.com/tHmgX-b9UVMAAAAi/beating-a-dead-horse-funny.gif',
                'https://c.tenor.com/02XWVGkAdt0AAAAd/kunleinho-kunleinhogifs.gif',
                'https://c.tenor.com/ORPuJm61lnQAAAAC/beating-impact.gif',
                'https://c.tenor.com/26nQ_QG7DiMAAAAM/telangana-sakuntala-beating-sunil-telangana-sakuntala.gif',
                'https://c.tenor.com/cnXV00w8TzEAAAAM/vadivel-vadivelu.gif']

@client.command()
async def beat(ctx , member:discord.Member):
    embed = discord.Embed(title = 'Beating You!',
                            colour = (discord.Colour.random()), 
                            description = f'{ctx.author.mention} Beats :punch_tone1: {member.mention}')
    embed.set_image(url = (random.choice(beat_gifs)))
    await ctx.send(embed = embed)


@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id)
    await channel.send(f"Welcome to this server {member.mention} :man_bowing: ")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(channel_id)
    await channel.send(f"Goodbye {member.mention} :man_bowing: ")

@client.command()
async def rps(ctx,message):
    answer = message.lower()
    rps_gifs = ['https://c.tenor.com/Aqvwi1BYCyAAAAAC/friends-rock-paper-scissors.gif',
                    'https://c.tenor.com/mpdRJ7wlNNIAAAAM/rock-paper.gif',
                    'https://c.tenor.com/uupnJ56cTYkAAAAM/the-big-bang-theory-tv-shows.gif',
                    'https://c.tenor.com/w2rIJOAcZOsAAAAd/noo-yess.gif',
                    'https://c.tenor.com/aNX1d0WbcYIAAAAd/rock-paper-scissors-game.gif']
    choices = ['rock','paper','scissors']
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.send("invalid option! Please use one of these : rock , paper , scissors")
        return
    else:
        if computers_answer == answer:
            embed = discord.Embed(title = f'Tie! We both Picked {answer}'
                                    ,colour = (discord.Colour.random()))
            embed.set_image(url = 'https://c.tenor.com/wyfhYqF1tJIAAAAC/mark-wahlberg-wahlberg.gif')
            await ctx.send(embed = embed)
        if computers_answer == "rock":
            if answer == 'paper':
                embed = discord.Embed(title = f'You Win :partying_face: ! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)
        if computers_answer == "paper":
            if answer == 'rock':
                embed = discord.Embed(title = f'I Win :partying_face:! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)
        if computers_answer == "scissors":
            if answer == 'rock':
                embed = discord.Embed(title = f'You Win :partying_face:! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)
        if computers_answer == "rock":
            if answer == 'scissors':
                embed = discord.Embed(title = f'I Win :partying_face:! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)
        if computers_answer == "paper":
            if answer == 'scissors':
                embed = discord.Embed(title = f'You Win :partying_face:! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)
        if computers_answer == "scissors":
            if answer == 'paper':
                embed = discord.Embed(title = f'I Win :partying_face:! I picked {computers_answer} and you picked {answer}!'
                                    ,colour = (discord.Colour.random()))
                embed.set_image(url = (random.choice(rps_gifs)))
                await ctx.send(embed = embed)

@client.command()
async def urru_bot(ctx):
    await ctx.send('''
Hello, I am the urru bot
Here are some of my services :
--> Greetings like 𝕙𝕖𝕝𝕝𝕠  , 𝕓𝕪𝕖 , 𝕜𝕖𝕞_𝕔𝕙𝕠 , 𝕞𝕖𝕞𝕓𝕖𝕣_𝕛𝕠𝕚𝕟 , 𝕞𝕖𝕞𝕓𝕖𝕣_𝕝𝕖𝕒𝕧𝕖
--> GAMES like rock, paper, sissors, shoot!
--> Change 𝕟𝕚𝕔𝕜𝕟𝕒𝕞𝕖 and back
--> Laugh at a 𝕛𝕠𝕜𝕖 and enjoy several 𝕗𝕦𝕟_𝕗𝕒𝕔𝕥𝕤
--> Use fun commands for 𝕡𝕦𝕟𝕔𝕙 , 𝕤𝕝𝕒𝕡 , 𝕙𝕦𝕘 , 𝕓𝕖𝕒𝕥 involving other servermates
* Bot work is under progress , till then stay tune and have fun :)
    ''')

client.run(token)
