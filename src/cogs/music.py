import discord
import json
import requests
import os
import lavalink
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send("{} is not connected to a voice channel.".format(ctx.author.name))
            return
        else:
            channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))