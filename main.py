import discord
from discord.ext import commands
import os

# Configuración básica del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def vgg(ctx, region: str, precio: float):
    region = region.lower()
    
    # Cálculos originales pero forzando el símbolo Euro (€)
    if region == "com" or region == "es":
        payout = precio * 0.879
        buyer = precio * 1.20
        titulo = "VGG .COM / ESPAÑA"
    elif region == "uk":
        # Se mantiene tu fórmula original de UK pero el resultado sale en €
        payout = precio * 0.85 
        buyer = precio * 1.15
        titulo = "VGG UK"
    else:
        await ctx.send("❌ Usa: `!vgg com 100` o `!vgg uk 100`")
        return

    # Mensaje final siempre en Euros
    msg = f"✅ **{titulo}**\n💰 Payout: {payout:.2f}€\n🛒 Buyer: {buyer:.2f}€"
    await ctx.send(msg)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Sistema de seguridad para leer el token desde Render
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("ERROR: No se encontró el token en las variables de entorno de Render")
