import discord
from discord.ext import commands
import datetime

import json
from urllib.request import Request, urlopen

url_cow = "https://api.pancakeswap.info/api/v2/tokens/0x8b6fa031c7d2e60fbfe4e663ec1b8f37df1ba483"
url_milk = "https://api.pancakeswap.info/api/v2/tokens/0xe5bd6c5b1c2df8f499847a545838c09e45f4a262"

bot = commands.Bot(command_prefix='!', description="This is the price bot for Cash Cow Protocol, best project in the DeFi world!", help_command=None)


#Price-message:
@bot.command()
async def price(ctx):
    #j_cow : json with cow data-------------------------------------------------
    req = Request(url_cow, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    j_cow = json.loads(webpage)
    #---------------------------------------------------------------------------

    #j_milk : json with milk data-----------------------------------------------
    req = Request(url_milk, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    j_milk = json.loads(webpage)
    #---------------------------------------------------------------------------

    embed = discord.Embed()

    embed.description ="""
    **$COW** 🐮

    Price: $ {:f}
    Price in BNB: {:f}

    💱 [Buy $COW](https://pancakeswap.finance/swap?outputCurrency=0x8b6fa031c7d2e60fbfe4e663ec1b8f37df1ba483)
    📈 [Poocoin chart](https://poocoin.app/tokens/0x8b6fa031c7d2e60fbfe4e663ec1b8f37df1ba483)

    **$MILK** 🥛

    Price: $ {:f}
    Price in BNB: {:f}

    💱 [Buy $MILK](https://pancakeswap.finance/swap?outputCurrency=0xe5bd6c5b1c2df8f499847a545838c09e45f4a262)
    📈 [Poocoin chart](https://poocoin.app/tokens/0xe5bd6c5b1c2df8f499847a545838c09e45f4a262)
    """.format(round(float(j_cow["data"]["price"]), 6), round(float(j_cow["data"]["price_BNB"]), 6),
        round(float(j_milk["data"]["price"]),6),round(float(j_milk["data"]["price_BNB"]),6))

    await ctx.send(embed=embed)

@bot.command()
async  def  help(ctx):
    des = """
    Commands for CashCowProtocol Price Bot:\n

     **Prefix**:       !\n

     **!price**:       Get information about Cash Cow Protocol tokens price\n


    """
    embed = discord.Embed(title="I'm the price bot for Cash Cow Protocol, best project in the DeFi world!",url="##########",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.blue())
    embed.set_footer(text="Made by v0st0k1")


    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print('The CashCowProtocol Price Bot is ready!')



bot.run('##########')
