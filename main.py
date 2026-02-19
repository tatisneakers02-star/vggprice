import discord
from discord.ext import commands
import os

# Configuramos el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def vgg(ctx, region: str, precio: float):
    region = region.lower()
    
    # Cálculos originales pero con símbolo de Euro (€)
    if region == "com" or region == "es":
        payout = precio * 0.879
        buyer = precio * 1.20
        msg = f"✅ **VGG .COM / ESPAÑA**\n💰 Payout: {payout:.2f}€\n🛒 Buyer: {buyer:.2f}€"
    elif region == "uk":
        # Aquí el cálculo se mantiene igual pero forzamos el símbolo €
        payout = precio * 0.85 
        buyer = precio * 1.15
        msg = f"✅ **VGG .UK**\n💰 Payout: {payout:.2f}€\n🛒 Buyer: {buyer:.2f}€"
    else:
        msg = "❌ Usa: `!vgg com 100` o `!vgg uk 100`"
    
    await ctx.send(msg)

# Esto es para que Render sepa que el bot está vivo
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Lee tu token secreto de Render
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
