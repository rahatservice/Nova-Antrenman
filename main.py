import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

# Kanal ID'leri
ANTRENMAN_KANAL = 1503342068821655653
PEN_KANAL = 1503342071019470941

# Sayaç sistemi
sayaclar = {}

# ---------------- ANTRENMAN SAYACI ---------------- #

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    if message.channel.id == ANTRENMAN_KANAL:

        user_id = message.author.id

        if user_id not in sayaclar:
            sayaclar[user_id] = 0

        sayaclar[user_id] += 1

        if sayaclar[user_id] < 5:

            await message.channel.send(
                f"{message.author.mention} antrenman: {sayaclar[user_id]}/5"
            )

        else:

            await message.channel.send(
                f".dver {message.author.mention} 3m ant"
            )

            sayaclar[user_id] = 0

    await bot.process_commands(message)

# ---------------- PENALTI ---------------- #

@bot.command()
async def pen(ctx):

    if ctx.channel.id != PEN_KANAL:
        kanal = bot.get_channel(PEN_KANAL)
        return await ctx.send(
            f"Bu komut sadece {kanal.mention} kanalında kullanılabilir."
        )

    sonuc = random.choice(["gol", "kale"])

    if sonuc == "gol":
        await ctx.send("⚽ GOL!")
        await ctx.send(f".dver {ctx.author.mention} 2m")

    else:
        await ctx.send("🥅 KALE!")

# ---------------- KALECİ ---------------- #

@bot.command()
async def kaleci(ctx):

    if ctx.channel.id != PEN_KANAL:
        kanal = bot.get_channel(PEN_KANAL)
        return await ctx.send(
            f"Bu komut sadece {kanal.mention} kanalında kullanılabilir."
        )

    sonuc = random.choice(["gol", "kaleci"])

    if sonuc == "kaleci":
        await ctx.send("🧤 KALECİ KURTARDI!")
        await ctx.send(f".dver {ctx.author.mention} 2m")

    else:
        await ctx.send("⚽ GOL!")

bot.run("TOKEN")
