import discord
import json
import requests
import os
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True)
    async def bruh(self, ctx):
        channel = ctx.author.voice.channel
        if not channel:
                await ctx.send("You are not in any voice channel")
        else:
                await channel.connect()
        player = await channel.create_ytdl_player(r'https://youtu.be/2ZIpFytCSVc')
        player.start()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))