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

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=" $wealth"))
    print("bot ready")

@bot.command(name='wealth', help='Check your wealth')
async def nine_nine(ctx, user: discord.Member = None):
    wealth_quotes = [
        'Wah u this year got money oh',
        'If you stop spending on Shopee maybe u can be rich',
        'Got abit of money la',
        'u think money drop from sky is it',
        'stop spending money',
        'Hope ur angpao only got RM1 inside',
        'Stop begging money from me',
        'Go buy bitcoin',
        'can donate abit la this year',
        'If you wear red this year, you would look like a clown',
        'Pls gimme angpao this year',
        'You are gonna be super lucky',
    ]

    response = random.choice(wealth_quotes)
    if user!=None:
        await ctx.send(f"{user.mention } " + response)
    else:
        await ctx.send(f"{ctx.author.mention} " + response)
    
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
    cny_quotes = [
        'Happy CNY; lancau na lai',
        'Gong Xi Fa Cai; Gong hei fatt choi',
        'Hepi cainis nu yer',
        'Send me E-Angpao',
        'BAK KWA CAK BISSS',
        'Going to your house to eat all your bakwa',
        'I give u orange, u give me angpao. EZ trade',
        'I wear red to your house dun worry',
        'Aunty & Uncle, pls dun harass me',
    ]
    cny_wish = random.choice(cny_quotes)
    await ctx.send(cny_wish,file=file)

bot.run(TOKEN)
