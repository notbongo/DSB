import disnake
from disnake.ext import commands
from PIL import Image, ImageFont, ImageDraw
from colorama import Fore, Style
import requests
import io
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

json_path_pics = f'{current_directory[:-4]}pics/'

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class tester(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Annoc{yellow} is loaded...{reset}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        json_path = f'{current_directory[:-4]}config/{member.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        width, height = 612, 168

        guild = member.guild

        role = guild.get_role(config['JOIN_ROLE'])
        await member.add_roles(role)

        background = Image.open(f'{json_path_pics}join_card_main.png')
        background = background.resize((width, height))

        url = str(member.avatar.url)[:-10]

        response = requests.get(url, stream=True)

        mask = Image.new('L', (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)

        avatar = Image.open(io.BytesIO(response.content))
        avatar = avatar.convert('RGBA')
        avatar = avatar.resize((100, 100), Image.BILINEAR)

        avatar.putalpha(mask)

        background.paste(avatar, (20, 20), avatar)

        draw = ImageDraw.Draw(background)
        name = member.name

        member_count = len(member.guild.members)

        headline_font = ImageFont.truetype('arial.ttf', size=20)
        undertext_font = ImageFont.truetype('arial.ttf', size=20)

        draw.text((135, 33), f'Добро пожаловать, {name}!', font=headline_font)
        draw.text((135, 60), f'ID: {member.id}', font=undertext_font)
        draw.text((135, 83), f'member #{member_count}', font=undertext_font)

        background.save(f'{json_path_pics}join_card.png')

        channel = guild.get_channel(config['WELCOME_CHANNEL'])

        await channel.send(file=disnake.File("join_card.png"))

def setup(bot):
    bot.add_cog(tester(bot))
