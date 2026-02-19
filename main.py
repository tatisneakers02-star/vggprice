import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def vgg(ctx, region: str, precio_listado: float):
    region = region.lower()
    
    # --- PARÁMETROS VIAGOGO OFICIALES (según tu tabla) ---
    PAYOUT_MULTIPLIER = 0.879
    BUYER_MULTIPLIER = 1.20

    payout = precio_listado * PAYOUT_MULTIPLIER
    buyer_price = precio_listado * BUYER_MULTIPLIER

    # --- Configuración visual por Región (Emojis y Colores) ---
    if region in ["com", "es"]:
        titulo_embed = "🇪🇸 VGG ESPAÑA / .COM CALCULATOR"
        color_embed = 0xFFC300  # Amarillo Dorado para resaltar
        region_icon = "🇪🇸"
    elif region == "uk":
        titulo_embed = "🇬🇧 VGG UNITED KINGDOM CALCULATOR"
        color_embed = 0x3498DB  # Azul Británico
        region_icon = "🇬🇧"
    else:
        await ctx.send("⚠️ **Error:** Región no reconocida. Usa `!vgg es 100` o `!vgg uk 100`")
        return

    # --- Construcción del EMBED (El recuadro bonito) ---
    embed = discord.Embed(
        title=f"✨ {titulo_embed} ✨",
        description=f"📈 Precio que tú **listas** en Viagogo: **{precio_listado:.2f}€**\n\n",
        color=color_embed
    )
    
    # 💰 PAYOUT - Destacado con emoji y color amarillo vibrante
    embed.add_field(
        name=f"💰 TU GANANCIA NETA (PAYOUT)", 
        value=f"```fix\n{payout:.2f}€\n```", 
        inline=False
    )
    
    # 🛒 PRECIO COMPRADOR - Con emoji de carrito y color más sutil
    embed.add_field(
        name=f"🛒 PRECIO QUE PAGA EL COMPRADOR", 
        value=f"```yaml\n{buyer_price:.2f}€\n```", 
        inline=False
    )

    # Pequeños detalles para la profesionalidad
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2091/2091665.png") # Icono de billetes
    embed.set_footer(
        text=f"{region_icon} Cálculos basados en tus parámetros ({PAYOUT_MULTIPLIER} / {BUYER_MULTIPLIER})", 
        icon_url=ctx.author.avatar.url if ctx.author.avatar else None
    )

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'✅ VGG Bot v2.0 Ultra Pro Online ({bot.user})')

token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
