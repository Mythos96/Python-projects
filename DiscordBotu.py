import os
import discord
import time
from bilgi import *
from ayarlar import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

    activity = discord.Game("!help")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def merhaba(ctx):
    await ctx.send('Selam')

@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(f"{left} + {right} = {left + right}")

@bot.command()
async def şifre(ctx):   
    user = ctx.author
    def sifre_olusturucu():
        karakterler = [".","}","{","é",",",";","^",":","~","'","_","]","[","(",")","+","-","/","*","!","&","$","#","?","=","@","<",">","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
        sifre = ""
        for i in range(8):
            sifre += random.choice(karakterler)
        return sifre
    await user.send(f"Şifreniz: {sifre_olusturucu()}")
    await ctx.send(f"{user.mention} Şifreniz DM ile göderildi!")

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def ranmoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 594238347719737354:
        await ctx.send("{Logging off}")
        await bot.close()
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok!")

@bot.command()
async def ping(ctx):
    if ctx.author.id == 594238347719737354:
        latency = round(bot.latency * 1000)
        await ctx.send(f"pong! {latency}ms")
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok!")

@bot.command()
async def market_tavsiyesi(ctx):
    day = time.strftime("%A")
    if day == "Sunday":
        await ctx.send("Market alışcerişinden sonra plastik torba kullanmak yerine alışveriş için aldığın bir çantaya ürünlerini koyarak çevreye yardım edebilirsin")
    else:
        await ctx.send("İyi günler")
    
@bot.command()
async def ayrisma(ctx):
    await ctx.send("Plastik doğada tam 450 yılda çözünür!\nBebek bezlerinin doğada ayrışması için ise tam 550 yıl gerekir")

@bot.command()
async def help(ctx):
    await ctx.send("Myth Bot Komutları:\n- !merhaba\n- !bye\n- !şifre\n- !coin\n- !ranmoji \n- !add\n\nYetkili komutları:\n- !shutdown\n- !ping")



bot.run(token)
