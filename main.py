import discord
from discord.ext import commands
import os

# Configuración básica
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def vgg(ctx, region: str, precio: float):
    region = region.lower()
    
    # Mantenemos tus porcentajes originales pero TODO con el símbolo €
    if region == "com" or region == "es":
        payout = precio * 0.879
        buyer = precio * 1.20
        titulo = "VGG .COM / ESPAÑA"
    elif region == "uk":
        payout = precio * 0.85 
        buyer = precio * 1.15
        titulo = "VGG UK"
    else:
        await ctx.send("❌ Usa: `!vgg com 100` o `!vgg uk 100`")
        return

    # Mensaje simple y claro en Euros
    respuesta = (
        f"✅ **{titulo}**\n"
        f"💰 **Payout:** {payout:.2f}€\n"
        f"🛒 **Buyer:** {buyer:.2f}€"
    )
    
    await ctx.send(respuesta)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Carga el token desde la configuración segura de Render
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
