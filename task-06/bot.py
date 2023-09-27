import discord
from discord.ext import commands
import scrapper

TOKEN = 'MTE1MjIzMTIyMzQzMTc5NDgxMg.GZR4mC.pPm9_MlhdX8LN8MFJXx2M37Oz_kz3cmr5JnN1Q'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", help_command=None, intents=intents)
csv_file = 'livescores.csv'

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def no_live(ctx):
    result = scrapper.no_live()
    await ctx.send(result)

@bot.command()
async def livescore(ctx):
    team_1 = scrapper.team_1
    over_1 = scrapper.over_1
    score_1 = scrapper.score_1
    team_2 = scrapper.team_2
    over_2 = scrapper.over_2
    score_2 = scrapper.score_2
    live_status = scrapper.live_status
    current_time = scrapper.current_time
    result = scrapper.score(team_1, over_1, score_1, team_2, over_2, score_2, live_status, current_time)
    r = scrapper.add_data()
    await ctx.send(result)

@bot.command()
async def help(ctx):
    msg = ('''
           Welcome to cricket bot!
My Commands:
/livescore - To get live updates
/generate - To get csv file with livscores stored till now''')
    await ctx.send(msg)

@bot.command()
async def generate(ctx):
    with open(csv_file, "rb") as file:
        csv = discord.File(file, filename=csv_file)
        await ctx.send(file=csv)     

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command. \nUse /help for a list of available commands.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Unknown argument. \nUse /help for a list of available commands.")

bot.run(TOKEN)