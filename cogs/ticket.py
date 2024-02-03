import disnake
from disnake.ext import commands
from disnake import Button, ButtonStyle,ModalInteraction,TextInputStyle
import inter
import json
from colorama import Fore, Style
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

yellow = Fore.YELLOW
lye = Fore.LIGHTYELLOW_EX
red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA
reset = Style.RESET_ALL

button = disnake.ui.Button(style=ButtonStyle.success, label="\u2705 создать обращение", custom_id="ticket_button_open")
button_close_wnr = disnake.ui.Button(style=disnake.ButtonStyle.danger, label="Закрыть", custom_id="close_button_WNR")
button_close_wr = disnake.ui.Button(style=disnake.ButtonStyle.danger, label="Закрыть с причиной", custom_id="close_button_WR")
button_close_t_X = disnake.ui.Button(style=disnake.ButtonStyle.secondary,label="Отклонить", custom_id="close_t_X")
button_delete_msg = disnake.ui.Button(style=disnake.ButtonStyle.primary,label="Удалить", custom_id="delete_msg")
button_join_ticket = disnake.ui.Button(style=disnake.ButtonStyle.primary,label="Взять тикет", custom_id="join_ticket")

class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Причина",
                placeholder="Введите причину закрытия",
                custom_id="Причина закрытия",
                style=TextInputStyle.short,
                max_length=100,
            )
        ]
        super().__init__(title="Create Tag", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        r = inter.response
        embedmodal = disnake.Embed(title="Закрытие тикета")
        for key, value in inter.text_values.items():
            embedmodal = disnake.Embed(
                title= key.capitalize(),
                description= f"Автор: {inter.author.mention}\n\nПричина: `{value[:1024]}`"
            )
            
        await r.send_message(embed=embedmodal,components=[button_close_wnr,button_close_t_X,button_delete_msg])


class TICKET(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{green}Ticket{yellow} is loaded...{reset}")


    @commands.slash_command(name="ticket", description="Создаёт embed для создания тикета.")
    async def ticket(self,ctx):
        json_path = f'{current_directory[:-4]}config/{ctx.guild.id}.json'
        with open(f'{json_path}') as config_file:
            config = json.load(config_file)
        if config['ADMIN_ROLE'] in [role.id for role in ctx.author.roles] or ctx.author.guild_permissions.administrator:
            embed = disnake.Embed(
                title="Создать обращение",
                color=0x00ff00
                )
        
            embed.add_field(
                name="Правила:",
                value="```diff\n- Запрещено оффтопить тикетами\n#Наказание - блокировка доступа к этому каналу\n```",
                inline=False
                )
            await ctx.send(embed=embed, components=[button])
            print(f"{magenta}=======================\n{lye}Command: /ticket\nВ канале: {ctx.channel} # {ctx.channel.id}\n{ctx.author} # {ctx.author.id} Вызвал меню Ticket\n{magenta}======================={reset}")
        else:
            await ctx.send("Недостаточно прав.", ephemeral=True)

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        try:
            json_path = f'{current_directory[:-4]}config/{interaction.guild.id}.json'
            with open(json_path) as config_file:
                config = json.load(config_file)

            user = interaction.user

            existing_ticket_channels = [channel for channel in interaction.guild.text_channels if f"{user}-тикет" in channel.name]

            ticketchannel = interaction.channel

            channel = self.bot.get_channel(config['TicketlogsChannel'])

            embed0 = disnake.Embed(
                    title="Обращение создано!",
                    description=f"Автор тикета:{user.mention} | {user.name}\nИзложите в полной мере суть вашей проблемы\nПримечание:\n```diff\n- За спам причинами закрытия, вам будет выдан мут на 3 дня + закрытие доступа в канал.\n```",
                    color=0x00ff00
            )
        
            embed1 = disnake.Embed(
                title="Причина закрытия - отклонена.",
                description=f"Отклонил: {interaction.author.mention} | {interaction.author.name}"
            )

            embed2 = disnake.Embed(
                description=f"**На вашу проблему откликнулись!**\n**Вам помогает -** {interaction.author.mention} | {interaction.author.name}"
            )

            embed3 = disnake.Embed(
                title= "Тикет закрыт",
                description=f"Закрыл: {user.mention} | {user.name}"
            )

            if interaction.component.custom_id == "delete_msg":
                if config['ADMIN_ROLE'] in [role.id for role in user.roles]:
                    await interaction.message.delete()
                    print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
                else:
                    await interaction.response.send_message("Недостаточно прав.", ephemeral=True)

            elif interaction.component.custom_id == "join_ticket":
                if config['ADMIN_ROLE'] in [role.id for role in user.roles]:
                    await interaction.response.send_message(embed=embed2)
                    print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
                else:
                    await interaction.response.send_message("Недостаточно прав.", ephemeral=True)
        
            elif interaction.component.custom_id == "close_t_X":
                if config['ADMIN_ROLE'] in [role.id for role in user.roles]:
                    await interaction.response.send_message(embed=embed1)
                    print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
                else:
                    await interaction.response.send_message("Недостаточно прав.", ephemeral=True)

            elif interaction.component.custom_id == "close_button_WNR":
                if config['ADMIN_ROLE'] in [role.id for role in user.roles]:
                    await interaction.response.send_message(embed=embed3)
                    messages = await ticketchannel.history(limit=None).flatten()
                    config['TICKET_COUNT'] = config['TICKET_COUNT'] + 1
                    filename = os.path.join("ticket_logs", f"{ticketchannel}-{config['TICKET_COUNT']}.txt")
                    with open(f"{json_path}", "w") as file:
                        json.dump(config, file, indent=4)
                    with open(filename, "w", encoding="utf-8") as file:
                        for message in reversed(messages):
                            if message.embeds:
                                for embed in message.embeds:
                                    line = f"\n{message.author.name}({message.author.id}) → \n{embed.title}{embed.description}\n"
                                    file.write(line)
                            elif message.attachments:
                                for attachment in message.attachments:
                                    if attachment.content_type.startswith('image/'):
                                        file.write(f"\n{message.author.name}({message.author.id}) → {message.content} \n(изображение) {attachment.url}\n")
                            else:
                                file.write(f"\n{message.author.name}({message.author.id}) → {message.content}\n")

                    await channel.send(file=disnake.File(filename))
                    await ticketchannel.delete()
                    print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
                else:
                    interaction.response.send_message("Недостаточно прав.", ephemeral=True)


            elif interaction.component.custom_id == "close_button_WR":
                modal = MyModal()
                await interaction.response.send_modal(modal=modal)
                print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
            
            elif existing_ticket_channels:
                await interaction.response.send_message(content="У вас уже есть активный тикет.", ephemeral=True)
            elif interaction.component.custom_id == "ticket_button_open":

                category = self.bot.get_channel(config['TICKET_CATEGORY'])

                channel = await category.create_text_channel(f"{user}-тикет")
                await interaction.response.send_message(content=f"{channel.mention} - канал обращения создан.", ephemeral=True)

                await channel.send(embed=embed0, components=[button_close_wnr, button_close_wr, button_join_ticket])

                admin_role = interaction.guild.get_role(config['ADMIN_ROLE'])

                everyone_perms = channel.overwrites_for(interaction.guild.default_role)
                everyone_perms.view_channel = False

                creator_perms = channel.overwrites_for(interaction.author)
                creator_perms.view_channel = True

                admin_perms = channel.overwrites_for(admin_role)
                admin_perms.view_channel = True

                await channel.set_permissions(interaction.guild.default_role, overwrite=everyone_perms)
                await channel.set_permissions(interaction.author, overwrite=creator_perms)
                await channel.set_permissions(admin_role, overwrite=admin_perms)

                print(f"{magenta}=======================\n{lye}Button: {interaction.component.custom_id}\nВ канале: {interaction.channel} # {interaction.channel.id}\n{interaction.author} # {interaction.author.id} Нажал кнопку\n{magenta}======================={reset}")
        except Exception as e:
            await interaction.response.send_message(f"Возникла ошибка!\n ```diff\n-{e}\n```\nОбратитесь с описанием проблемы к <@520550728859779072>", ephemeral=True)

def setup(bot):
    bot.add_cog(TICKET(bot))