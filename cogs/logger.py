import disnake
from disnake.ext import commands
import json
import os
from colorama import Fore,Style

magenta = Fore.MAGENTA
blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

current_directory = os.path.dirname(os.path.abspath(__file__))

class logger(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Logger{yellow} is loaded...{reset}")

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        json_path = f'{current_directory[:-4]}config/{message.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        print(message)
        

def setup(bot):
    bot.add_cog(logger(bot))