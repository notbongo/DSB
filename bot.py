import disnake
from disnake.ext import commands
from colorama import Fore, Style
from os import listdir
from disnake import Button, ButtonStyle
import json
import os



current_directory = os.path.dirname(os.path.abspath(__file__))

bot = commands.Bot(command_prefix="v!", help_command=None, intents=disnake.Intents.all())

magenta = Fore.MAGENTA
blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

configpar = {
      "MUTED_ROLE": None,
      "NMChennel": None,
      "ADMIN_ROLE": None,
      "JOIN_ROLE": None,
      "WELCOME_CHANNEL": None,
      "TicketlogsChannel": None,
      "TICKET_CATEGORY": None,
      "PRIVATE_CHENNEL_CR": None,
      "TICKET_COUNT": 0,
      "ADMIN_LIST" : None,
      "ChannelLog" : None,
      "Authrole" : None,
      "role1" : None,
      "role2" : None,
      "role3" : None,
      "role4" : None,
      "role5" : None,
      "role6" : None,
      "role7" : None,
      "role8" : None,
      "role9" : None,
      "role10" : None
}


@bot.event
async def on_ready():
      print(f"{green}Bot{yellow} is ready!{reset}\n{yellow}Bot: {magenta}{bot.user.name}#{bot.user.discriminator}{reset}, {yellow}Bot id: {magenta}{bot.user.id}{reset}")
      print(f"{blue}{cogcount} cogs{yellow} is loaded...{reset}\n")

      for guild in bot.guilds:
            json_path = f'{current_directory}\\config\\{guild.id}.json'
            if os.path.exists(json_path):
                  print(f"Конфиг для сервера {yellow}{guild}{reset} # {yellow}{guild.id}{reset} существует {yellow}{json_path}{reset}.\n")
            else:
                  print(f"Конфиг для сервера {yellow}{guild}{reset} # {yellow}{guild.id}{reset} не существует.\nСоздаю конфиг.")
                  with open(json_path, 'w') as json_file:
                        json.dump(configpar, json_file, indent=4)
                  print(f"Создал конфиг: {json_path}, {yellow}{guild}{reset} # {yellow}{guild.id}{reset}\n")

@bot.event
async def on_guild_join(guild):
    for guild in bot.guilds:
        json_path = f'{current_directory}/config/{guild.id}.json'
        if os.path.exists(json_path):
            print(f"Конфиг для сервера {yellow}{guild}{reset}({yellow}{guild.id}{reset}) существует {yellow}{json_path}{reset}.\n")
        else:
            print(f"Конфиг для сервера {yellow}{guild}{reset} # {yellow}{guild.id}{reset} не существует.\nСоздаю конфиг.")
            with open(json_path, 'w') as json_file:
                json.dump(configpar, json_file, indent=4)
            print(f"Создал конфиг: {yellow}{json_path}{reset}, {yellow}{guild}{reset}({yellow}{guild.id}{reset})\n\n")

      
                  

cogcount = 0
for filename in listdir("./cogs"):
      if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            cogcount = cogcount + 1
            


@bot.slash_command(name="reloadcog",description="Перезагружает коги.")
async def reloadсog(ctx):
      json_path = f'{current_directory}/config/{ctx.guild.id}.json'
      with open(json_path) as config_file:
            config = json.load(config_file)
      if ctx.author.guild_permissions.administrator:
            for filename in listdir("./cogs"):
                  if filename.endswith(".py"):
                        bot.unload_extension(f"cogs.{filename[:-3]}")
                        bot.load_extension(f"cogs.{filename[:-3]}")

            print(f"{green}Cogs reloaded...{reset}")
            await ctx.send("Коги перезагружены",ephemeral=True)          
      else:
            await ctx.send("Недостаточно прав.", ephemeral=True)

bot.run('MTE0MDAzNTMxNDMzNzk3MjI4NA.GW2VEp.VfAdQFAQAWCDlrAIJMbSbKf22zfXzzpFkogSE4')
