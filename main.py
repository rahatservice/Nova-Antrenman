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

@bot.command()
async def title(ctx, *, mesaj=None):

    # ---------------- ANTRENMAN ---------------- #
    if ctx.channel.id == ANTRENMAN_KANAL:

        user_id = ctx.author.id

        if user_id not in sayaclar:
            sayaclar[user_id] = 0

        sayaclar[user_id] += 1

        if sayaclar[user_id] < 5:
            await ctx.send(f"{ctx.author.mention} antrenman: {sayaclar[user_id]}/5")
        else:
            sayaclar[user_id] = 0

            role_mention = f"<@&{ROLE_ID}>"

            await ctx.send(
                f"🏁 5/5 antrenman tamamlandı!\n"
                f"{role_mention} ilgilenecektir."
            )

        return

    # ---------------- PEN / KALE ---------------- #
    if ctx.channel.id == PEN_KANAL:

        if mesaj is None:
            await ctx.send("Kullanım: .title pen veya .title kaleci")
            return

        mesaj = mesaj.lower()

        if mesaj == "pen":
            sonuc = random.choice(["gol", "kale"])

            if sonuc == "gol":
                await ctx.send(f"⚽ GOL! {ctx.author.mention} 2m ceza")
            else:
                await ctx.send("🥅 KALE!")

        elif mesaj == "kaleci":
            sonuc = random.choice(["gol", "kaleci"])

            if sonuc == "kaleci":
                await ctx.send(f"🧤 KALECİ KURTARDI! {ctx.author.mention} 2m ceza")
            else:
                await ctx.send("⚽ GOL!")

        else:
            await ctx.send("Sadece: pen veya kaleci yazabilirsin")

    else:
        await ctx.send("Bu komut sadece belirlenen kanalda kullanılabilir.")

bot.run(TOKEN)
