import discord
from discord.ext import commands
import secrets
import random

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Not passing in guild_ids creates a global slash command.
    async def hi(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hi, this is a global slash command from a cog!")

    @commands.slash_command()
    async def password(self, ctx: discord.ApplicationContext, nbytes: int = 18):
        if nbytes not in range(3, 32):
            return await ctx.send("Error!")
        await ctx.send(f"**I'll send you your random Password in a Second {ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your Password:** 🎁\n{secrets.token_urlsafe(nbytes)}")   

    @password.error
    async def password_error(self, ctx: discord.ApplicationContext):
        await ctx.send("Oops something went wrong, Do you have PM's on private?")

    @commands.slash_command()
    async def avatar(self, ctx: discord.ApplicationContext, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        # Findet avatar_url_as nicht mehr
        await ctx.send(f"Avatar of User **{user.name}:**\n{user.avatar_url_as(size=1024)}")

    @commands.slash_command()
    async def casino(self, ctx: discord.ApplicationContext):

        # I think we need some juice fruits for this to make it look good, so here we go: Strawberry, Melons, Citrons, Cherrys.... YUMMY
        # You can use wahtever Emojies you want to use for this.
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        # This is like THE JACKPOT. THE HIGHSCORE. THE BEST. Pretty Rare to hit this, but possible. 
        if (a == b == c):
            embed1 = discord.Embed(colour=discord.Colour.dark_gold())
            embed1.set_footer(text=f"Played by: {ctx.author}")
            embed1.add_field(name=f"{slotmachine}", value="***WOW***, you just hit 3x the same Symbol! 🎉", inline=False)
            embed1.add_field(name="You won 800 XP", value="🎉 🎉 🎉", inline=False)

            await ctx.send(embed=embed1)

        # This is still good, but not as good as the one above.
        # You just need to hit 2 same Symbols and you got it.
        elif (a == b) or (a == c) or (b == c):

            embed2 = discord.Embed(colour=discord.Colour.dark_gold())
            embed2.set_footer(text=f"Played by: {ctx.author}")
            embed2.add_field(name=f"{slotmachine}", value="***WOW***, you achieved 200XP! 🎉", inline=False)
            await ctx.send(embed=embed2)

        # This is the badest one. you actually lost it. But hey, we'll give you 20XP Still since we're crying with you :((((
        else:

            embed3 = discord.Embed(colour=discord.Colour.dark_gold())
            embed3.set_footer(text=f"Played by: {ctx.author}")
            embed3.add_field(name=f"{slotmachine}", value="Not this time! 😢 Maybe you get it with the next try", inline=False)
            await ctx.send(embed=embed3)

def setup(bot):
    bot.add_cog(misc(bot))
