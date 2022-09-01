import os
import discord
import requests
from discord.ext import commands 
from dotenv import load_dotenv
from matplotlib.pyplot import imshow,show
from uuid import uuid4
import shutil
from ImageDescriptor import ImageDescriptor
import traceback

# bot URL: https://discord.com/api/oauth2/authorize?client_id=942393785009176676&permissions=8&scope=bot
# intents = discord.Intents.default()
intents = discord.Intents(0, messages=True, message_content=True)
client = discord.Client(intents = intents)
# client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    try:
        # to make bot ignore message by it self.
        if message.author == client.user:
            return
        print(message.content)
        print(message.attachments)
        url = message.attachments[0].url
        content = message.content
        user = message.author
        print(url)
                
    except IndexError:
        print('No attachment found')
        # traceback.print_exc()
        
    else:
        # cheak if attachment is 'image' 
        if url[0:27] == 'https://cdn.discordapp.com/': # and content == '':
            
            path = save_img(url)
            
            model = ImageDescriptor(path)    
            messageback = "this picture is " + model.get_description()
            await reply(message, messageback)
        
#reply massage to user.
async def reply(message, massageback ,mention_author = False):  
    await message.reply(massageback,mention_author=mention_author)
    
def save_img(url):
    r = requests.get(url, stream=True)
    imageName = 'img/' + str(uuid4()) + '.jpg'      # uuid creates random unique id to use for image names
    with open(imageName, 'wb') as out_file:
        print('Saving image: ' + imageName)
        shutil.copyfileobj(r.raw, out_file)     # save image (goes to project directory)
    return imageName


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)