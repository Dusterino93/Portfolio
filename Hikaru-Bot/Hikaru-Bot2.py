# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:07:38 2021

@author: doand
"""

# To import the necessary functions and library for the discord bot
import discord
from discord.ext import commands
import youtube_dl
import os
#import music
TOKEN = '#####################################################'

bot = commands.Bot('!', description='Yet another music bot.')

##################################################################
# Easter Eggs
# When certain people greet the bot, it'll return a message
@bot.event
async def on_message(message):
    message.content = message.content.lower()
    print(str(message.author) + ": " + str(message.content))
    if message.author == bot.user:
        return
    if message.content == ("hello"):
        if str(message.author) == "Dusterino#1007":
            await message.channel.send("Hello " + str(message.author) + "-nii chan~!")

    if message.content.startswith("dustin-niichan"):
        if str(message.author) == "AndyH#6969":
            await message.channel.send("You're back online, " + str(message.author) + ". B-b-baka!")

    if message.content.startswith("hello hikaru"):
        if str(message.author) == "aiileru#1695":
            await message.channel.send("*tips fedora* M'lady~")
        if str(message.author) == "Smigga77#1808":
            await message.channel.send(
                "Joseph Joestar: The next thing you're gonna say is 'Dustin fucking stupid lol'!")


##################################################################
# Role-Selection Bot
# To have the bot assign a role based on a reaction to a specific message
@bot.event
async def on_raw_reaction_add(payload):
    msg_id = payload.message_id
    # if msg_id == 806945535423676446:
    if msg_id == 807766801579638822 or 806945535423676446:
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

@bot.event
async def on_raw_reaction_remove(payload):
    msg_id = payload.message_id
    # if msg_id == 806945535423676446:
    if msg_id == 807766801579638822 or 806945535423676446:
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

##################################################################

# Just to make sure bot is working
@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

bot.run(TOKEN)
