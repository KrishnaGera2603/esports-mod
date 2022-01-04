import discord
from discord.ext import commands
import json
import os
import asyncio

def get_prefix(bot,message):
    if not message.guild:
        return commands.when_mentioned_or("e.")(bot,message)

    with open("prefixes.json","r") as f:
        prefixes=json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("e.")(bot,message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(f"{prefix}")(bot,message)

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents = discord.Intents.all())
bot.remove_command("help")

@bot.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx,*,prefix):

        with open(r"prefixes.json","r") as f:
            prefixes=json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
       
        with open("prefixes.json","w") as f:
            json.dump(prefixes,f ,indent=4)

            embed=discord.Embed(
            description=f'The prefix is now `{prefix}` for this server.',
            colour=discord.Colour.orange()
            )
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx,error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(
                description="You don't have permission to use this command.",
                colour=discord.Colour.orange()
            )
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(
                description="Error occured, please use the command correctly.",
                colour=discord.Colour.orange()
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MissingRole):
            embed=discord.Embed(
                description="You don't have permission to use this command.",
                colour=discord.Colour.orange()
            )
            await ctx.send(embed=embed)


@bot.command()
async def prefix(ctx):
    pre=ctx.prefix
            
    embed=discord.Embed(
    description=f'''The current prefix is `{pre}`
If u want to change the prefix use command `changeprefix <newprefix>`''',
    colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)








@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity= discord.Activity(type=discord.ActivityType.listening, name="e.help | e.setup"))
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping `{round(bot.latency*1000)}ms`')

