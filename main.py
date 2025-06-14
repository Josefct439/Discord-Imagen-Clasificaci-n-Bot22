import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("Archivo guardado")
            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                if class_name == "Palomas":
                    await ctx.send("Esto es una paloma y las palomas suelen comer semillas")
                elif class_name == "Gorriones":
                    await ctx.send("Esto es un gorrion y le gusta comer lombrices")
            except:
                await ctx.send("Error, puede que no se haya logrado la clasificación")
                await ctx.send("Recomiendo usar imagenes en formato JPG, JPEG y PNG")
    else:
        await ctx.send("No has subido una imagen")


bot.run("TOKEN")


