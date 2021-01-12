# bot.py
import os
import random
import cv2

import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='$')

@bot.command(name='wealth', help='Check your wealth')
async def nine_nine(ctx, user: discord.Member = None):
    wealth_quotes = [
        'Wah u this year got money oh',
        'If you stop spending on Shopee maybe u can be rich bodo',
        'Got abit of money la',
        'oi u think money drop from sky is it',
        'stop spending money bodo',
        'Hope ur angpao only got RM1 inside',
        'Stop begging money from me bitch',
        'Go buy bitcoin la bodo',
        'I bet u cook rice in a pan bodo',
        'Get a job u begger',
        'can donate abit to you la this year',
        'If you wear red this year, you look like a clown',
        'Pls gimme angpao this year laoban',
        'Laoban heng heng',
    ]

    response = random.choice(wealth_quotes)
    if user!=None:
        await ctx.send(f"{user.mention } " + response)
    else:
        await ctx.send(response)
    
@bot.command(name='kongsi', help='Uploads face swapped image')
async def imageUpload(ctx, user: discord.Member = None):
    filename = "user_avatar.jpg"
    if user!=None:
        await user.avatar_url.save(filename)
    else:
        await ctx.author.avatar_url.save(filename)

    # resize image
    output = cv2.resize(cv2.imread(filename), (200, 200))
    cv2.imwrite(filename,output) 
    
    ImageCNY = Image.open("cny.jpg")
    ImageUser = Image.open('user_avatar.jpg')
    ImageCNY.paste(ImageUser, (290,70))
    ImageCNY.save("cny.jpg")
    file = discord.File(fp="cny.jpg")
    await ctx.send("Happy CNY; lancau na lai",file=file)

bot.run(TOKEN)
