import wavelinkcord as wavelink
import nextcord
from nextcord.ext import commands
from nextcord.shard import EventItem
import disnake

from disnake.ext import commands
from colorama import Fore, Style

magenta = Fore.MAGENTA
blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = self

    async def on_node(self):
        node: wavelink.Node = wavelink.Node(uri="https://lavalink.clxud.pro:2333",password="youshallnotpass")

        await wavelink.NodePool.connect(client=self.bot,nodes=[node])

        wavelink.Player.autoplay = True

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Music{yellow} is loaded...{reset}")

    @commands.command(name="play",description="Поставить песню на воспроизведение.")
    async def play(self, interaction,search:str):
        query = await wavelink.YouTubeTrack.search(search)

        destination = interaction.user.voice.channel
        if interaction.guild.voice_client:
            vc: wavelink.Player = destination.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = interaction.guild.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(query)
            await interaction.response.send_message(f"Сейчас играет: {vc.current.title}")
        else:
            await vc.queue.put_wait(query)
            await interaction.response.send_message(f"Песня поставленна в очередь")

    @commands.slash_command(name="skip",description="")
    async def skip(self, interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        await vc.stop()
        await interaction.response.send_message(f"Песня была пропущена!")

    @commands.slash_command(name="pause",description="Поставить на паузу.")
    async def pause(self, interaction):
        vc: wavelink.Player = interaction.guild.voice_client

        if vc.is_playing():
            await vc.pause()
            await interaction.response.send_message(f"Поставил песню на паузу")
        else:
            await interaction.response.send_message(f"Песня стоит на паузе")

    @commands.slash_command(name="resume",description="")
    async def resume(self, interaction):
        vc: wavelink.Player = interaction.guild.voice_client

        if vc.is_playing():
            await interaction.response.send_message(f"Песня уже воспроизводится")
        else:
            await interaction.response.send_message(f"Продолжаю воспроизведение")
            await vc.resume()

    @commands.slash_command(name="disconnect",description="Отключить бота.")
    async def disconnect(self, interaction):
        vc: wavelink.Player = interaction.guild.voice_client

        await vc.disconnect
        await interaction.response.send_message(f"Отключаю бота")

    @commands.slash_command(name="queue",description="Посмотреть очередь песен.")
    async def queue(self, interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if not vc.queue.is_empty:
            song_counter = 0
            song = []
            queue = vc.queue.copy()
            embed = nextcord.Embed(title="queue")
            
            for song in queue:
                song_counter += 1
                song.append(song)
                embed.add_field(name=f"[{song_counter}, Кол-во {song.duration}]",value=f"[{song.title}]", inline=False)
            
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Очередь пуста")

def setup(bot):
    bot.add_cog(Music(bot))