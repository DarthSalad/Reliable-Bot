import discord
import json
import requests
import os
import youtube_dl
# import lavalink
from discord.ext import commands
from discord import utils, Embed

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
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect l -reconnect_streamed l-reconnect_delay_max 5',
            'options': '-vn' 
        }
        YDL_OPTIONS = {'format': "bestaudio"}
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            ctx.voice_client.play(source)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))