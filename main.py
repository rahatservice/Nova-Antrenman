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
        return await ctx.send("❌ Bu komut sadece antrenman kanalında kullanılabilir.")

    user_id = ctx.author.id
    if user_id not in sayaclar:
        sayaclar[user_id] = 0

    sayaclar[user_id] += 1

    if sayaclar[user_id] < 5:
        embed = discord.Embed(
            title="🏃 Antrenman Devam Ediyor",
            description=f"{ctx.author.mention}, disiplin başarıyı getirir!\n\n**İlerleme:** `{sayaclar[user_id]}/5`",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    else:
        sayaclar[user_id] = 0
        embed = discord.Embed(
            title="✅ Antrenman Tamamlandı!",
            description=f"Tebrikler {ctx.author.mention}, 5 set antrenmanı başarıyla bitirdin.\n\n🔔 <@&{ROLE_ID}>, bir sporcu eğitimini tamamladı!",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

# ---------------- PENALTI ---------------- #
@bot.command()
async def pen(ctx):
    if ctx.channel.id != PEN_KANAL:
        return await ctx.send("❌ Bu komut sadece penaltı kanalında kullanılabilir.")

    sonuc = random.choice(["gol", "kale"])
    
    if sonuc == "gol":
        embed = discord.Embed(
            title="⚽ MUHTEŞEM GOL!",
            description=f"{ctx.author.mention} topu ağlara gönderdi!\n\n💰 **Ödül:** 2m Ceza",
            color=discord.Color.gold()
        )
    else:
        embed = discord.Embed(
            title="🏟️ DIŞARIYA!",
            description=f"{ctx.author.mention} topu kaleye sokamadı, şansını tekrar dene!",
            color=discord.Color.red()
        )
    await ctx.send(embed=embed)

# ---------------- KALECİ ---------------- #
@bot.command()
async def kaleci(ctx):
    if ctx.channel.id != PEN_KANAL:
        return await ctx.send("❌ Bu komut sadece penaltı kanalında kullanılabilir.")

    sonuc = random.choice(["gol", "kaleci"])

    if sonuc == "kaleci":
        embed = discord.Embed(
            title="🧤 DEVLEŞEN KALECİ!",
            description=f"{ctx.author.mention} kalesinde duvar ördü!\n\n💰 **Ödül:** 2m Ceza",
            color=discord.Color.purple()
        )
    else:
        embed = discord.Embed(
            title="⚽ TOP AĞLARDA!",
            description=f"{ctx.author.mention} bu sefer topu çıkaramadı...",
            color=discord.Color.orange()
        )
    await ctx.send(embed=embed)

bot.run(TOKEN)
