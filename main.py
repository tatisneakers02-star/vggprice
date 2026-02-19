import discord
from discord.ext import commands

# Configuramos el bot
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

# ABAJO PON TU TOKEN ENTRE LAS COMILLAS
bot.run('MTQ3Mzk1NzY2OTc3MjQ2MDA0Mw.Gzs0vx.AlI5Z_kYuyxO2_su1eJrIUSYDFMLUatxT3M6tc')
