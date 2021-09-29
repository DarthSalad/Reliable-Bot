import discord
import requests
import os
import lavalink
import math
from discord.ext import commands
from discord import utils, Embed

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        
        if not hasattr(bot, 'lavalink'):
            self.bot.music = lavalink.Client(self.bot.user.id)
            self.bot.music.add_node('localhost', 8080, 'pass', 'na', 'music-node')
            self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
            
        self.bot.music.add_event_hook(self.track_hook)
    
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)
      
    async def connect_to(self, guild_id: int, channel_id: str):
        rn = self.bot._connection._get_websocket(guild_id)
        await rn.voice_state(str(guild_id), channel_id)

    @commands.command(pass_context=True)
    async def join(self, ctx):
        # print('test successful')
        if not ctx.author.voice:
            await ctx.send("{} is not connected to a voice channel.".format(ctx.author.name))
            return
        else:
            vc = ctx.author.voice.channel
        player = self.bot.music.player_manager.create(ctx.guild.id, endpoint = str(ctx.guild.region))
        if not player.is_connected:
            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(vc.id))

    @commands.command(pass_context=True, aliases=['stop', 'disconnect'])
    async def leave(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel != int(player.channel.id)):
            return await ctx.send("You are not in my voice channel.")

        player.queue.clear()
        await player.stop()
        await self.connect_to(ctx.guild.id, None)

    @commands.command(pass_context=True, help="Enter the name of the song/video(YouTube)")
    async def play(self, ctx, *, query):
        await ctx.invoke(self.bot.get_command('join'))
        def check(m):
            return m.author.id == ctx.author.id
        player = self.bot.music.player_manager.get(ctx.guild.id)
        # await ctx.channel.send("yt(for YouTube) or sc(for SoundCloud)")
        # platform = await self.bot.wait_for('message', check = check)
        # query = f'{platform}search:{query}'
        query = f'ytsearch:{query}'
        results = await player.node.get_tracks(query)
        # print(results) 
        tracks = results['tracks'][0:5]
        i = 0
        query_result = ''
        for track in tracks:
            i = i+1
            query_result = query_result + f'{i}:  **{track["info"]["title"]}** - {track["info"]["uri"]}\n\n'
        embed = Embed(color=discord.Color.red())
        embed.description = query_result
        await ctx.channel.send(embed=embed)

        response = await self.bot.wait_for('message', check=check)
        track = tracks[int(response.content)-1]

        player.add(requester = ctx.author.id, track = track)
        if not player.is_playing:
            await player.play()
    
    @commands.command(help="Shows the queue", aliases=["q"])
    async def queue(self, ctx, page: int = 1):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        queue = player.queue
        items_per_page = 10
        pages = math.ceil(len(queue)/items_per_page)
        start = (page-1)*items_per_page
        end = start + items_per_page
        description = f"Currently Playing: **[{player.current.title}]** **({player.current.uri})**\n"
        if len(queue):
            for index, track in enumerate(queue[start:end], start = 1):
                requester = ctx.guild.get_member(track.requester)
                description += f"{index}. **{track.title}** ({track.uri})\n" #(Requested by {requester.mention})

        elif player.current == None:
            description = "Queue is empty."

        embed=discord.Embed(
            title = "Current Playlist",
            color=discord.Color.red(),
            description=description
        )
        # embed.set_thumbnail(url="%s/0.jpg"%player.current.uri.replace(
        #   'https://www.youtube.com/watch?v=', 
        #   'http://img.youtube.com/vi/'))
        embed.set_footer(text=f'{page}/{pages}\n')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Music(bot))

#pause, resume, next, skip, remove, reorder, see playlist, private playlists(MySQL)