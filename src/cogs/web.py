import discord
import json
import requests
import os
import spotipy
import lyricsgenius as lg
from spotipy.oauth2 import SpotifyOAuth
from discord.ext import commands
from googlesearch import search
from dotenv import load_dotenv

key = os.getenv('key')
gen = os.getenv('gen')
sp_id = os.getenv('SPOTIFY_CLIENT_ID')
sp_key = os.getenv('SPOTIFY_CLIENT_SECRET')
uri = os.getenv('SPOTIFY_REDIRECT_URI')
class Web(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command(help="Type the number of results after command")
    async def gsearch(self, ctx, n :int):
        await ctx.send("Type the search query")
        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await self.bot.wait_for("message", check=check)
        return_value=search(str(msg.content), tld='co.in', num=n, stop=n, pause=1)
        for j in return_value:
                await ctx.send(j)

    @commands.command(help='Type the YT search query and number of results desired')
    async def yt(self, ctx, *, info):
        query = " ".join(info.split(" ")[0:-1]).replace(" ","+")
        num = int(info.split(" ")[-1])
        req = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={num}&q={query}&key={key}"
        response = requests.get(req)
        for item in response.json()["items"]:
            if item["id"]["kind"] == "youtube#playlist":
                await ctx.send("https://www.youtube.com/watch?v=temp&list="+item["id"]["playlistId"])
            elif item["id"]["kind"] == "youtube#video":
                await ctx.send("https://www.youtube.com/watch?v="+item["id"]["videoId"])

    @commands.command(help="Input the song and artist's name to display the lyrics")
    async def genius(self, ctx, song_name, artist_name):
        g = lg.Genius(gen)
        g.excluded_terms = ["(Remix)", "(Live)"]
        song = g.search_song(song_name, artist_name)
        await ctx.send(song.lyrics)

    @commands.command(help="Type the name of the song")
    async def spotify(self, ctx, *, args):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=sp_id, 
                client_secret=sp_key, 
                redirect_uri=uri
            )
        )
        results = sp.search(q='track: ' + args, type='track')
        items = results['tracks']['items']
        album_id = items[0]
        await ctx.send(album_id['external_urls']['spotify'])


def setup(bot):
    bot.add_cog(Web(bot))