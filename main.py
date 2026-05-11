import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

TOKEN = os.getenv("TOKEN")

ANTRENMAN_KANAL = 1503342068821655653
PEN_KANAL = 1503342071019470941
ROLE_ID = 1503341767049740369

sayaclar = {}

# ---------------- ANTRENMAN ---------------- #
@bot.command()
async def ant(ctx):

    if ctx.channel.id != ANTRENMAN_KANAL:
        return await ctx.send("Bu komut sadece antrenman kanalında kullanılabilir.")

    user_id = ctx.author.id

    if user_id not in sayaclar:
        sayaclar[user_id] = 0

    sayaclar[user_id] += 1

    if sayaclar[user_id] < 5:
        await ctx.send(f"{ctx.author.mention} antrenman: {sayaclar[user_id]}/5")
    else:
        sayaclar[user_id] = 0
        await ctx.send(
            f"🏁 5/5 antrenman tamamlandı!\n"
            f"<@&{ROLE_ID}> ilgilenecektir."
        )

# ---------------- PENALTI ---------------- #
@bot.command()
async def pen(ctx):

    if ctx.channel.id != PEN_KANAL:
        return await ctx.send("Bu komut sadece penaltı kanalında kullanılabilir.")

    sonuc = random.choice(["gol", "kale"])

    if sonuc == "gol":
        await ctx.send(f"⚽ GOL! {ctx.author.mention} 2m ceza")
    else:
        await ctx.send("🥅 KALE!")

# ---------------- KALECİ ---------------- #
@bot.command()
async def kaleci(ctx):

    if ctx.channel.id != PEN_KANAL:
        return await ctx.send("Bu komut sadece penaltı kanalında kullanılabilir.")

    sonuc = random.choice(["gol", "kaleci"])

    if sonuc == "kaleci":
        await ctx.send(f"🧤 KALECİ KURTARDI! {ctx.author.mention} 2m ceza")
    else:
        await ctx.send("⚽ GOL!")

bot.run(TOKEN)
