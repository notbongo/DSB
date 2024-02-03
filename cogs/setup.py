import disnake
from disnake.ext import commands
import os
import json
from colorama import Fore,Style
import asyncio
import inter

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL
magenta = Fore.MAGENTA
lye = Fore.LIGHTYELLOW_EX

class SetupConfig(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}setup{yellow} is loaded...{reset}")

    
    @commands.slash_command(name="config", description="Конфиг лист сервера.")
    async def config(self, ctx):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            join_role = disnake.utils.get(ctx.guild.roles, id=config['JOIN_ROLE'])
            admin_role = disnake.utils.get(ctx.guild.roles, id=config['ADMIN_ROLE'])
            muted_role = disnake.utils.get(ctx.guild.roles, id=config['MUTED_ROLE'])
            authrole = disnake.utils.get(ctx.guild.roles, id=config['Authrole'])

            join_role_mention = join_role.mention if join_role else "Роль не найдена"
            admin_role_mention = admin_role.mention if admin_role else "Роль не найдена"
            muted_role_mention = muted_role.mention if muted_role else "Роль не найдена"
            authrole_mention = authrole.mention if authrole else "Роль не найдена"

            if ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Конфиг вашего сервера",
                    description=f"**[we]Канал приветствия:** `{config['WELCOME_CHANNEL']}` | <#{config['WELCOME_CHANNEL']}>\n**[tl]Канал ТикетЛог:** `{config['TicketlogsChannel']}` | <#{config['TicketlogsChannel']}>\n**[tk]Тикет категория:** `{config['TICKET_CATEGORY']}` | {config['TICKET_CATEGORY']}\n**[nmc]Канал без общения:** `{config['NMChennel']}` | <#{config['NMChennel']}>\n**[pc]Канал приватных гс:** `{config['PRIVATE_CHENNEL_CR']}` | <#{config['PRIVATE_CHENNEL_CR']}>\n**[mr]Роль мута:** `{config['MUTED_ROLE']}` | {muted_role_mention}\n**[ar]Роль администрации** `{config['ADMIN_ROLE']}` | {admin_role_mention}\n**[dr]Роль для новых людей:** `{config['JOIN_ROLE']}` | {join_role_mention}\n**[aut]Роль аутентификации:** `{config['Authrole']}` | {authrole_mention}"
                )
                await ctx.send(embed=embed, ephemeral=True)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(e, ephemeral=True)

            

    @commands.slash_command(name="role-config",description="Конфиг ролей.")
    async def roleconfig(self,ctx):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            cfgrole1 = disnake.utils.get(ctx.guild.roles, id=config['role1'])
            cfgrole2 = disnake.utils.get(ctx.guild.roles, id=config['role2'])
            cfgrole3 = disnake.utils.get(ctx.guild.roles, id=config['role3'])
            cfgrole4 = disnake.utils.get(ctx.guild.roles, id=config['role4'])
            cfgrole5 = disnake.utils.get(ctx.guild.roles, id=config['role5'])
            cfgrole6 = disnake.utils.get(ctx.guild.roles, id=config['role6'])
            cfgrole7 = disnake.utils.get(ctx.guild.roles, id=config['role7'])
            cfgrole8 = disnake.utils.get(ctx.guild.roles, id=config['role8'])
            cfgrole9 = disnake.utils.get(ctx.guild.roles, id=config['role9'])
            cfgrole10 = disnake.utils.get(ctx.guild.roles, id=config['role10'])

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


            if ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Конфиг ролей.",
                    description=f"Роль 1: {role1_mention} | {config['role1']}\nРоль 2: {role2_mention} | {config['role2']}\nРоль 3: {role3_mention} | {config['role3']}\nРоль 4: {role4_mention} | {config['role4']}\nРоль 5: {role5_mention} | {config['role5']}\nРоль 6: {role6_mention} | {config['role6']}\nРоль 7: {role7_mention} | {config['role7']}\nРоль 8: {role8_mention} | {config['role8']}\nРоль 9: {role9_mention} | {config['role9']}\nРоль 10: {role10_mention} | {config['role10']}\n"
                )

                await ctx.send(embed=embed, ephemeral=True)

                print(f"{magenta}=======================\n{lye}Command: /ticket\nВ канале: {ctx.channel} # {ctx.channel.id}\n{ctx.author} # {ctx.author.id} Вызвал меню Ticket\n{magenta}======================={reset}")

            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"`{e}`", ephemeral=True)

    @commands.slash_command(name="role-install",description="Автоматическая установка ролей.")
    async def roleinstall(self,ctx):
        await ctx.response.defer(ephemeral=True)
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)

        b = 0

        if config['role1'] == None:
            role1c = await ctx.guild.create_role(name="Роль 1")
            config['role1'] = role1c.id
        else:
            b = b+1

        if config['role2'] == None:
            role2c = await ctx.guild.create_role(name="Роль 2")
            config['role2'] = role2c.id
        else:
            b = b+1

        if config['role3'] == None:
            role3c = await ctx.guild.create_role(name="Роль 3")
            config['role3'] = role3c.id
        else:
            b = b+1

        if config['role4'] == None:
            role4c = await ctx.guild.create_role(name="Роль 4")
            config['role4'] = role4c.id
        else:
            b = b+1

        if config['role5'] == None:
            role5c = await ctx.guild.create_role(name="Роль 5")
            config['role5'] = role5c.id
        else:
            b = b+1

        if config['role6'] == None:
            role6c = await ctx.guild.create_role(name="Роль 6")
            config['role6'] = role6c.id
        else:
            b = b+1
        
        if config['role7'] == None:
            role7c = await ctx.guild.create_role(name="Роль 7")
            config['role7'] = role7c.id
        else:
            b = b+1

        if config['role8'] == None:
            role8c = await ctx.guild.create_role(name="Роль 8")
            config['role8'] = role8c.id
        else:
            b = b+1
        
        if config['role9'] == None:
            role9c = await ctx.guild.create_role(name="Роль 9")
            config['role9'] = role9c.id
        else:
            b = b+1

        if config['role10'] == None:
            role10c = await ctx.guild.create_role(name="Роль 10")
            config['role10'] = role10c.id
        else:
            b = b+1

        if b >= 1:
            await ctx.send("Процесс прерван. Очистите конфиги ролей.")
        else:
            with open(json_path, 'w') as json_file:
                json.dump(config, json_file, indent=4)
            await ctx.send("Установка завершена.", ephemeral=True)
            print(f"{magenta}=======================\n{lye}Command: role-install\nВ канале: {ctx.channel} # {ctx.channel.id}\n{ctx.author} # {ctx.author.id} Вызвал меню Ticket\n{magenta}======================={reset}")
        

    @commands.slash_command(name="cfg-edit", description="Ручное управление конфигами.")
    async def cfgedit(self,ctx,we="default",tl="default",tk="default",nmc="default",pc="default",mr="default",ar="default",dr="default",aut="default",role1="default",role2="default",role3="default",role4="default",role5="default",role6="default",role7="default",role8="default",role9="default",role10="default"):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            default = "default"
            if ctx.author.guild_permissions.administrator:
                if we != default:
                    config['WELCOME_CHANNEL'] = int(we)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)  
                if tl != default:
                    config['TicketlogsChannel'] = int(tl)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if tk != default:
                    config['TICKET_CATEGORY'] = int(tk)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if nmc != default:
                    config['NMChennel'] = int(nmc)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if pc != default:
                    config['PRIVATE_CHENNEL_CR'] = int(pc)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if mr != default:
                    config['MUTED_ROLE'] = int(mr)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if ar != default:
                    config['ADMIN_ROLE'] = int(ar)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if dr != default:
                    config['JOIN_ROLE'] = int(dr)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if aut != default:
                    config['Authrole'] = int(aut)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role1 != default:
                    config['role1'] = int(role1)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role2 != default:
                    config['role2'] = int(role2)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role3 != default:
                    config['role3'] = int(role3)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role4 != default:
                    config['role4'] = int(role4)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role5 != default:
                    config['role5'] = int(role5)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role6 != default:
                    config['role6'] = int(role6)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role7 != default:
                    config['role7'] = int(role7)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role8 != default:
                    config['role8'] = int(role8)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role9 != default:
                    config['role9'] = int(role9)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)
                if role10 != default:
                    config['role10'] = int(role10)
                    await ctx.send("Изменения в конфигурации внесены.",ephemeral=True)

                with open(json_path, 'w') as json_file:
                        json.dump(config, json_file, indent=4)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"Возникла ошибка!\n ```\n{e}\n```\nОбратитесь с описанием проблемы к <@520550728859779072>", ephemeral=True)

    @commands.slash_command(name="install", description="Запускает автоматическую установку конфигов.")
    async def install(self,ctx):
        try:
            if ctx.author.guild_permissions.administrator:
                b = 0

                await ctx.response.defer(ephemeral=True)

                json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
                with open(json_path) as config_file:
                    config = json.load(config_file)

                if config['MUTED_ROLE'] == None:
                    mutedrole = await ctx.guild.create_role(name="Роль Мута")
                    config['MUTED_ROLE'] = mutedrole.id
                else:
                    b = b+1
            
                if config['NMChennel'] == None:
                    Nomessagechennel = await ctx.guild.create_text_channel("Канал без общения.")
                    config['NMChennel'] = Nomessagechennel.id
                else:
                    b = b+1

                if config['ADMIN_ROLE'] == None:
                    adminrole = await ctx.guild.create_role(name="Роль администрации.")
                    config['ADMIN_ROLE'] = adminrole.id
                else:
                    b = b+1

                if config['JOIN_ROLE'] == None:
                    joinrole = await ctx.guild.create_role(name="Роль для новых людей.")
                    config['JOIN_ROLE'] = joinrole.id
                else:
                    b = b+1
            
                if config['WELCOME_CHANNEL'] == None:
                    welcomech = await ctx.guild.create_text_channel("Канал приветствия.")
                    config['WELCOME_CHANNEL'] = welcomech.id
                else:
                    b = b+1
            
                if config['TicketlogsChannel'] == None:
                    tlc = await ctx.guild.create_text_channel("Канал тикет логов.")
                    config['TicketlogsChannel'] = tlc.id
                else:
                    b = b+1

                if config['TICKET_CATEGORY'] == None:
                    ticketct = await ctx.guild.create_category("Категория для тикетов.")
                    config['TICKET_CATEGORY'] = ticketct.id
                else:
                    b = b+1

                if config['PRIVATE_CHENNEL_CR'] == None:
                    privatevoice = await ctx.guild.create_voice_channel("Создать приватный канал.")
                    config['PRIVATE_CHENNEL_CR'] = privatevoice.id
                else:
                    b = b+1
                
                if config['Authrole'] == None:
                    authrole = await ctx.guild.create_role(name="Роль аутентификации.")
                    config['PRIVATE_CHENNEL_CR'] = authrole.id
                else:
                    b = b+1

                if b >= 1:
                    await ctx.send("Процесс прерван. Очистите все конфиги перед использованием команды.")
                else:
                    with open(json_path, 'w') as json_file:
                        json.dump(config, json_file, indent=4)
                    await ctx.send("Установка завершена.", ephemeral=True)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(e, ephemeral=True)

    @commands.slash_command(name="cfg-clear", description="Очистить конфиги.")
    async def cfgclear(self,ctx):
        try:
            if ctx.author.guild_permissions.administrator:

                await ctx.response.defer(ephemeral=True)

                json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
                with open(json_path) as config_file:
                    config = json.load(config_file)

                config['MUTED_ROLE'] = None
                config['NMChennel'] = None
                config['ADMIN_ROLE'] = None
                config['JOIN_ROLE'] = None
                config['WELCOME_CHANNEL'] = None
                config['TicketlogsChannel'] = None
                config['TICKET_CATEGORY'] = None
                config['PRIVATE_CHENNEL_CR'] = None

                with open(json_path, 'w') as json_file:
                    json.dump(config, json_file, indent=4)
                await ctx.send("Очистка конфигов завершено.", ephemeral=True)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(e, ephemeral=True)

    @commands.slash_command(name="role-cfg-clear", description="Очистить конфиги ролей.")
    async def rolecfgclear(self,ctx):
        try:
            if ctx.author.guild_permissions.administrator:

                await ctx.response.defer(ephemeral=True)

                json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
                with open(json_path) as config_file:
                    config = json.load(config_file)

                config['role1'] = None
                config['role2'] = None
                config['role3'] = None
                config['role4'] = None
                config['role5'] = None
                config['role6'] = None
                config['role7'] = None
                config['role8'] = None
                config['role9'] = None
                config['role10'] = None

                with open(json_path, 'w') as json_file:
                    json.dump(config, json_file, indent=4)
                await ctx.send("Очистка конфигов завершено.", ephemeral=True)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(e, ephemeral=True)

def setup(bot):
    bot.add_cog(SetupConfig(bot))