import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

# Define the intents and ensure they are configured correctly
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


class CommandLister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commandline(self, ctx):
        """Lists all commands of the bot."""
        command_names = [command.name for command in self.bot.commands]
        commands_list = '\n'.join(f'!{name}' for name in command_names)
        await ctx.send(f"Here are the available commands:\n{commands_list}")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.add_cog(CommandLister(bot))


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency}ms')


@bot.command()
async def owner(ctx):
    if ctx.guild is None:
        await ctx.send("This command can only be used in a server.")
        return
    try:
        owner = ctx.guild.owner
        await ctx.send(f'The owner of this server is {owner.mention}')
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for: {reason}')
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to ban members.")


@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked for: {reason}')
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to kick members.")


@bot.command()
@has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name="Muted")

    if not mute_role:
        mute_role = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False, read_message_history=True,
                                          read_messages=True)

    await member.add_roles(mute_role, reason=reason)
    await ctx.send(f'{member.mention} has been muted for: {reason}')


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to mute members.")


bot.run('MTA4NzU0ODM5MDI5MzkxMzYyMQ.GPNJcn.j_JEIBVxKrROfHFrAltDHaEdW2WxUrtMpXskz0')
