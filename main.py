import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=intents)

intents = discord.Intents.default()
intents.message_content = True

meme_dict = {"Usa i mezzi pubblici o i mezzi ecologici"
             "Evita gli imballaggi, compra sfuso"
             "No al sacchetto di plastica"
             "Salva gli alberi, non sprecare carta"
             "Pianta un albero"
             "Chiudi l'acqua"
             "Abbbassa il riscaldamento"
             "Spegni la luce e gli apparecchi in stand by"
             ""}

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

    bot.run("MTE3Nzk5OTkwNjgxNjkxNzY0NQ.G5E_XO.FAta2kQNcC2SB8m25oK70E-tj54NZooBFt2mVc")

