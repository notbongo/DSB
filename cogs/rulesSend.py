import disnake
from disnake.ext import commands
from colorama import Fore, Style
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class Rules(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = self

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}RulesSend{yellow} is loaded...{reset}")  

    @commands.command(name="rules", description="Правила.")
    async def rules(self,ctx):
        embednote = disnake.Embed(
            title=f"Правила дискорд **SavageRust[RU]**",
            description=f"**ПРИМЕЧАНИЯ**\n- Незнание правил не отвлекает от ответственности\n- Высший состав имеет право выдавать наказания исходя из ситуации и игнорируя рамки сроков указанные в правилах.\n- Администрация вправе снимать наказания если конфликт смог разрешится мирным путём.\n- Здравый смысл превыше любого правила, в случае если правила ему противоречат, решения основываются именно на нём.\n- Правила Discord работают на все чаты. Дополнительные запреты на другие каналы будут прописано отдельно в закреплённых сообщениях в этих же каналах.\n- От скольки выдаётся рецидив указано в сами правилах после `x`."
        )

        embed11 = disnake.Embed(
            title="**Правило — 1.1**",
            description="```\nЗапрещена отправка гиф/видео файлов которые способны вызвать вылет дискорда и тп.\n```"
        )
        embed11.add_field(name="> Наказание", value="```\n[Пред | 30m mute — 3d mute | Рецидив x5]\n```", inline=True)
        embed11.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)
        
        embed12 = disnake.Embed(
            title="**Правило — 1.2**",
            description="```\nЗапрещено отправлять множественные однотипные/бессмысленные сообщения в любые каналы.\n```"
        )
        embed12.add_field(name="> Наказание", value="```\n[Пред | 1h mute — 3d mute | Рецидив x5]\n```", inline=True)
        embed12.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embed13 = disnake.Embed(
            title="**Правило — 1.3**",
            description="```\nЗапрещено отправлять nsfw/18+ контент.\n```"
        )
        embed13.add_field(name="> Наказание", value="```\n[Пред | 10m mute — 1d mute | Рецидивx8]\n```", inline=True)
        embed13.add_field(name="> Рецидив", value="```\nBan / Kick / Mute   \n```", inline=True)

        embed14 = disnake.Embed(
            title="**Правило — 1.4**",
            description="```\nЗапрещено напрямую грубо оскорблять человека или его родственников.\n```"
        )
        embed14.add_field(name="> Наказание", value="```\n[Пред | 10m mute — 7d mute | Рецидив x10]\n```", inline=True)
        embed14.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embed15 = disnake.Embed(
            title="**Правило — 1.5**",
            description="```\nЗапрещена реклама сторонних twitch/дискорд каналов.\n```"
        )
        embed15.add_field(name="> Наказание", value="```\n[Пред | 1h mute — 7d mute | Рецидив x2]\n```", inline=True)
        embed15.add_field(name="> Рецидив", value="```\nBan / Kick / Mute   \n```", inline=True)

        embed16 = disnake.Embed(
            title="**Правило — 1.6**",
            description="```\nЗапрещена отправка фишинговых, вредоностных ссылок, а так-же ссылки на казино/микрозаймы и другие подобные ссылки.\n```"
        )
        embed16.add_field(name="> Наказание", value="```\n[ Ban ]\n```", inline=True)
        embed16.add_field(name="> Рецидив", value="```\n-----------------\n```", inline=True)

        embed17 = disnake.Embed(
            title="**Правило — 1.7**",
            description="```\nЗапрещено множественно упоминать (@name/@role) без веской причины.\n```"
        )
        embed17.add_field(name="> Наказание", value="```\n[Пред | 10m mute — 3d mute | Рецидив x8]\n```", inline=True)
        embed17.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embed18 = disnake.Embed(
            title="**Правило — 1.8**",
            description="```\nЗапрещено угрожать расправой в реальной жизни.\n```"
        )
        embed18.add_field(name="> Наказание", value="```\n[Пред | 40m mute — 7d mute | Рецидив]\n```", inline=True)
        embed18.add_field(name="> Рецидив", value="```\nBan / Kick / Mute     \n```", inline=True)

        embed19 = disnake.Embed(
            title="**Правило — 1.9**",
            description="```\nЗапрещена реклама сторонних дискорд в никнейме/в статусе/обо мне.\n```"
        )
        embed19.add_field(name="> Наказание", value="```\n[Карантин до добровольного удаления рекламы + 8h mute | Рецидив x2]\n```", inline=True)
        embed19.add_field(name="> Рецидив", value="```\nBan\n```", inline=True)

        embed110 = disnake.Embed(
            title="**Правило — 1.10**",
            description="```\nАдминистрация имеет право выдавать наказание исходя из ситуации даже если оно не подписана каким либо пунктом правил.\n```"
        )
        embed110.add_field(name="> Наказание", value="```\n[Ban/Mute/Warn/Карантин]\n```", inline=True)
        embed110.add_field(name="> Рецидив", value="```\n-----------------\n```", inline=True)

        embedvoice = disnake.Embed(
            title="**Правила Войс-чатов**"
        )

        embed21 = disnake.Embed(
            title="**Правило — 2.1**",
            description="```\nЗапрещено вести себя чрезмерно неадекватно в войс-чате. ( оскорблять людей и орать в микрофон )\n```"
        )
        embed21.add_field(name="> Наказание", value="```\n[Пред | 30m mute — 7d mute | Рецидив]\n```", inline=True)
        embed21.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embed22 = disnake.Embed(
            title="**Правило — 2.2**",
            description="```\nЗапрещено мешать комфортному нахождению в войс-чате. ( постоянно перезаходить, производить неприятные звуки, bassboost и т.п)\n```"
        )
        embed22.add_field(name="> Наказание", value="```\n[Пред | 30m mute — 7d mute | Рецидив]\n```", inline=True)
        embed22.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embed23 = disnake.Embed(
            title="**Правило — 2.3**",
            description="```\nЗапрещено одновременное использование твинк аккаунтов для общения в войс чате.\n```"
        )
        embed23.add_field(name="> Наказание", value="```\n[Пред | 30m mute — 1d mute | Рецидив]\n```", inline=True)
        embed23.add_field(name="> Рецидив", value="```\nBan / Kick / Mute\n```", inline=True)

        embedrust = disnake.Embed(
            title="**Правила RUST**",
            description="Актуальные правила находятся по этой ссылке:\nhttps://docs.google.com/document/d/1J-X7UaZ8cCdZiezfzb4D2d062u5XWhGUjqxootD8GsU/edit?usp=sharing"
        )

        embedadminrules = disnake.Embed(
            title="**Правила администрации**"
        )

        embedAA = disnake.Embed(
            title="**Правило — AA**",
            description="```\nЗапрещено использовать свои права в корыстных целях.\n```"
        )
        embedAA.add_field(name="> Наказание", value="```\n[Выговор x1]\n```", inline=True)
        embedAA.add_field(name="> Выговор х3", value="```\nСнятие/Ban/Kick                                 \n```", inline=True)

        embedEH = disnake.Embed(
            title="**Правило — EA**",
            description="```\nЗапрещено не подчиняться системе иерархии.\n```"
        )
        embedEH.add_field(name="> Наказание", value="```\n[Выговор x1]\n```", inline=True)
        embedEH.add_field(name="> Выговор х5", value="```\nСнятие/Ban/Kick                                 \n```", inline=True)

        embedSV = disnake.Embed(
            title="**Правило — SV**",
            description="```\nЗапрещено использовать свои права в целях слить свою привелегию.\n```"
        )
        embedSV.add_field(name="> Наказание", value="```\n[Снятие + Ban]\n```", inline=True)
        embedSV.add_field(name="> Рецидив", value="```\n-----------------\n```", inline=True)

        channel = ctx.channel
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(json_path) as config_file:
            config = json.load(config_file)

        if ctx.guild.id != config['BANNER']:
            await ctx.send("На этом сервере команда запрещена.", ephemeral=True)
            return
        
        if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
            await ctx.send("done", ephemeral=True)
            await channel.send(embed=embednote)
            await channel.send(embed=embed11)
            await channel.send(embed=embed12)
            await channel.send(embed=embed13)
            await channel.send(embed=embed14)
            await channel.send(embed=embed15)
            await channel.send(embed=embed16)
            await channel.send(embed=embed17)
            await channel.send(embed=embed18)
            await channel.send(embed=embed19)
            await channel.send(embed=embed110)
            await channel.send(embed=embedvoice)
            await channel.send(embed=embed21)
            await channel.send(embed=embed22)
            await channel.send(embed=embed23)
            await channel.send(embed=embedrust)
            await channel.send(embed=embedadminrules)
            await channel.send(embed=embedAA)
            await channel.send(embed=embedEH)
            await channel.send(embed=embedSV)

        else:
            await ctx.send("Недостаточно прав.", ephemeral=True)

def setup(bot):
    bot.add_cog(Rules(bot))