import disnake
from disnake.ext import commands
import json
from colorama import Fore, Style
import asyncio
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

magenta = Fore.MAGENTA
blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class prch(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}prch {yellow}is loaded...{reset}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        json_path = f'{current_directory[:-4]}config/{member.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        if after.channel and after.channel.id == config['PRIVATE_CHENNEL_CR']:
            overwrites = {
                member: disnake.PermissionOverwrite(
                    manage_permissions=True,
                    manage_channels=True,
                    mute_members=True,
                    deafen_members=True,
                    move_members=True
                ),
                member.guild.default_role: disnake.PermissionOverwrite(
                    connect=False
                )
            }

            new_channel = await after.channel.category.create_voice_channel(f"{member.display_name}'s Private Channel", overwrites=overwrites)
            await member.edit(voice_channel=new_channel)

            async def check_empty(channel):
                while len(channel.voice_states) >= 1:
                    await asyncio.sleep(1)
                await channel.delete()

            self.bot.loop.create_task(check_empty(new_channel))

def setup(bot):
    bot.add_cog(prch(bot))