@bot.command()
async def botinfo(ctx):
    embed=discord.Embed(
        title='ABOUT ESPORTS MOD',
        description='ESports Mod is a discord bot which is developed for managing tournaments, scrims, moderation and much more!',
        colour=discord.Colour.orange()
    )
    embed.add_field(name='SYSTEM',value=f'<:orangedot:893156901955715113>**Ping -** {round(bot.latency*1000)} ms\n<:orangedot:893156901955715113>**Users -** {len(bot.users)}\n<:orangedot:893156901955715113>**Total Servers -** {len(bot.guilds)}',inline=False)
    embed.add_field(name='DEVELOPER',value='<:mayankpfp:893156858494320690> Mayank#7687',inline=False)
    embed.add_field(name='IMPORTANT LINKS',value='<:orangedot:893156901955715113>[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=878221988714393660&permissions=268757072&scope=bot)\n<:orangedot:893156901955715113>[Support Server](https://discord.gg/XNvqc7we8x)\n<:orangedot:893156901955715113>[Vote](https://top.gg/bot/878221988714393660/vote)\n<:orangedot:893156901955715113>[Github](https://github.com/KrishnaGera2603/esports-mod)',inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/546647317155938304/893530047720349726/1633104534853.png')
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed=discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.add_field(name='ESports Mod Invite Link',value='[Click here to invite the Bot in your server](https://discord.com/api/oauth2/authorize?client_id=878221988714393660&permissions=268757072&scope=bot)',inline=False)
    embed.add_field(name='Support Server',value='[Click here to join Support Server](https://discord.gg/XNvqc7we8x)',inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def reqperms(ctx):
    embed=discord.Embed(
        description="The Bot required following permissions :- `Manage Channels`, `Manage Roles`, `Manage Messages`, `Embed Links`, `Attach Files`, `Add Reactions`, `Use External Emojis`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
async def vote(ctx):
    embed=discord.Embed(
        description="**Vote Now!**\n[Click here to vote for ESports Mod](https://top.gg/bot/878221988714393660/vote)",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N
#M  O  D  E  R  A  T  I  O  N

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx ,member : discord.Member ,*, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server. {reason}')
    await member.send(f"You were kicked from {ctx.guild.name} for {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server. {reason}')
    await member.send(f"You were banned from {ctx.guild.name} for {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    bannedUsers=await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name,user.discriminator) == (name,discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was unbanned.')
            return

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx,member : discord.Member,*,role:discord.Role= None):
    await member.add_roles(role)
    embed=discord.Embed(
        description=f'{member.mention} now have {role.mention}',
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx,member : discord.Member,*,role:discord.Role= None):
    await member.remove_roles(role)
    embed=discord.Embed(
        description=f'Removed {role.mention} from {member.mention}',
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member : discord.Member,*,reason=None):
    guild=ctx.guild
    mutedrole=discord.utils.get(guild.roles, name="Muted by EM")

    if not mutedrole:
        mutedrole=await guild.create_role(name="Muted by EM")

        for channel in guild.channels:
            await channel.set_permissions(mutedrole,speak=False,send_messages=False,read_message_history=True,read_messages=True)
    await member.add_roles(mutedrole)
    embed=discord.Embed(
        description=f"{member.mention} was muted.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    await member.send(f"You were muted in {guild.name} for {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member,*,reason=None):
    role=discord.utils.get(ctx.guild.roles , name="Muted by EM")
    await member.remove_roles(role)
    embed=discord.Embed(
        description=f"{member.mention} was unmuted.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addmassrole(ctx, role: discord.Role, members:commands.Greedy[discord.Member]):
    for m in members:
        await m.add_roles(role)
        await asyncio.sleep(1) 
    embed=discord.Embed(
        description=f"Added {role.mention} to {','.join(m.mention for m in members)}",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removemassrole(ctx, role: discord.Role, members:commands.Greedy[discord.Member]):
    for m in members:
        await m.remove_roles(role)
        await asyncio.sleep(1) 
    embed=discord.Embed(
        description=f"Removed {role.mention} from {','.join(m.mention for m in members)}",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
@commands.is_owner()
async def leave(ctx):
    await ctx.voice_client.disconnect()


# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S
# E S P O R T S       C O M M A N D S

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    role = await ctx.guild.create_role(name="ESports Mod Handler")
    overwrites = {
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
}
    channel = await ctx.guild.create_text_channel(name="esports-mod", overwrites=overwrites)
    await channel.set_permissions(role,read_messages=True)
    embed=discord.Embed(
        title="Setup done!",
        description="**Things created :-**\n<:orangedot:893156901955715113>Created a text channel `esports-mod` do not delete or rename that channel.\n<:orangedot:893156901955715113>Created a role `ESports Mod Handler` do not delete or rename this role.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    embed=discord.Embed(
        title="Welcome to ESports Mod",
        description="**Note :-**\n\n<:orangedot:893156901955715113>Do not delete this channel or the role (ESports Mod Handler) or do not change name of both of these.\n\n <:orangedot:893156901955715113>The Esports commands doesn't work if you delete or rename this channel or the role.\n\n<:orangedot:893156901955715113>If you want any of your staff member to manage or use the esports command give them the role `ESports Mod Handler`.\n\n<:orangedot:893156901955715113>Please use `setup` command only once in your server.\n\n<:orangedot:893156901955715113>Use the `starttourney` command in the channel where you want people to register their teams.\n\n<:orangedot:893156901955715113>All the Future updates of the bot and the commands will appear on this channel.\n\n<:orangedot:893156901955715113>Make sure to [Vote](https://top.gg/bot/878221988714393660/vote) for the ESports Mod and join the [Support Server](https://discord.gg/XNvqc7we8x) for any queries.\n\n<:orangedot:893156901955715113>Thank you very much for using our bot  ~**Mayank#7687**",
        colour=discord.Colour.orange()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/546647317155938304/893530047720349726/1633104534853.png")
    await channel.send(embed=embed)

@bot.command()
@commands.has_role("ESports Mod Handler")
async def idpass(ctx):
    def check(m):
        return m.channel==ctx.channel

    embed=discord.Embed(
        description="Enter the custom room id.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message=await bot.wait_for('message' ,check=check)
    embed=discord.Embed(
        description="Enter the custom room password.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message2=await bot.wait_for('message' ,check=check)
    embed=discord.Embed(
        description="Enter the map name.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message3=await bot.wait_for('message' ,check=check)
    embed=discord.Embed(
        description="Enter the channel id (`for eg - 1234567890`) where u want the bot to send the ID PASS.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message4=await bot.wait_for('message' ,check=check)
    embed=discord.Embed(
        description="Enter the role id (`for eg - 1234567890`) which u want to mention.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message5=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        title='New Custom Room. JOIN NOW!',
        colour=discord.Colour.orange()
    )
    embed.add_field(name="Room ID",value=f"{message.content}",inline=True)
    embed.add_field(name="Password",value=f"{message2.content}",inline=True)
    embed.add_field(name="Map",value=f"{message3.content}",inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text="Autodelete in 30 minutes.")

    channel=bot.get_channel(int(message4.content))
    await channel.send(f'<@&{message5.content}>',embed=embed,delete_after=1800)




@bot.command()
@commands.has_role("ESports Mod Handler")
async def banteam(ctx):
    def check(m):
        return m.channel==ctx.channel
    
    embed=discord.Embed(
        description="Enter the Team Name.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message=await bot.wait_for('message',check=check)

    embed=discord.Embed(
        description="Enter the name or tag of Team IGL.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message2=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter ban duration.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message3=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter the ban reason.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message4=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter the channel id (`for eg - 1234567890`) where you want to send Banned Team message.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message5=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        title='TEAM BANNED',
        description=f'**Team Name :-** {message.content} \n**Team IGL :-** {message2.content} \n**Duration :-** {message3.content} \n**Reason :-** {message4.content}',
        colour=discord.Colour.red()
    )
    channel = bot.get_channel(int(message5.content))
    await channel.send(embed=embed)




@bot.command()
@commands.has_role("ESports Mod Handler")
async def unbanteam(ctx):
    def check(m):
        return m.channel==ctx.channel
    
    embed=discord.Embed(
        description="Enter the Team Name.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message=await bot.wait_for('message',check=check)

    embed=discord.Embed(
        description="Enter the name or tag of Team IGL.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message2=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter the channel id (`for eg - 1234567890`) where you want to send Unbanned Team message.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    message3=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
            title='TEAM UNBANNED',
            description=f'**Team Name :-** {message.content} \n**Team IGL :-** {message2.content}',
            colour=discord.Colour.green()
        )
    channel = bot.get_channel(int(message3.content))
    await channel.send(embed=embed)






@bot.command()
@commands.has_role("ESports Mod Handler")
async def starttourney(ctx):
    def check(m):
        return m.channel==ctx.channel
    
    embed=discord.Embed(
        description="Enter the channel id (`for eg - 1234567890`) where you want to send Confirmed Team Names.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    channelid=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter the role id (`for eg - 1234567890`) which you want to give to the Confirmed Teams.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    roleid=await bot.wait_for('message' ,check=check)

    embed=discord.Embed(
        description="Enter the number of slots in the Tournament. `(Not more than 5000 or less than 1)`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    slots=await bot.wait_for('message' ,check=check)

    channel=bot.get_channel(int(channelid.content))
    role=ctx.guild.get_role(int(roleid.content))

    embed=discord.Embed(
        title="REGISTRATION STARTED",
        description=f"**Total Number of Slots :-** `{slots.content}`\n**Number of Mentions Required :-** `4`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

    bot.to_run = True 

    for message in range(int(slots.content)):
        if bot.to_run is False:
            break

        message=await bot.wait_for('message' ,check=check)
        mentions = message.mentions
        if len(mentions) < 4:
            await ctx.send(f'{message.author.mention} Minimum 4 tags required' ,delete_after=10)
            await message.add_reaction("❌")
        elif mentions[0] != mentions[1] and mentions[1] != mentions[2] and mentions[2] != mentions[0] and mentions[3] != mentions[2] and mentions[3] != mentions[1] and mentions[3] != mentions[0]:
            await message.add_reaction("✅")
            await message.author.add_roles(role)

            embed=discord.Embed(
                title='TEAM REGISTRATION CONFIRMED',
                description=f'**{message.content.splitlines()[0]}**\n** Team Players :-** {mentions[0]}, {mentions[1]}, {mentions[2]}, {mentions[3]}',
                colour=discord.Colour.orange()
            )
            await channel.send(f'{message.author.mention}',embed=embed)

    embed=discord.Embed(
        description="**__REGISTRATION CLOSED__**",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)




@bot.command()
@commands.has_role("ESports Mod Handler")
async def endtourney(ctx):
    bot.to_run = False

#help command

#help command


#help command



#help command



#help command



@bot.group(invoke_without_command=True)
async def help(ctx):
    pre=ctx.prefix
    embed=discord.Embed(
        title="Help & Support",
        description=f"First type `{pre}setup` to enable all the esports commands in your server (for more information use {pre}help setup).",
        colour=discord.Colour.orange()
    )
    embed.add_field(name="Information",value="`ping`, `botinfo`, `prefix`, `vote`, `invite`, `reqperms`",inline=False)
    embed.add_field(name="Moderation",value="`clear`, `kick`, `changeprefix`, `ban`, `unban`, `mute`, `unmute`, `addrole`, `removerole`, `addmassrole`, `removemassrole`",inline=False)
    embed.add_field(name="ESports",value="`idpass`, `banteam`, `unbanteam`, `starttourney`, `endtourney`",inline=False)
    embed.add_field(name="Important Links",value="[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=878221988714393660&permissions=268757072&scope=bot) | [Support Server](https://discord.gg/XNvqc7we8x) | [Vote](https://top.gg/bot/878221988714393660/vote)",inline=False)
    embed.set_footer(text=f"Use {pre}help <command> for more information about that command.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/546647317155938304/893530047720349726/1633104534853.png")
    await ctx.send(embed=embed)

@help.command()
async def ping(ctx):
    embed=discord.Embed(
        description="Gives you the bot latency.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def botinfo(ctx):
    embed=discord.Embed(
        description="Gives you the information about the bot and the system and also name of the developer(Mayank#7687)",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def prefix(ctx):
    embed=discord.Embed(
        description="Gives you the current prefix of the bot if u want to change the prefix use command `changeprefix`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def invite(ctx):
    embed=discord.Embed(
        description="Gives you the link through which you can invite ESports Mod to your server.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
    embed=discord.Embed(
        title="Command : Clear",
        description="**Description :** Deletes the message more than 1.\n**Usage :** `clear <messageamount>`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def kick(ctx):
    embed=discord.Embed(
        title="Command : Kick",
        description="**Description :** Kicks a member from the server. \n**Usage :** `kick @MemberMention <reason>`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def changeprefix(ctx):
    embed=discord.Embed(
        title="Command : Changeprefix",
        description="**Description :** Changes the prefix of the bot. \n**Usage :** `changeprefix <newprefix>`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def ban(ctx):
    embed=discord.Embed(
        title="Command : Ban",
        description="**Description :** Bans a member from the server.  \n**Usage :** `ban @MemberMention <reason>`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def unban(ctx):
    embed=discord.Embed(
        title="Command : Unban",
        description="**Description :** Unbans a member from the server.  \n**Usage :** `unban MemberName#MemberTag`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def mute(ctx):
    embed=discord.Embed(
        title="Command : Mute",
        description="**Description :** Don't allow member to chat or speak.  \n**Usage :** `mute @MemberMention <reason>`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def unmute(ctx):
    embed=discord.Embed(
        title="Command : Unmute",
        description="**Description :** Allow muted person to chat and speak.\n**Usage :** `unmute @MemberMention`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def addrole(ctx):
    embed=discord.Embed(
        title="Command : Addrole",
        description="**Description :** Give the mentioned member a role. \n**Usage :** `addrole @MemberMention @RoleMention`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def removerole(ctx):
    embed=discord.Embed(
        title="Command : Removerole",
        description="**Description :** Removes the role from the mentioned member. \n**Usage :** `removerolerole @MemberMention @RoleMention`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def idpass(ctx):
    embed=discord.Embed(
        title="Command : Idpass",
        description="**Description :** Sends the id pass of the custom room in a specific channel. \n**Usage :** `idpass`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def banteam(ctx):
    embed=discord.Embed(
        title="Command : Banteam",
        description="**Description :** Sends a message with team name and team leader who got a ban from matches. \n**Usage :** `banteam`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def unbanteam(ctx):
    embed=discord.Embed(
        title="Command : Unbanteam",
        description="**Description :** Sends a message with team name and team leader who got unbanned from mathces. \n**Usage :** `unban`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def starttourney(ctx):
    embed=discord.Embed(
        title="Command : Starttourney",
        description="**Description :** Start tournament registration `Use this command in the channel where you want people to register.`. \n**Usage :** `starttourney`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def endtourney(ctx):
    embed=discord.Embed(
        title="Command : Endtourney",
        description="**Description :** Stops all the running tournaments in the server. \n**Usage :** `endtourney`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def addmassrole(ctx):
    embed=discord.Embed(
        title="Command : Addmassrole",
        description="**Description :** Give a role to all the mentioned members. \n**Usage :** `addmassrole @RoleMention @Member1Mention @Member2Mention @Member3Mention ...`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def removemassrole(ctx):
    embed=discord.Embed(
        title="Command : Removemassrole",
        description="**Description :** Removes a role from all the mentioned members. \n**Usage :** `removemassrole @RoleMention @Member1Mention @Member2Mention @Member3Mention ...`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def setup(ctx):
    embed=discord.Embed(
        title="Command : Setup",
        description="**Description :** Creates a channel and a role which is important to run this bot.\n**Permissions :** The member require Admin perms to run this command, Bot required perms you can check using `reqperms` command.\n**Usage :** `setup`",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def reqperms(ctx):
    embed=discord.Embed(
        title="Command : Reqperms",
        description="**Description :** Gives you the list of permissions that bot required.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)

@help.command()
async def vote(ctx):
    embed=discord.Embed(
        title="Command : Vote",
        description="**Description :** Gives you the link where you can vote our bot.",
        colour=discord.Colour.orange()
    )
    await ctx.send(embed=embed)
    
bot.run(${{secret.myToken}})
