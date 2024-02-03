import disnake
import asyncio
from disnake.ext import commands,tasks
import json
from colorama import Fore, Style
import os
import datetime
import random

auth_button_1 = disnake.ui.Button(style=disnake.ButtonStyle.success,label="1", custom_id="auth_button_1")
auth_button_2 = disnake.ui.Button(style=disnake.ButtonStyle.success,label="2", custom_id="auth_button_2")
auth_button_3 = disnake.ui.Button(style=disnake.ButtonStyle.success,label="3", custom_id="auth_button_3")
auth_button_4 = disnake.ui.Button(style=disnake.ButtonStyle.success,label="4", custom_id="auth_button_4")
auth_button_5 = disnake.ui.Button(style=disnake.ButtonStyle.success,label="5", custom_id="auth_button_5")


current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class authentication(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}authentication{yellow} is loaded...{reset}")

    @commands.slash_command(name="auth-menu",description="Создание меню аутентификации.")
    async def authmenu(self,ctx):
        if ctx.guild.id == 818710560899465256:
            authembed = disnake.Embed(
                title=f"Добро пожаловать на сервер **{ctx.guild.name}**",
                description=f"> Сервер не ограничивает деятельность администрации.\n> Девиз администрации: https://www.youtube.com/watch?v=oMQfuyliVco\n\n> Распространение переписок из чатов в любом виде на сторонних ресурсах карается баном\n> (Исключение: Администрация)\n\n> Сервер является пророссийским и пропаганда любых ценностей `ОУН` `УПА` `Киевского режима` карается баном.\n\n> Остальные правила будут находиться в канале #rules. Нажми на кнопку 3"
            )
            await ctx.send(embed=authembed,components=[auth_button_1,auth_button_2,auth_button_3,auth_button_4,auth_button_5])
        else:
            await ctx.send("Команда не работает на этом сервере!", ephemeral=True)
        
    @commands.Cog.listener()
    async def on_button_click(self,interaction):
        json_path = f'{current_directory[:-4]}config/{interaction.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)

        if interaction.component.custom_id == "auth_button_1":
            await interaction.response.send_message("Не правильно.", ephemeral=True)
        elif interaction.component.custom_id == "auth_button_2":
            await interaction.response.send_message("Не правильно.", ephemeral=True)
        elif interaction.component.custom_id == "auth_button_3":

            await interaction.author.remove_roles(interaction.guild.get_role(config['JOIN_ROLE']))
            
            await interaction.author.add_roles(interaction.guild.get_role(config['Authrole']))

            await interaction.response.send_message("<a:Applause81:1157865234686541844>", ephemeral=True)
            
        elif interaction.component.custom_id == "auth_button_4":
            await interaction.response.send_message("Не правильно.", ephemeral=True)
        elif interaction.component.custom_id == "auth_button_5":
            await interaction.response.send_message("Не правильно.", ephemeral=True)

def setup(bot):
    bot.add_cog(authentication(bot))