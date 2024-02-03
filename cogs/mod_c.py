import disnake
import asyncio
from disnake.ext import commands,tasks
import json
from colorama import Fore, Style
import os
import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class Mod_c(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.check_unmute_task.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Mod_c{yellow} is loaded...{reset}")
           


    @commands.slash_command(name="kick",description="Выгоняет человека с сервера")
    async def kick(self,ctx, member: disnake.Member,reason: str):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Система правосудия",
                    description="Наказание выдали по ошибке? обратитесь в этот дискорд сервер: https://discord.gg/5P9zhFYXcj",
                    color=0xFF0000
                )
                embed.add_field(name="Администратор", value=ctx.author.mention, inline=True)
                embed.add_field(name="Нарушитель", value=member.mention, inline=True)
                embed.add_field(name="Наказание", value="kick", inline=True)
                embed.add_field(name="Причина", value=reason, inline=True)

                if reason == None:
                    reason = "Не указано"
        
                await ctx.send(embed=embed)
                await member.send(embed=embed)
                await member.kick(reason=reason)    
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)  
        except Exception as e:
            await ctx.send(f"Возникла ошибка, возможно наказание не выдалось, обратитесь к администратору бота <@{520550728859779072}>\n`{e}`", ephemeral = True)
        finally:
            await member.kick(reason=reason) 


    @commands.slash_command(name="ban",description="Банит человека на сервере.")
    async def ban(self,ctx, member: disnake.Member,reason: str):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Система правосудия",
                    description="Наказание выдали по ошибке? обратитесь в этот дискорд сервер: https://discord.gg/5P9zhFYXcj",
                    color=0xFF0000
                )
                embed.add_field(name="Администратор", value=ctx.author.mention, inline=True)
                embed.add_field(name="Нарушитель", value=member.mention, inline=True)
                embed.add_field(name="Наказание", value="ban", inline=True)
                embed.add_field(name="Причина", value=reason, inline=True)

                if reason == None:
                    reason = "Не указано"

                await ctx.send(embed=embed)
                await member.send(embed=embed)
                await member.ban(reason=reason)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)     
        except Exception as e:
            await ctx.send(f"Возникла ошибка, возможно наказание не выдалось, обратитесь к администратору бота <@{520550728859779072}>\n`{e}`", ephemeral = True)
        finally:
            await member.ban(reason=reason)

    @commands.slash_command(name="mute", description="Блокирует возможность писать в чаты и присоединяться к голосовым каналам.")
    async def mute(ctx, member: disnake.Member, duration: int, reason: str):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path,'r') as config_file:
                config = json.load(config_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Система правосудия",
                    description="Наказание выдали по ошибке? обратитесь в этот дискорд сервер: https://discord.gg/5P9zhFYXcj",
                    color=0xFF0000
                )
            if config['MUTED_ROLE'] == None:
                await ctx.send("Отсутствует роль для выдачи мута.", ephemeral=True)
                
                
                embed.add_field(name="Администратор", value=ctx.author.mention, inline=True)
                embed.add_field(name="Нарушитель", value=member.mention, inline=True)
                embed.add_field(name="Наказание", value="mute", inline=True)
                embed.add_field(name="Длительность", value=f"{duration}m", inline=True)
                embed.add_field(name="Причина", value=reason, inline=True)
                role = ctx.guild.get_role(config['MUTED_ROLE'])

                if role in member.roles:
                    await ctx.send("Участник уже замучен.", ephemeral=True)
                    return
                
                
                if reason is None:
                    reason = "Не указано"

                await ctx.send(embed=embed)
                await member.add_roles(role)

                end_time = datetime.datetime.now() + datetime.timedelta(minutes=duration)
                
                json_logs_path = f"{current_directory[:-4]}/logs/mute_log.json"

                try:
                    with open(json_logs_path, 'r') as json_file:
                        mutelogs = json.load(json_file)
                except (FileNotFoundError, json.decoder.JSONDecodeError):
                    mutelogs = {"mute_logs_list": {}}

                mutelogs["mute_logs_list"][member.id] = {
                    'server' : ctx.guild.id,
                    'name': member.name,
                    'id': member.id,
                    'start_time': datetime.datetime.now().isoformat(),
                    'end_time': end_time.isoformat(),
                    'reason': reason
                }

                with open(json_logs_path, 'w') as log_file:
                    json.dump(mutelogs, log_file,indent=4)
                    log_file.write('\n')

            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"Возникла ошибка, возможно наказание не выдалось, обратитесь к администратору бота <@{520550728859779072}>\n`{e}`", ephemeral = True)
        finally:
            await member.add_roles(role)

    @tasks.loop(seconds=10)
    async def check_unmute_task(self):
        try:
            json_logs_path = f"{current_directory[:-4]}logs/mute_log.json"
            print(json_logs_path)
            with open(json_logs_path, 'r') as json_file:
                mutelogs = json.load(json_file)
            print(f"{red}unmutexxx{reset}")
            current_time = datetime.datetime.now()
            for guild in self.bot.guilds:
                json_path = f'{current_directory[:-4]}config/{guild.id}.json'
                with open(json_path,'r') as config_file:
                    config = json.load(config_file)
                for member_id, mute_data in list(mutelogs["mute_logs_list"].items()):
                    end_time = datetime.datetime.fromisoformat(mute_data["end_time"])
                    member = guild.get_member(int(member_id))
                    if member and current_time >= end_time:
                        role = guild.get_role(config["MUTED_ROLE"])
                        if role:
                            await member.remove_roles(role)
                            print(mutelogs["mute_logs_list"][member_id])
                            del mutelogs["mute_logs_list"][member_id]
            with open(json_logs_path, 'w') as json_file:
                json.dump(mutelogs, json_file, indent=4)
        except Exception as e:
            print(e)
                
    @check_unmute_task.before_loop
    async def before_check_unmute_task(self):
        await self.bot.wait_until_ready()

    @commands.slash_command(name="unmute",description="Размучивает пользователя.")
    async def unmute(self,ctx, member: disnake.Member,reason: str):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            json_logs_path = f"{current_directory[:-4]}/logs/mute_log.json"
            with open(json_logs_path, 'r') as json_file:
                mutelogs = json.load(json_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    title="Система правосудия",
                    description="Снятие мута",
                    color=0x00FF00
                )
                embed.add_field(name="Администратор", value=ctx.author.mention, inline=True)
                embed.add_field(name="Пользователь", value=member.mention, inline=True)
                embed.add_field(name="Причина", value=reason, inline=True)
                role = disnake.utils.get(ctx.guild.roles, id=config['MUTED_ROLE'])
                if reason == None:
                    reason = "Не указано"
                await ctx.send(embed=embed)
                
                for member_id, mute_data in list(mutelogs["mute_logs_list"].items()):
                    if mute_data['id'] == member.id and mute_data['server'] == ctx.guild.id:
                        role = ctx.guild.get_role(config['MUTED_ROLE'])
                        if role:
                            await member.remove_roles(role)
                        del mutelogs["mute_logs_list"][member_id]
                        with open(json_logs_path, 'w') as json_file:
                            json.dump(mutelogs, json_file, indent=4)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"Возникла ошибка, возможно мут не был снят, обратитесь к администратору бота <@{520550728859779072}>\n`{e}`", ephemeral = True)

    @commands.slash_command(name="lock", description="Блокирует пользователям возможнсть писать в канал.")
    async def lock(self,ctx):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    description=":lock:Канал заблокирован",
                    color=0xFF0000
                )
                channel = ctx.channel
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"Возникла ошибка: {e}", ephemeral=True)

    @commands.slash_command(name="unlock", description="Открывает доступ писать в чат пользователям.")
    async def unlock(self,ctx):
        try:
            json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)
            if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
                embed = disnake.Embed(
                    description=":unlock:Канал разблокирован",
                    color=0x00FF00
                )
                channel = ctx.channel
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Недостаточно прав.", ephemeral=True)
        except Exception as e:
            await ctx.send(f"Возникла ошибка: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Mod_c(bot))