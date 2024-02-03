import disnake
from disnake.ext import commands
import json
from colorama import Fore, Style
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class HelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}HelpCommand{yellow} is loaded...{reset}")


    @commands.slash_command(name="help", description="Команды.")
    async def help(self,ctx):
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
            embed = disnake.Embed(
                description="**Модераторские команды**<a:giga_chad_gamer98:1157219383937093662>\n`/ban` `/mute` `/kick` `/unmute` `/lock` `/unlock` `/rules` `/annoc_*_*` `/ticket`\n\n**Команды развлечения**<a:Applause81:1157865234686541844>\n`/avatar` `/randomizer` `/server-info` `/user-info` `/rps` `/sex` `/coinflip` `/roll` `/say` `/ping`\n\n**Конфиг**<a:gear_anim:1143216395262365758>\n`/config` `/role-config` `/cfg-edit` `/cfg-clear` `/role-cfg-clear` `/install` `/role-install`\n\n**Разное**<a:loading:1143216371463893134>\n`/role-menu` `/auth-menu` `/helpr` `/helpc` `/help`"
            )
            channel = ctx.channel
            await channel.send(embed=embed)
            await ctx.send("done",ephemeral = True)

        else:
                await ctx.send("Недостаточно прав.", ephemeral=True)

    @commands.slash_command(name="helpc", description="Справочник.")
    async def helpc(self,ctx):
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
            embed = disnake.Embed(
                   description="```\n                     ◖Добро пожаловать◗                     \n```\n<#1145932206913618061> - **Канал с новоприбывшими.**\n<#1145932558882844822> - **Информация о сервере.**\n<#1145933407231168663> - **Канал с наказаниями игроков на дискорд сервере.**\n\n```\n                          ◖Новости◗                          \n```\n<#1145928952486039653> - **Канал с новостями.**\n<#1146114951900045312> - **Канал с уведомлениями о рейдах.**\n**Канал<#1145929514967371876> - **Канал с уведомлениями о стримах.**\n\n```\n                         ◖Общение◗                         ```\n<#1108192669752115260> - **Канал для общения.**\n<#1145915736049598575> - **Канал для команд боту.**\n<#1145916233196245102> - **Мемы.**\n<#1145916978914144257> - **Канал для любых медиа, фото/видео/gif и тд. Без общения.**\n<#1149163971451039844> - **Поиск тиммейтов.**\n\n```\n                          ◖Помощь◗                          \n```\n<#1145948659989622815> - **Если возникла проблема с дискорд сервером или сервером RUST, то можете создать обращение. Вам помогут по мере возможности.**\n\n```\n                        ◖Информация◗                        ```\n<#1125215700496175255> - **Актуальный свод правил.**\n<#1135168742603620412> - **Канал для набора персонала.**\n<#1135175872123510795> - **Канал для вопросов к администрации.**\n<#1137538171077410947> - **Ваши идеи по улучшению сервера.**\n\n```\n                     ◖Голосовые каналы◗                     \n```\n<#1145926657664888832> - **Голосовой канал.**\n<#1145926919427207219> - **Голосовой канал.**\n<#1145927044748820621> - **Голосовой канал.**\n<#1145927361863352363> - **Голосовой канал.**\n<#1145927276073078874> - **Голосовой канал.**\n\n```\n                     ◖Приватные каналы◗                     \n```\n<#1145927689446899854> - **Зайдите в этот канал чтобы создать приватный голосовой канал.**"
            )
            channel = ctx.channel
            await channel.send(embed=embed)
            await ctx.send("done",ephemeral = True)

        else:
            await ctx.send("Недостаточно прав.", ephemeral=True)

    @commands.slash_command(name="rules", description="Справочник роли.")
    async def helpr(self, ctx):
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)
        if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
            embed = disnake.Embed(
                description=f"{ctx.guild.get_role(1106589328307667085).mention} - **Создатели SavageRust**\n{ctx.guild.get_role(1146113752194875538).mention} - **Бот для мониторинга онлайна**\n\n**Модераторские роли**\n{ctx.guild.get_role(1135600343758164120).mention} - **Администратор Дискорда**\n{ctx.guild.get_role(1106589326516686848).mention} - **Роль охватывает множество профилей. ТехАдмин, Стафф админ и т.п**\n{ctx.guild.get_role(1132630637900214314).mention} - **Следящий за сервером RUST, отвечает на репорты.**\n{ctx.guild.get_role(1145921277610184794).mention} - **Стажер на пост модератора. Помогает модераторам и администраторам.**\n{ctx.guild.get_role(1132630830703984640).mention} - **Новый участник стаффа, обучается правилам и игровым ситуациям.**\n{ctx.guild.get_role(1106590317941112986).mention} - **Роль для ботов.**\n{ctx.guild.get_role(1145920640352780378).mention} - **Проверяющий тикеты.**\n{ctx.guild.get_role(1146015284096946196).mention} - **Высший модераторский состав.**\n{ctx.guild.get_role(1146015060876079214).mention} - **Низший модераторский состав.**\n{ctx.guild.get_role(1136516423812923463).mention} - **Человек проходящий набор в состав.**\n\n**Тематические роли**\n{ctx.guild.get_role(1069252140809326664).mention} - **Бустер сервера. И вообще хороший человек.**\n{ctx.guild.get_role(1145602728727421018).mention} - **Человек денежно поддержавший проект.**\n{ctx.guild.get_role(1124557311969611836).mention} - **Стример.**\n{ctx.guild.get_role(1130313860641984522).mention} - **▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**\n{ctx.guild.get_role(1098938695844909076).mention} - **Роль выдаваемая при заходе на сервер.**\n\n{ctx.guild.get_role(1139467071697207299).mention} - **Замучен.**"
            )
            channel = ctx.channel
            await channel.send(embed=embed)
            await ctx.send("done",ephemeral = True)
        else:
            await ctx.send("Недостаточно прав.", ephemeral=True)


def setup(bot):
    bot.add_cog(HelpCommand(bot))