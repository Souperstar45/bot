Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["hello", "hi", "howdy"]

starter_encouragements = [
  "hello!", "good morning/afternoon/evening", "we missed you!", "welcome back!"
]

async def message(message):
  if message.author == client.user:
   return

msg = message.content

if any(word in msg for word in sad_words):
  await message.channel.send(random.choice(options))

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
   encouragements = db["encouragements"]
   encouragements.append(encouraging_message)
   db["encouragements"] = encouragements
  else:
   db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
   del encouragements[index]
  db["encouragements"] = encouragements

  options = starter_encouragements
  if "encouragements" in db.keys():
   options = options + db["encouragements"]

@client.event
async def on_message(message):
    if message.author == client.user:
      return

if msg.startswith("$new"):
   encouraging_message = msg.split("$new ",1)[1]
   update_encouragements(encouraging_message)
  await message.channel.send("New encouraging message added.")

if msg.startswith("$del"):
   encouragements = []
   if "encouragements" in db.keys():
   index = int(msg.split("$del",1)[1])
   delete_encouragment(index)
   encouragements = db["encouragements"]
  await message.channel.send(encouragements)

client.run(os.getenv('TOKEN'))