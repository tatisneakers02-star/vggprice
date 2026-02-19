import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def vgg(ctx, region: str, precio: float):
    region = region.lower()
    if region == "com":
        payout = precio * 0.879
        buyer = precio * 1.20
        msg = f"✅ **VGG .COM**\n💰 Payout: {payout:.2f}$\n🛒 Buyer: {buyer:.2f}$"
    elif region == "uk":
        payout = precio * 0.85 
        buyer = precio * 1.15
        msg = f"✅ **VGG .UK**\n💰 Payout: {payout:.2f}£\n🛒 Buyer: {buyer:.2f}£"
    else:
        msg = "❌ Usa: !vgg com 100"
    await ctx.send(msg)

# Esto es para que Render no crea que el bot ha fallado
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

token = os.getenv('MTQ3Mzk1NzY2OTc3MjQ2MDA0Mw.GnkZQH.K16krfsTXtkv51JzwOUISTRzhe27KMsk5dSgsg')
bot.run(token)
