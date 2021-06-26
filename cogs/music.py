import discord
import json
import requests
import os
from discord.ext import commands
# import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    # youtube_dl.utils.bug_reports_message = lambda: ''
    # ytdl_format_options = {
    #     'format': 'bestaudio/best',
    #     'restrictfilenames': True,
    #     'noplaylist': True,
    #     'nocheckcertificate': True,
    #     'ignoreerrors': False,
    #     'logtostderr': False,
    #     'quiet': True,
    #     'no_warnings': True,
    #     'default_search': 'auto',
    #     'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
    # }

    # ffmpeg_options = {
    #     'options': '-vn'
    # }

    # ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

    # @commands.command(pass_context=True)
    # async def bruh(self, ctx):
    #     channel = ctx.author.voice.channel
    #     if not channel:
    #             await ctx.send("You are not in any voice channel")
    #     else:
    #             await channel.connect()
    #     player = await channel.create_ytdl_player(r'https://youtu.be/2ZIpFytCSVc')
    #     player.start()

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send("{} is not connected to a voice channel.".format(ctx.author.name))
            return
        else:
            channel = ctx.author.voice.channel
        await channel.connect()

    # @commands.command(pass_context = True, help='Plays the YouTube url provided', aliases=['p', 'pl'])
    # async def play(self, ctx, url):
    #     server = ctx.message.guild
    #     voice_channel = server.voice_client

    #     async with ctx.typing():
    #         filename = await YTDLSource.from_url(url, loop=bot.loop)
    #         voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
    #     await ctx.send('**Now playing:** {}'.format(filename))
    #     if not voice.is_connected():
    #         await ctx.author.voice.channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))