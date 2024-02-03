from disnake.ext import commands
from disnake.ext import tasks
from datetime import datetime, timedelta
from PIL import Image, ImageFont, ImageDraw
import io
from colorama import Fore,Style
import requests
import os
import asyncio
import disnake
import json

current_directory = os.path.dirname(os.path.abspath(__file__))

json_path_pics = f'{current_directory[:-4]}pics/'

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL
magenta= Fore.MAGENTA


class banner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        #self.my_task.start()
        #self.my_task_1.start()
        #self.my_task_2.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Banner {yellow}is ready{reset}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            if member.guild.id == 1069109857032093698:
                if before.channel != after.channel:
                    guild = member.guild
                    voice_channels = [channel for channel in guild.voice_channels if len(channel.members) > 0 and channel.guild.id == 1069109857032093698]

                    total_users = sum(len(channel.members) for channel in voice_channels)

                    background = Image.open(f'{json_path_pics}savagebanner.png')
                    draw = ImageDraw.Draw(background)

                    total_users_text = ImageFont.truetype('arial.ttf', size=90)

                    draw.text((755, 360), f'{total_users}', font=total_users_text)

                    background.save(f'{json_path_pics}bannersv.png')
        except Exception as e:
            print(f"Ошибка в banneronline|on_voice_state_update| {e}")




    @tasks.loop(seconds=10)
    async def my_task(self):
        try:
            b = 0
            target_guild_id = 1069109857032093698

            background = Image.open(f'{json_path_pics}bannersv.png')
            draw = ImageDraw.Draw(background)

            user_message_counts = {}

            for guild in self.bot.guilds:
                if guild.id == target_guild_id:
                    b = 1
                    for text_channel in guild.text_channels:
                        print(text_channel)
                        async for message in text_channel.history(limit=1):
                            if message.author.bot:
                                continue
                            user_message_counts[message.author.id] = user_message_counts.get(message.author.id, 0) + 1
            
            if b == 0:
                print(f"Сервер с id {target_guild_id} не найден, или возможна другая ошибки")
                return

            if not user_message_counts:
                print(f"Сообщений не найдено.")
            else:
                print(user_message_counts)
                most_active_user_id = max(user_message_counts, key=user_message_counts.get)
                most_active_user = await self.bot.fetch_user(most_active_user_id)

                user = most_active_user.name

                membername = ImageFont.truetype('arial.ttf', size=42)

                if len(user) > 7:
                    user = f"{most_active_user.name[:-3]}..."


                draw.text((385, 440), user, font=membername)

                url = str(most_active_user.avatar.url)[:-10]

                response = requests.get(url, stream=True)

                mask = Image.new('L', (100, 100), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 100, 100), fill=255)

                avatar = Image.open(io.BytesIO(response.content))
                avatar = avatar.convert('RGBA')
                avatar = avatar.resize((100, 100), Image.BILINEAR)

                avatar.putalpha(mask)

                background.paste(avatar, (415, 350), avatar)

                background.save(f'{json_path_pics}most_active_user_bannersv.png')
        except Exception as e:
            print(f"Ошибка в banneronline|my_task| {e}")


    @tasks.loop(seconds=10)
    async def my_task_1(self):
        try:
            
            target_guild_id = 1069109857032093698

            background = Image.open(f'{json_path_pics}most_active_user_bannersv.png')
            draw = ImageDraw.Draw(background)

            for guild in self.bot.guilds:
                if guild.id == target_guild_id:
                    total_members = guild.member_count

                    online_members = len([member for member in guild.members if member.status != disnake.Status.offline])

                    defulttext = ImageFont.truetype('arial.ttf', size=42)

                    draw.text((155, 340), f'{total_members}', font=defulttext)

                    draw.text((155, 440), f'{online_members}', font=defulttext)

                    background.save(f'{json_path_pics}finishbanner.png')
        except Exception as e:
            print(f"Ошибка в banneronline|my_task_1| {e}")

    @tasks.loop(seconds=10)
    async def my_task_2(self):
        try:
            with open(f'{json_path_pics}finishbanner.png', "rb") as banner_file:
                image_bytes = banner_file.read()

                guild = self.bot.get_guild(1069109857032093698)

                await guild.edit(banner=image_bytes)
        except Exception as e:
            print(f"Ошибка в banneronline|my_task_2| {e}")

                
    @my_task.before_loop
    async def before_my_task(self):
        await self.bot.wait_until_ready()

    @my_task_1.before_loop
    async def before_my_task_1(self):
        await self.bot.wait_until_ready()
        
    @my_task_2.before_loop
    async def before_my_task_2(self):
        await self.bot.wait_until_ready()



def setup(bot):
    bot.add_cog(banner(bot))
