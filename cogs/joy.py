import disnake
from disnake.ext import commands
from colorama import Fore, Style
import json
import os
import random
from disnake import Button, ButtonStyle
import random
from datetime import datetime, timedelta

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class joy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.games = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Joy{yellow} is loaded...{reset}")

    @commands.slash_command(name="sex", description="Секс...")
    async def sex(self,ctx,member: disnake.Member):
        if ctx.guild.id == 818710560899465256:
        
            json_path = f'{current_directory[:-4]}config/{member.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            random_number = random.randint(100, 999)
            random_chanse = random.randint(0,10)
            randompics = random.randint(0,62)

            words = ["сношаются","спариваются","ебуться","трахаются","совокупляются","горячо общаются","любятся","занимаются сексом","проводят интимное время","удовлетворяют друг друга","спариваются"]

            words1 = ["ебёт","дерёт","спускает сперму в","принуждает"]

            words2 = ["Отсоси.","Письку падёргай оборванец.","Почихарди в трусиках мальчик.","Заглотни пизду мертвой жирухи уебан.","Лох","В трусы напруди.","Закинься солью чихардист","Хрюкни чубахлопчек."]

            links = ["https://cdn.discordapp.com/attachments/1156206494581260328/1156863381790281780/10d.gif?ex=65172d3b&is=6515dbbb&hm=1ebf725968b9c77c8ab2c48748213b87370836a3ca499f4b90a25ceab9f26490&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863382406836275/1d.gif?ex=65172d3b&is=6515dbbb&hm=19053c77a79409083a39cdb1b6528fb201f59af3eaf1f0388a624c795471d254&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863383094689822/2d.gif?ex=65172d3c&is=6515dbbc&hm=028b8bff6ba14c0d43710284333b7d85189697a96d7a0b213bb29fbaa01d527e&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863383694495765/3d.gif?ex=65172d3c&is=6515dbbc&hm=58e14ebbea1aaac2b258e5f68ef2f967e018fe0d0b75e015acc2b250610ac4e4&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863384298467338/4d.gif?ex=65172d3c&is=6515dbbc&hm=0349811b9368e786b0764f8d8e6a97348e011e42a0518e99f5b3197bd12abf7e&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863385141530644/5d.gif?ex=65172d3c&is=6515dbbc&hm=8a4e8987ba3005e921ecb7cf76b9b8f09b0e506e38640df7a9ebd17bfd4d5f62&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863385875513354/6d.gif?ex=65172d3c&is=6515dbbc&hm=e3844192c2087866535ce0a7cc82b14e5e125835d4be791a35bee28d7a10e47f&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863388085932104/7d.gif?ex=65172d3d&is=6515dbbd&hm=76ea23d4bb947ed6bce443fe9bedc6475f60ff78bfbdbae51d807626d8c3c965&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863388824109086/8d.gif?ex=65172d3d&is=6515dbbd&hm=14958a37fff73701adc295850ff2fbb9dac17b520d0b853c3a810e93143ce358&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156863389650407474/9d.gif?ex=65172d3d&is=6515dbbd&hm=a07c6ce67ff3656fd4d1e408d1bc587489a7afd8d01dc7a01c7482b846fa84d9&",

                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865850851205140/26v.gif?ex=65172f88&is=6515de08&hm=1a7f6c77d3d1cc0bfde13724abb0192928647c2629e2f1d69cd5077e968df6b5&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865851450982500/27v.gif?ex=65172f88&is=6515de08&hm=552e02e117e3a17e0e6109cc128d7b4a04a451733804eaab41f1a44420314890&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865852306628628/28v.gif?ex=65172f88&is=6515de08&hm=bcd32bc02abb28dfc20ccdf18056d9a6bc8a84247ebce7c97824e455c49fcfe9&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865853531357224/29v.gif?ex=65172f89&is=6515de09&hm=aa88350893eda9397d7da358d1c1b2f1995c672e8ad533b88878086015a0fa9f&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865854407987231/30v.gif?ex=65172f89&is=6515de09&hm=d7f1007f43ca305aa8f7300c83be0f8583808a41fe50ff9ea8cd38b736c92768&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865855007752242/21v.gif?ex=65172f89&is=6515de09&hm=2c4a2991fe166e9933ef4cdc08b9d7b2826db80f5f3add0c146a5ed45a1f2a33&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865855796289586/22v.gif?ex=65172f89&is=6515de09&hm=6925702f3872715452f54c0fbf5ffd0eafdf2127851d9d643e5c20fa9fcd03aa&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865856530305056/23v.gif?ex=65172f89&is=6515de09&hm=13ed7b17eaab57218cb580c96e51a54873e06fe19beb180b9f9c5b404cd7d1f1&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865857314619412/24v.gif?ex=65172f89&is=6515de09&hm=b4d7f612cbb86ae36f79d385e041e111046a21f8e4ce0a431ff8d026d0d5d9f2&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156865857968939038/25v.gif?ex=65172f8a&is=6515de0a&hm=caa30b29f618e3aabaec0339298d0ca50eb1036e3542de15a9c3a33cf6195320&",
                    
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866058213400606/11c.gif?ex=65172fb9&is=6515de39&hm=6dff2f774ebfe90b5f5d7e0b9288901febe33057ae084ca2c06ed48d5ad9ebb5&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866059182297159/12c.gif?ex=65172fba&is=6515de3a&hm=7d46e2d991cd5bd30df9e95d5548985f658eed7817524a0c4809e20f49e1698f&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866059962429450/13c.gif?ex=65172fba&is=6515de3a&hm=1634530cd0868ed1fa881f02c94d8d44f35e6cc69aa1e89ce3d805e8dbc67d91&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866060545433680/14c.gif?ex=65172fba&is=6515de3a&hm=44e3de3abce2ac90e034923c289aa39d814ae463297fe3f224db6a6c9c69efa4&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866061254283336/15c.gif?ex=65172fba&is=6515de3a&hm=a39652c36a11cd2ecd22a1c70c0ae4867cb90665f4891ef8a0fa203985a32438&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866061979889686/16c.gif?ex=65172fba&is=6515de3a&hm=90474eca3da4f66e2c4025b5419da0da570bb474b2cb6b1304f0c3d589197e0f&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866062697111563/17c.gif?ex=65172fba&is=6515de3a&hm=95cf520e3354c419281b9c474048713d85187da5f85c7a0357581d53e1e4035b&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866063309492314/18c.gif?ex=65172fbb&is=6515de3b&hm=07cbe68771fbbf1727ee4b2addb363b31156877463f3a4aa7a55c755b818d571&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866063896686754/19c.gif?ex=65172fbb&is=6515de3b&hm=30f6a1fd68deeb3b13475ab9b48dbd19f05bd1ad756f597eb10e8589e9285851&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866064467107920/20c.gif?ex=65172fbb&is=6515de3b&hm=66667b0d823c526b6e37a78067046684db3e2bf0343fd2622018213515a64971&",

                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866197040664597/31b.gif?ex=65172fda&is=6515de5a&hm=b4da3f082e6b7f6df28d496f0e65a8fb3f86e963f3e8a1be5aa140dfc240fa64&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866197770489957/32b.gif?ex=65172fdb&is=6515de5b&hm=e2b861a0feb07841bde9258ecadccd61c41cfa49c63714efd8523a99a9c43231&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866198626123786/33b.gif?ex=65172fdb&is=6515de5b&hm=d25816d197ce90be3523a7889707345318a121adcc3ba146ccb4dcfbc295ad56&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866199532097546/34b.gif?ex=65172fdb&is=6515de5b&hm=9b7d6fb7069ac479fb9c21bab54588eae7ec66f034c95ee6068ebd5e25b0c6ff&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866200341581835/35b.gif?ex=65172fdb&is=6515de5b&hm=052d0164fb8d8109dfd2ef20b48ef382cd0a8095cf97ca029846ce0a8a3f2484&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156866201469865995/36b.gif?ex=65172fdb&is=6515de5b&hm=f52cf1ba83e81c5b3401309eff2ffff327ba7d1cee6ce58c4ffc4517c0060641&",

                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874873994489866/49e.gif?ex=651737ef&is=6515e66f&hm=9d592ed5a6a886b962014f787e6111bb9393852b0d8328d834e8e73a5f0d4c5c&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874874833338428/43e.gif?ex=651737ef&is=6515e66f&hm=ab81c6dd77eb02424fa686dee0b24634532ef486e3e78e1151cde2938b2be91e&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874875693178880/44e.gif?ex=651737f0&is=6515e670&hm=cfdbf2d62717304c6ee6c9404c72422aacb752261bf1aedbb1d63664a85e2f00&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874876620124201/45e.gif?ex=651737f0&is=6515e670&hm=881b93360d83b75e15a77fc2f833a471914071b0b2bc75deb0d690fc9cd8ff7e&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874877622550610/46e.gif?ex=651737f0&is=6515e670&hm=81b4e7cd8c91bb01eaa070794fa437519af4fd8082d7613c8509d7b2bf95f314&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874878323007571/47e.gif?ex=651737f0&is=6515e670&hm=c7d0b173f531d4b4810cc579fc2bbdb7cb28b658b4d876a48c8bb28e6c7d1061&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874878885048361/48e.gif?ex=651737f0&is=6515e670&hm=d4254daa4726c0694dc2f30f5062740624014f419e91f1af2f7f7efd5b766fc3&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874904730353704/42w.gif?ex=651737f6&is=6515e676&hm=d44e0a69f9b0117576b8b79baa014e043dddcec758c7284ba469aea1bf4a8e96&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874905967656960/37w.gif?ex=651737f7&is=6515e677&hm=03ac07a594512c302b1092231096abde3ae717e8c1725c6b464dd6b1bc475106&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874907012050964/38w.gif?ex=651737f7&is=6515e677&hm=023f2bb66c01e75da9220c2485a6b310181bbb93aa026ecfa212d9763803ec14&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874907968339988/39w.gif?ex=651737f7&is=6515e677&hm=40b1ea9bde8896bbf0d3a02f0356d251c536c93c748b121341d4b80dcf4805ee&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874909239226450/40w.gif?ex=651737f8&is=6515e678&hm=9ac0842c348746fce3f4fd5de8cb52ba85e112feeb2b08d5345f399dfd1b35ad&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156874910036148296/41w.gif?ex=651737f8&is=6515e678&hm=c255865c6ff0677da379167644549fa600e633ad9f13f58d8c64f234b7a0ec38&",

                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156883081203036180/50t.gif?ex=65173f94&is=6515ee14&hm=06e86a6ce7c3dbd43fa3a3e848eee91a0b2eb4f946753d8e806130fa77a61048&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156883082893328424/51t.gif?ex=65173f94&is=6515ee14&hm=c11c010c481d81a9107b789b3dec1b6d87585df69bd3ce5a6207da1270372f85&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156883083853828127/52t.gif?ex=65173f95&is=6515ee15&hm=5abc458b2f7a27676f170e7d5880d7550bc9545ffc1f6cc7bbdc064e32f4d62d&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156883084856274954/53t.gif?ex=65173f95&is=6515ee15&hm=70efabfcb537654f9b9fc03bbe592d817a5cb0f1c434b953545a9086966ce50a&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156883086076809216/54t.gif?ex=65173f95&is=6515ee15&hm=89b6cd523cfd8b5cd4cc36cba1d54f32179885756ba5e7d32169968b1f276b78&",

                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156887889045622844/63.gif?ex=6517440e&is=6515f28e&hm=33d0e613a0a0ad0c6f1d4fdb79864fd4ddea1143c751de77ca46b8fa53a7f47d&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889272452919326/56r.gif?ex=65174558&is=6515f3d8&hm=18a1938396a40343cbd9d4cc1811f57511800dac3d252704e3816faf478915d6&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889273778311271/57r.gif?ex=65174558&is=6515f3d8&hm=c747296dd69118f17fd99b2bc81ce8340d03cfcf2cd4ff643c058607881a487f&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889274994659349/58r.gif?ex=65174559&is=6515f3d9&hm=35a6f105a34e62d09ceb8dfd73e963a466717f69e104b0d1727ffacfde2a1b54&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889276026466325/59r.gif?ex=65174559&is=6515f3d9&hm=fac07f038ff93d115f7e04a1060730a311cddcaf92808bef77d6d75ad6b8400e&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889277087617084/60r.gif?ex=65174559&is=6515f3d9&hm=1c63ccc7d38698f3c0de6150dc59565274ae1abc6c839c6d38cc848205ee6d63&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889277708386335/61r.gif?ex=65174559&is=6515f3d9&hm=1bd7fdf24466a6384f9204421ccaf6d79f0ef6a201ef678785331da1f8ec87e8&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889278358491156/62r.gif?ex=65174559&is=6515f3d9&hm=e532757b22e598398a7afbd71d2fe0d795e2b83a3b442ef049f81de3ae8c3834&",
                    "https://cdn.discordapp.com/attachments/1156206494581260328/1156889280388546580/55r.gif?ex=6517455a&is=6515f3da&hm=4ffe8c20d0028968ddc12fd7a7b198a817d279a46415b7557bc835bc5dd7a6da&"]

            random_word = random.choice(words)

            random_word1 = random.choice(words1)

            random_word2 = random.choice(words2)

            randompicsmsv = random.choice(links)

            if member.id == 520550728859779072:
                embedno0 = disnake.Embed(
                    description=f"**{random_word2}**"
                )
                embedno0.set_image(url="https://steamuserimages-a.akamaihd.net/ugc/2038483691961211171/73BD90FDBB468D8877422D569E1921AEDC1224A6/")
                await ctx.send(embed=embedno0)
            elif random_chanse == 0:
                embedsex0 = disnake.Embed(
                    description=f"**По всему офису разносится ритмичный стук и глухой стон..\nВ кабинете {random_number} {ctx.author.mention} и {member.mention} {random_word}**",
                    color=0xF08080
                )
                embedsex0.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex0, ephemeral=True)
            elif random_chanse == 1:
                embedsex1 = disnake.Embed(
                    description=f"**Звуки секса переполняют заветшалый солевой притон.\nНа гнилом матрасе {random_word} {ctx.author.mention} и {member.mention}.**",
                    color=0xF08080
                )
                embedsex1.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex1)
            elif random_chanse == 2:
                embedsex2 = disnake.Embed(
                    description=f"**Лгбт это плохо! заявил проповедник на улице.\n{ctx.author.mention} и {member.mention} доказали обратное. {ctx.author.mention} и {member.mention} жестко {random_word}.**",
                    color=0xF08080
                )
                embedsex2.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex2)
            elif random_chanse == 3:
                embedsex3 = disnake.Embed(
                    description=f"**В ночном клубе разносится музыка и глухие стоны веселья.\nЗа одном из столиков в позе рака {random_word} {ctx.author.mention} и {member.mention}.**",
                    color=0xF08080
                )
                embedsex3.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex3)
            elif random_chanse == 4:
                embedsex4 = disnake.Embed(
                    description=f"**В городском парке под звуки дождя.\nВ кустах {ctx.author.mention} насилует {member.mention}**",
                    color=0xF08080
                )
                embedsex4.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex4)
            elif random_chanse == 5:
                embedsex5 = disnake.Embed(
                    description=f"**Закрытая школьная библиотека наполнилась запахом слюней, эякулята и мочи.\nЗа стойкой администратора {random_word} {ctx.author.mention} и {member.mention}.**",
                    color=0xF08080
                )
                embedsex5.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex5)
            elif random_chanse == 6:
                embedsex6 = disnake.Embed(
                    description=f"**Урок начальных классов прервался из-за непрерывных звуков глотания.\nНа последних партах {ctx.author.mention} и {member.mention} {random_word1}**",
                    color=0xF08080
                )
                embedsex6.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex6)
            elif random_chanse == 7:
                embedsex7 = disnake.Embed(
                    description=f"**Анальная боль не покидала {member.mention}.\nСегодня проктолог {ctx.author.mention} помог справится с тяготами бытия {member.mention}**",
                    color=0xF08080
                )
                embedsex7.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex7)
            elif random_chanse == 8:
                embedsex8 = disnake.Embed(
                    description=f"**Хронический стокгольмский синдром был обнаружен у {member.mention}\nВидимо {member.mention} понравился секс с {ctx.author.mention}**",
                    color=0xF08080
                )
                embedsex8.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex8)
            elif random_chanse == 9:
                embedsex9 = disnake.Embed(
                    description=f"**Белая пелена перед глазами.\nВидимо {ctx.author.mention} устроил анальный lockdown {member.mention}**",
                    color=0xF08080
                )
                embedsex9.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex9)
            elif random_chanse == 10:
                embedsex10 = disnake.Embed(
                    description=f"**`Я НЕКРОМАНТ!`заявил {ctx.author.mention}\n И выебал труп {member.mention}**",
                    color=0xF08080
                )
                embedsex10.set_image(url=randompicsmsv)
                await ctx.send(embed=embedsex10)
        else:
            await ctx.send("Команда не работает на этом сервере!", ephemeral=True)

    @commands.slash_command(name="roll", description="ролл от 1 до 100.")
    async def roll(self,ctx):
        roll = random.randint(0,100)
        ctxurl = ctx.author.avatar.url[:-10]
        embedroll = disnake.Embed(
            description=f"{ctx.author.mention} использует ролл и получает **`{roll} из 100`**"
        )
        embedroll.set_author(
            name="[ROLL]",
            icon_url=ctxurl
        )
        await ctx.send(embed=embedroll)

    @commands.slash_command(name="coinflip", description="Орёл или решка.")
    async def coinflip(self,ctx):
        if isinstance(ctx.channel, disnake.DMChannel):
            await ctx.send("Бот не работает в личных сообщениях.",ephemeral = True)
        coin = ["Выпал **`Орёл`**","Выпала **`Решка`**"]
        coinflip = random.choice(coin)
        ctxurl = ctx.author.avatar.url[:-10]

        embedcoin = disnake.Embed(
            description=f"{ctx.author.mention} кидает монетку. {coinflip}"
        )
        embedcoin.set_author(
            name="[COINFLIP]",
            icon_url=ctxurl
        )

        await ctx.send(embed=embedcoin)

    @commands.slash_command(name="say", description="Общение через бота.")
    async def say(self,ctx,text: str):
        channel = ctx.channel
        await ctx.send("Отправлено.", ephemeral=True)
        await channel.send(text)

    @commands.slash_command(name="avatar", description="Получить аватарку человека.")
    async def avatar(self,ctx,member):
        if isinstance(ctx.channel, disnake.DMChannel):
            await ctx.send("Бот не работает в личных сообщениях.",ephemeral = True)
        memberavatar = member.avatar.url[:-10]

        embedavatar = disnake.Embed(
            title=f"@{member.author}"
        )
        embedavatar.set_image(url=memberavatar)

        await ctx.send(embed=embedavatar)

    @commands.slash_command(name="rps", description="Камень, ножницы, бумага.")
    async def rps(self, ctx: disnake.ApplicationCommandInteraction, member: disnake.Member):
        if ctx.author == member:
            await ctx.send("Вы не можете играть сами с собой.", ephemeral=True)
            return

        button3 = disnake.ui.Button(style=disnake.ButtonStyle.primary, label="Камень", custom_id="rock")
        button2 = disnake.ui.Button(style=disnake.ButtonStyle.primary, label="Ножницы", custom_id="scissors")
        button1 = disnake.ui.Button(style=disnake.ButtonStyle.primary, label="Бумага", custom_id="paper")

        embed = disnake.Embed(
            title="Камень, Ножницы, Бумага",
            description=f"{ctx.author.mention} против {member.mention}. Выберите свой вариант!",
        )

        await ctx.response.send_message(embed=embed, components=[button1, button2, button3])
        message = await ctx.original_message()

        self.games[message.id] = {"author": ctx.author, "member": member, "message": message, "choices": {"author": None, "member": None}}

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        if interaction.component.custom_id not in ("rock", "scissors", "paper"):
            return

        game = self.games.get(interaction.message.id)

        print(game["author"],game["member"],game["choices"])

        if not game:
            return

        user_id = interaction.user.id
        if user_id not in (game["author"].id, game["member"].id):
            await interaction.response.send_message("Вы не участвуете в этой игре.", ephemeral=True)
            return
        
        if game["author"].id == user_id:
            if game["choices"]["author"] is not None:
                await interaction.response.send_message("Вы уже сделали выбор.", ephemeral=True)
                return
        elif game["member"].id == user_id:
            if game["choices"]["member"] is not None:
                await interaction.response.send_message("Вы уже сделали выбор.", ephemeral=True)
                return

        if user_id == game["author"].id:
            game["choices"]["author"] = interaction.component.custom_id
            await interaction.response.send_message(f"Вы выбрали {interaction.component.label}", ephemeral=True)
        else:
            game["choices"]["member"] = interaction.component.custom_id
            await interaction.response.send_message(f"Вы выбрали {interaction.component.label}", ephemeral=True)


        if None not in game["choices"].values():
            await self.resolve_game(game)

    async def resolve_game(self, game):
        author_choice = game["choices"]["author"]
        member_choice = game["choices"]["member"]

        if author_choice == member_choice:
            result = "Ничья!"
        elif (author_choice == "rock" and member_choice == "scissors") or \
             (author_choice == "scissors" and member_choice == "paper") or \
             (author_choice == "paper" and member_choice == "rock"):
            result = f"{game['author'].mention} **победил!**"
        else:
            result = f"{game['member'].mention} **победил!**"

        embed = disnake.Embed(
            title="**Итог игры!**",
            description=f"{game['author'].mention} выбрал {author_choice.capitalize()}\n{game['member'].mention} выбрал {member_choice.capitalize()}\n\n{result}",
        )

        await game["message"].edit(embed=embed,components=[])
        del self.games[game["message"].id]

    @commands.slash_command(name="server-info", description="Информация о сервере.")
    async def serverinfo(self, ctx):
        try:
            guild = ctx.guild
            owner = guild.owner
            server_name = guild.name
            member_count = guild.member_count
            online_members = [member for member in guild.members if member.status == disnake.Status.online]
            online_count = len(online_members)

            text_channel_count = len(guild.text_channels)
            voice_channel_count = len(guild.voice_channels)

            server_avatar_url = guild.icon.url[:-10] if guild.icon else None

            nitro_tier = guild.premium_tier
            nitro_level = guild.premium_subscription_count

            creation_date = guild.created_at + timedelta(days=1)

            embed = disnake.Embed(
                title=f"Информация о сервере {server_name}"
            )

            if server_avatar_url:
                embed.set_thumbnail(url=server_avatar_url)
            else:
                embed.add_field(name="Аватарка.", value=f"Сервер не имеет аватарку.", inline=False)

            embed.add_field(name="Создатель сервера", value=f"{owner.name}#{owner.discriminator}", inline=False)
            embed.add_field(name="Пользователи", value=member_count, inline=True)
            embed.add_field(name="Пользователи онлайн", value=online_count, inline=True)
            embed.add_field(name="", value="", inline=True)
            embed.add_field(name="Нитро", value=f"Уровень: {nitro_level}\nБустов: {nitro_tier}", inline=True)
            embed.add_field(name="Дата создания", value=f"{creation_date.strftime('%Y-%m-%d %H:%M:%S')}", inline=True)
            embed.add_field(name="Количество каналов", value=f"  Текстовые: {text_channel_count}\nГолосовые: {voice_channel_count}", inline=True)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Ошибка: `{e}`", ephemeral=True)

    @commands.slash_command(name="user-info", description="Получить информацию о пользователе.")
    async def userinfo(self, ctx, id="default",mention: disnake.Member="default"):
        try:
            if id != "default" and mention != "default":
                await ctx.send("Выберите только один параметр.", ephemeral=True)
                return
            
            if id == "default":
                id = ctx.author.id

            if mention != "default":
                id = mention.id
                
            id = int(id)

            user = await self.bot.fetch_user(id)
            member = ctx.guild.get_member(id)

            embed = disnake.Embed(
                title="Информация о пользователе."
            )

            user_avatar = user.avatar.url[:-10]

            embed.set_thumbnail(url=user_avatar)

            if member:
                roles_mentions = ', '.join([role.mention for role in member.roles if role.name != "@everyone"])
                roles_count = len([role for role in member.roles if role.name != "@everyone"])
                highest_role = member.top_role.mention
                    
                joined_at = member.joined_at.strftime("%Y-%m-%d")
                joined_at_date = datetime.strptime(joined_at, "%Y-%m-%d")
                joined_at_plus_one_day = joined_at_date + timedelta(days=1)
                joined_at_plus_one_day_str = joined_at_plus_one_day.strftime("%Y-%m-%d")
                    
            else:
                roles_mentions = "Пользователь не находится на сервере или ролей нет."
                roles_count = 0
                highest_role = "Нет высшей роли"
                joined_at_plus_one_day_str = "Неизвестно"

            created_at = user.created_at
            created_at_one_day = created_at + timedelta(days=1)
            created_at_one_day_str = created_at_one_day.strftime("%Y-%m-%d")
                    
            embed.add_field(name="Пользователь", value=f"{user.name}#{user.discriminator} ({user.id})", inline=True)
            embed.add_field(name="Высшая роль", value=f"{highest_role}", inline=True)
            embed.add_field(name="Дата регистрации", value=f"{created_at_one_day_str}", inline=False)
            embed.add_field(name="Дата присоединения к серверу", value=f"{joined_at_plus_one_day_str}", inline=False)
            embed.add_field(name=f"Роли({roles_count})", value=f"{roles_mentions}", inline=False)

            await ctx.send(embed=embed)

        except disnake.NotFound:
            await ctx.send('Пользователь с указанным ID не найден.')

    @commands.slash_command(name="randomize",description="Рандомайзер.")
    async def randomize(self,ctx,sequence_from: int = "1",sequence_to: int = "5",quantity_of_generated: int = "1"):
        try:
            b = 0

            sf = int(sequence_from)

            st = int(sequence_to)

            qof = int(quantity_of_generated)

            if sf <= 0 or st <= 0 or qof <= 1:
                b = b + 1
                await ctx.send(f"Одно из ведённых чисел меньше нуля.", ephemeral = True)

            if qof > 100:
                await ctx.send(f"Нельзя ставить количество генерируемых чисел больше 100.", ephemeral = True)

            if sf >= st:
                b = b + 1
                await ctx.send(f"sequence_from(`{sf}`), не должно быть больше sequence_to({st}).", ephemeral = True)

            if b >= 1:
                return

            randomnubmer = ' '.join(str(random.randint(sf,st)) for _ in range(qof))

            ctxurl = ctx.author.avatar.url[:-10]

            embed = disnake.Embed(
                description=f"Параметры:\nПоследовательность от: {sequence_from}\nПоследовательность до: {sequence_to}\nКол-во генерируемых чисел: {quantity_of_generated}\n\nЧисло: {randomnubmer}"
            )

            embed.set_author(
                name="[RANDOMIZE]",
                icon_url=ctxurl
            )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Ошибка: `{e}`", ephemeral=True)

def setup(bot):
    bot.add_cog(joy(bot))