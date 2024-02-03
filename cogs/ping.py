import disnake
from disnake.ext import commands
import json
from colorama import Fore, Style

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Ping{yellow} is loaded...{reset}")  

    @commands.slash_command(name="ping",description="Показывает пинг.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"`{round(self.bot.latency*1000)}`ms", ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
