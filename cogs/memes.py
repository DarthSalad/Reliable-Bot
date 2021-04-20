import discord
import json
import requests
import os
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(help="Drake Hotline Bling meme")
    async def drake(self, ctx, arg1, arg2):
        parameters = {
            "template_id": 181913649,
            "username": 'darthsalad',
            "password": os.getenv('pass'),
            'text0': str(arg1),
            'text1': str(arg2),
        }

        response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
        await ctx.send(response.json()['data']['url'])

    @commands.command()
    async def bf(self, ctx, arg1, arg2, arg3):
        parameters = {
            "template_id": 112126428,
            "username": 'darthsalad',
            "password": os.getenv('pass'),
            'boxes[0][text]': str(arg1),
            'boxes[1][text]': str(arg2),
            'boxes[2][text]': str(arg3),
        }
        response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
        await ctx.send(response.json()['data']['url'])

    @commands.command()
    async def changemind(self, ctx, *, arg1):
        parameters = {
            "template_id": 129242436,
            "username": 'darthsalad',
            "password": os.getenv('pass'),
            'boxes[0][text]': str(arg1),
        }

        response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
        await ctx.send(response.json()['data']['url'])

    @commands.command()
    async def pigeon(self, ctx, arg1, arg2, arg3):
        parameters = {
            "template_id": 100777631,
            "username": 'darthsalad',
            "password": os.getenv('pass'),
            'boxes[0][text]': str(arg1),
            'boxes[1][text]': str(arg2),
            'boxes[2][text]': str(arg3),
        }

        response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
        await ctx.send(response.json()['data']['url'])
    
    @commands.command()
    async def trade(self, ctx, arg1, arg2, arg3):
        parameters = {
            "template_id": 313035061,
            "username": 'darthsalad',
            "password": os.getenv('pass'),
            'boxes[0][text]': str(arg1),
            'boxes[1][text]': str(arg2),
            'boxes[2][text]': str(arg3),
        }

        response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
        await ctx.send(response.json()['data']['url'])


def setup(bot):
    bot.add_cog(Meme(bot))

