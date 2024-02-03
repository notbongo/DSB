import disnake
from disnake.ext import commands
from colorama import Fore, Style
import json
import os
import random
from disnake import Button, ButtonStyle
import random

current_directory = os.path.dirname(os.path.abspath(__file__))

rolemenu = disnake.ui.Button(style=disnake.ButtonStyle.green,label="Открыть меню.", custom_id="rolemenu")

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class rolesmenu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}rolesmenu{yellow} is loaded...{reset}")

    @commands.slash_command(name="role-menu",description="Меню выдачи ролей.")
    async def rolemenu(self,ctx):
        if ctx.author.guild_permissions.administrator:
            embed = disnake.Embed(
                description="Нажми на кнопку чтобы получить роль."
            )
            channel = ctx.channel

            await channel.send(embed=embed,components=[rolemenu])

            await ctx.send("done", ephemeral=True)
        else:
            await ctx.send("Недостаточно прав.", ephemeral = True)

    @commands.Cog.listener()
    async def on_button_click(self,interaction):
            json_path = f'{current_directory[:-4]}config/{interaction.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            customid = interaction.component.custom_id

            if customid == "rolemenu":
                await self.rolecreate(interaction) 
    
            elif customid == "role1green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role1']))
                await self.roledit(interaction) 

            elif customid == "role1red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role1']))
                await self.roledit(interaction)

            elif customid == "role2green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role2']))
                await self.roledit(interaction) 

            elif customid == "role2red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role2']))
                await self.roledit(interaction) 

            elif customid == "role3green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role3']))
                await self.roledit(interaction) 

            elif customid == "role3red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role3']))
                await self.roledit(interaction) 

            elif customid == "role4green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role4']))
                await self.roledit(interaction) 

            elif customid == "role4red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role4']))
                await self.roledit(interaction) 

            elif customid == "role5green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role5']))
                await self.roledit(interaction) 

            elif customid == "role5red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role5']))
                await self.roledit(interaction) 

            elif customid == "role6green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role6']))
                await self.roledit(interaction) 

            elif customid == "role6red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role6']))
                await self.roledit(interaction)

            elif customid == "role7green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role7']))
                await self.roledit(interaction) 

            elif customid == "role7red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role7']))
                await self.roledit(interaction) 

            elif customid == "role8green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role8']))
                await self.roledit(interaction) 

            elif customid == "role8red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role8']))
                await self.roledit(interaction)

            elif customid == "role9green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role9']))
                await self.roledit(interaction) 

            elif customid == "role9red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role9']))
                await self.roledit(interaction)

            elif customid == "role10green":
                await interaction.author.add_roles(interaction.guild.get_role(config['role10']))
                await self.roledit(interaction) 

            elif customid == "role10red":
                await interaction.author.remove_roles(interaction.guild.get_role(config['role10']))
                await self.roledit(interaction)

    async def rolecreate(self,interaction):
        try:
            json_path = f'{current_directory[:-4]}config/{interaction.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            cfgrole1 = disnake.utils.get(interaction.guild.roles, id=config['role1'])
            cfgrole2 = disnake.utils.get(interaction.guild.roles, id=config['role2'])
            cfgrole3 = disnake.utils.get(interaction.guild.roles, id=config['role3'])
            cfgrole4 = disnake.utils.get(interaction.guild.roles, id=config['role4'])
            cfgrole5 = disnake.utils.get(interaction.guild.roles, id=config['role5'])
            cfgrole6 = disnake.utils.get(interaction.guild.roles, id=config['role6'])
            cfgrole7 = disnake.utils.get(interaction.guild.roles, id=config['role7'])
            cfgrole8 = disnake.utils.get(interaction.guild.roles, id=config['role8'])
            cfgrole9 = disnake.utils.get(interaction.guild.roles, id=config['role9'])
            cfgrole10 = disnake.utils.get(interaction.guild.roles, id=config['role10'])

            role1_mention = cfgrole1.mention if cfgrole1 else "Роль не найдена"
            role2_mention = cfgrole2.mention if cfgrole2 else "Роль не найдена"
            role3_mention = cfgrole3.mention if cfgrole3 else "Роль не найдена"
            role4_mention = cfgrole4.mention if cfgrole4 else "Роль не найдена"
            role5_mention = cfgrole5.mention if cfgrole5 else "Роль не найдена"
            role6_mention = cfgrole6.mention if cfgrole6 else "Роль не найдена"
            role7_mention = cfgrole7.mention if cfgrole7 else "Роль не найдена"
            role8_mention = cfgrole8.mention if cfgrole8 else "Роль не найдена"
            role9_mention = cfgrole9.mention if cfgrole9 else "Роль не найдена"
            role10_mention = cfgrole10.mention if cfgrole10 else "Роль не найдена"

            has_role1 = config['role1'] in [role.id for role in interaction.author.roles]
            has_role2 = config['role2'] in [role.id for role in interaction.author.roles]
            has_role3 = config['role3'] in [role.id for role in interaction.author.roles]
            has_role4 = config['role4'] in [role.id for role in interaction.author.roles]
            has_role5 = config['role5'] in [role.id for role in interaction.author.roles]
            has_role6 = config['role6'] in [role.id for role in interaction.author.roles]
            has_role7 = config['role7'] in [role.id for role in interaction.author.roles]
            has_role8 = config['role8'] in [role.id for role in interaction.author.roles]
            has_role9 = config['role9'] in [role.id for role in interaction.author.roles]
            has_role10 = config['role10'] in [role.id for role in interaction.author.roles]

            if has_role1:
                role1 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#1", custom_id="role1red")
            else:
                role1 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#1", custom_id="role1green")

            if has_role2:
                role2 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#2", custom_id="role2red")
            else:
                role2 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#2", custom_id="role2green")

            if has_role3:
                role3 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#3", custom_id="role3red")
            else:
                role3 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#3", custom_id="role3green")

            if has_role4:
                role4 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#4", custom_id="role4red")
            else:
                role4 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#4", custom_id="role4green")

            if has_role5:
                role5 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#5", custom_id="role5red")
            else:
                role5 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#5", custom_id="role5green")

            if has_role6:
                role6 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#6", custom_id="role6red")
            else:
                role6 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#6", custom_id="role6green")

            if has_role7:
                role7 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#7", custom_id="role7red")
            else:
                role7 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#7", custom_id="role7green")

            if has_role8:
                role8 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#8", custom_id="role8red")
            else:
                role8 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#8", custom_id="role8green")

            if has_role9:
                role9 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#9", custom_id="role9red")
            else:
                role9 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#9", custom_id="role9green")

            if has_role10:
                role10 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#10", custom_id="role10red")
            else:
                role10 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#10", custom_id="role10green")
            
            embed = disnake.Embed(
                title=f"Меню выдачи ролей.",
                description=":green_square: Получить роль.\n:red_square: Убрать роль."
            )
            embed.add_field(name="Роль #1",value=f"{role1_mention}",inline=True)
            embed.add_field(name="Роль #2",value=f"{role2_mention}",inline=True)
            embed.add_field(name="Роль #3",value=f"{role3_mention}",inline=True)
            embed.add_field(name="Роль #4",value=f"{role4_mention}",inline=True)
            embed.add_field(name="Роль #5",value=f"{role5_mention}",inline=True)
            embed.add_field(name="Роль #6",value=f"{role6_mention}",inline=True)
            embed.add_field(name="Роль #7",value=f"{role7_mention}",inline=True)
            embed.add_field(name="Роль #8",value=f"{role8_mention}",inline=True)
            embed.add_field(name="Роль #9",value=f"{role9_mention}",inline=True)
            embed.add_field(name="Роль #10",value=f"{role10_mention}",inline=True)

            await interaction.response.send_message(embed = embed,components = [role1,role2,role3,role4,role5,role6,role7,role8,role9,role10], ephemeral = True)
            
        except Exception as e:
            await interaction.response.send_message(f"`{e}`", ephemeral=True)

    async def roledit(self,interaction):
        try:
            json_path = f'{current_directory[:-4]}config/{interaction.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            cfgrole1 = disnake.utils.get(interaction.guild.roles, id=config['role1'])
            cfgrole2 = disnake.utils.get(interaction.guild.roles, id=config['role2'])
            cfgrole3 = disnake.utils.get(interaction.guild.roles, id=config['role3'])
            cfgrole4 = disnake.utils.get(interaction.guild.roles, id=config['role4'])
            cfgrole5 = disnake.utils.get(interaction.guild.roles, id=config['role5'])
            cfgrole6 = disnake.utils.get(interaction.guild.roles, id=config['role6'])
            cfgrole7 = disnake.utils.get(interaction.guild.roles, id=config['role7'])
            cfgrole8 = disnake.utils.get(interaction.guild.roles, id=config['role8'])
            cfgrole9 = disnake.utils.get(interaction.guild.roles, id=config['role9'])
            cfgrole10 = disnake.utils.get(interaction.guild.roles, id=config['role10'])

            role1_mention = cfgrole1.mention if cfgrole1 else "Роль не найдена"
            role2_mention = cfgrole2.mention if cfgrole2 else "Роль не найдена"
            role3_mention = cfgrole3.mention if cfgrole3 else "Роль не найдена"
            role4_mention = cfgrole4.mention if cfgrole4 else "Роль не найдена"
            role5_mention = cfgrole5.mention if cfgrole5 else "Роль не найдена"
            role6_mention = cfgrole6.mention if cfgrole6 else "Роль не найдена"
            role7_mention = cfgrole7.mention if cfgrole7 else "Роль не найдена"
            role8_mention = cfgrole8.mention if cfgrole8 else "Роль не найдена"
            role9_mention = cfgrole9.mention if cfgrole9 else "Роль не найдена"
            role10_mention = cfgrole10.mention if cfgrole10 else "Роль не найдена"

            has_role1 = config['role1'] in [role.id for role in interaction.author.roles]
            has_role2 = config['role2'] in [role.id for role in interaction.author.roles]
            has_role3 = config['role3'] in [role.id for role in interaction.author.roles]
            has_role4 = config['role4'] in [role.id for role in interaction.author.roles]
            has_role5 = config['role5'] in [role.id for role in interaction.author.roles]
            has_role6 = config['role6'] in [role.id for role in interaction.author.roles]
            has_role7 = config['role7'] in [role.id for role in interaction.author.roles]
            has_role8 = config['role8'] in [role.id for role in interaction.author.roles]
            has_role9 = config['role9'] in [role.id for role in interaction.author.roles]
            has_role10 = config['role10'] in [role.id for role in interaction.author.roles]

            if has_role1:
                role1 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#1", custom_id="role1red")
            else:
                role1 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#1", custom_id="role1green")

            if has_role2:
                role2 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#2", custom_id="role2red")
            else:
                role2 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#2", custom_id="role2green")

            if has_role3:
                role3 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#3", custom_id="role3red")
            else:
                role3 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#3", custom_id="role3green")

            if has_role4:
                role4 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#4", custom_id="role4red")
            else:
                role4 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#4", custom_id="role4green")

            if has_role5:
                role5 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#5", custom_id="role5red")
            else:
                role5 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#5", custom_id="role5green")

            if has_role6:
                role6 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#6", custom_id="role6red")
            else:
                role6 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#6", custom_id="role6green")

            if has_role7:
                role7 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#7", custom_id="role7red")
            else:
                role7 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#7", custom_id="role7green")

            if has_role8:
                role8 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#8", custom_id="role8red")
            else:
                role8 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#8", custom_id="role8green")

            if has_role9:
                role9 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#9", custom_id="role9red")
            else:
                role9 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#9", custom_id="role9green")

            if has_role10:
                role10 = disnake.ui.Button(style=disnake.ButtonStyle.red,label="#10", custom_id="role10red")
            else:
                role10 = disnake.ui.Button(style=disnake.ButtonStyle.green,label="#10", custom_id="role10green")
            
            embed = disnake.Embed(
                title=f"Меню выдачи ролей.",
                description=":green_square: Получить роль.\n:red_square: Убрать роль."
            )
            embed.add_field(name="Роль #1",value=f"{role1_mention}",inline=True)
            embed.add_field(name="Роль #2",value=f"{role2_mention}",inline=True)
            embed.add_field(name="Роль #3",value=f"{role3_mention}",inline=True)
            embed.add_field(name="Роль #4",value=f"{role4_mention}",inline=True)
            embed.add_field(name="Роль #5",value=f"{role5_mention}",inline=True)
            embed.add_field(name="Роль #6",value=f"{role6_mention}",inline=True)
            embed.add_field(name="Роль #7",value=f"{role7_mention}",inline=True)
            embed.add_field(name="Роль #8",value=f"{role8_mention}",inline=True)
            embed.add_field(name="Роль #9",value=f"{role9_mention}",inline=True)
            embed.add_field(name="Роль #10",value=f"{role10_mention}",inline=True)
            
            await interaction.response.edit_message(embed = embed,components = [role1,role2,role3,role4,role5,role6,role7,role8,role9,role10])
            
        except Exception as e:
            await interaction.response.send_message(f"`{e}`", ephemeral=True)

def setup(bot):
    bot.add_cog(rolesmenu(bot))