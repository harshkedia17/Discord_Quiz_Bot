from http import client
# from pydoc import cli
from async_timeout import asyncio
import discord
from django.http import response
import requests
client = discord.Client()
import json
def get_question():
    qs = ''
    id=1
    answer = 0
    response = requests.get('http://127.0.0.1:8000/api/random/')    
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + '\n'
    
    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer']+'\n'
        
        if item['is_correct']:
            answer = id

        id +=1
    
    return(qs,answer)


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('$question'):
        a,b = get_question()
        await message.channel.send(a)

    def check(m):
          return m.author == message.author and m.content.isdigit()

    try:
      guess = await client.wait_for('message',check = check, timeout= 5.0)
    except asyncio.TimeoutError:
        return await message.channel.send('Sorry you took too Long')

    if int(guess.content) == b:
        await message.channel.send("You're right")
    else: 
        await message.channel.send('Oops. That is not right')
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return 
    
#     if message.content.startswith('hello'):
#         await message.channel.send(f'Hello {message.author.name} I am a bot')
        
client.run('OTMxMTAzMzA4MzMwOTg3NTUx.Yd_jhw.QvQ16oSq5leouYD8ZkXrup-B6qA')
