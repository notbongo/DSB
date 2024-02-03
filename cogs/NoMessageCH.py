import disnake
from disnake.ext import commands
import json
from colorama import Fore, Style
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

magenta = Fore.MAGENTA
blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL


class NMC(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}NMC {yellow}is loaded...{reset}")

    @commands.Cog.listener()
    async def on_message(self, message):
        json_path = f'{current_directory[:-4]}config/{message.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        channel_id = config['NMChennel']

        if message.author == self.bot.user:
            return

        if message.channel.id == channel_id:
            chelname = message.author.display_name

            if any(attachment.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm','mp3')) for attachment in message.attachments) or any(word in message.content for word in ('http://', 'https://')):
                thread_name = f"Ветка {chelname}"
                await message.create_thread(name=thread_name)
            else:
                await message.delete()

        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(NMC(bot))
