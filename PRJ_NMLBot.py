import discord
import requests
import json

token= ""
client = discord.Client()



def get_quote():
    response = requests.get("https://zenquotes.io/api/random%22)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "  -" + json_data[0]['a']
    return(quote)




@client.event
async def on_ready():
    print('Logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/im tilted"):
        quote = get_quote()
        await message.channel.send(quote)

							
							
							
print("running")
client.run(token)
