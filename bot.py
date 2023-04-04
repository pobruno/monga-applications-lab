import os
import requests
import discord
import config

# Configure the Discord bot token and API endpoint
TOKEN = config.DevelopmentConfig.MONGAI_BOT_TOKEN
API_ENDPOINT = 'http://app.monga.dev.br/api/v1/message'

# Configure the Discord client
client = discord.Client()

# Define the on_message event handler


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
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

# Start the Discord client
client.run(TOKEN)
