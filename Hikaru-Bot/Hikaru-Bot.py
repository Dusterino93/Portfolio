# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:07:38 2021

@author: doand
"""

# To import the necessary functions and library for the discord bot
import discord
from discord.ext import commands
import asyncio
import youtube_dl
import os
#import music
TOKEN = 'ODA3NzE1MDE1MTg4Njc2NzAw.YB8BOg.6dd8MEOUsYlwoCrmpEIdnUo-Ymo'

bot = discord.Client()

##################################################################
# Just to make sure bot is working
@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

##################################################################
# Easter Eggs
# When certain people greet the bot, it'll return a message
@bot.event
async def on_message(message):
    message.content = message.content.lower()
    print(str(message.author) + ": " + str(message.content))

    if message.author == bot.user:
        return

    #Sends custom messages based on User's ID

    #Message sent if user is Me
    if message.content == ("i summon server bot in attack position!") and message.author.id == 321151280192028673:
        await message.channel.send("Gawddamnit Truck-Kun! Wrong Isekai! Wrong Isekai!!")
        await message.channel.send('https://tenor.com/view/panic-oh-no-hikaru-no-go-gif-13090623')

    #Message sent if user is Andy (lil bro).
    elif message.content.startswith("onii-chan~") and message.author.id == 314950798956298240:
        await message.channel.send("You're back online, " + str(message.author) + ". B-b-baka!")
        await message.channel.send ("https://tenor.com/view/baka-loli-gif-19487798")

    #Sends a message to tell the user the correct phrase to send Easter Eggs
    elif message.content == ("hello bot") or message.content == ("hi bot"):
        userID = message.author.id
        if userID == 480575542362505226 or 276107653472714762 or 171339356013854722 or 264288156822536192 or 321151280192028673:
            await message.channel.send("I have a name, you know. And it's Hikaru, HMPH!")
            await message.channel.send('https://tenor.com/view/ash-hmph-upset-disappointed-irritated-gif-15924314')
            return

    #Message sent if user is one of my friends.
    elif message.content == ("hello hikaru") or message.content == ("hi hikaru"):
        #If the author is Emily
        if message.author.id == 480575542362505226:
            await message.channel.send("🚀🚀🚀")
            await message.channel.send('https://tenor.com/view/doge-rocket-gif-4714547')
        #If the author is Miguel
        elif message.author.id == 276107653472714762:
            await message.channel.send("Joseph Joestar: The next thing you're gonna say is 'Dustin, you're a fuckin' idiot, lol!")
            await message.channel.send('https://tenor.com/view/joseph-joestar-smiling-jojos-bizarre-encyclopedia-anime-pointing-gif-8300882')
        #If the author is Mark
        elif message.author.id == 171339356013854722:
            await message.channel.send("Someone call the fire brigade! Somebody HOT HOT HOT just arrived 😏")
            await message.channel.send('https://tenor.com/view/ace-onepiece-flaming-flaming-fire-gif-12163183')
        #If the author is Chris
        elif message.author.id == 264288156822536192:
            await message.channel.send("New bot. Who dis? Ah, Issu that you Kurisu?")
            await message.channel.send('https://tenor.com/view/chuunibyou-anime-kawaii-yes-gif-8215787')
        else:
            return

##################################################################
# Role-Selection Bot
# To have the bot assign a role based on a reaction to a specific message
@bot.event
async def on_raw_reaction_add(payload):
    msg_id = payload.message_id
    # if msg_id == 806945535423676446:
    if msg_id == 808225063308230706:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Members')
        elif payload.emoji.name == '🎧':
            role = discord.utils.get(guild.roles, name='DJ')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")
    else:
        pass

@bot.event
async def on_raw_reaction_remove(payload):
    msg_id = payload.message_id
    # if msg_id == 806945535423676446:
    if msg_id == 808225063308230706:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Members')
        elif payload.emoji.name == '🎧':
            role = discord.utils.get(guild.roles, name='DJ')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            user_id = payload.user_id
            server = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
            member = server.get_member(user_id)
            if not member:
                member = await server.fetch_member(user_id)
            try:
                await member.remove_roles(role)
                print("done")
            except:
                print("Member not found.")
        else:
            print("Role not found.")
    else:
        pass

##################################################################



bot.run(TOKEN)
