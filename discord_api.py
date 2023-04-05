import os
import requests
import discord
import config
from app.openai import chatgpt_response

discord_token = config.config['development'].MONGAI_BOT_TOKEN


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    
    async def on_message(self, message):
        print(message.content)
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return
        command, user_message=None,None

        for text in ['/ai','/bot','/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text,'')
                print(command, user_message)

        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer:'{bot_response}'")

intentes = discord.Intents.default()
intentes.message_content = True

client = MyClient(intents=intentes)

            



"""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return

        # Send the message to the API endpoint
        data = {'text': message.content}
        response = requests.post(API_ENDPOINT, json=data)

        # Send the response back to Discord
        if response.ok:
            message = response.json()['message']
            await message.channel.send(message)
        else:
            await message.channel.send('Error generating response')

"""



