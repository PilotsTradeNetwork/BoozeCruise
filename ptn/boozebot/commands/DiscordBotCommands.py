import sys

from discord.ext import commands


class DiscordBotCommands(commands.Cog):
    def __init__(self, bot):
        """
        This class is a collection of generic blocks used throughout the booze bot.

        :param discord.ext.commands.Bot bot: The discord bot object
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        We create a listener for the connection event.

        :returns: None
        """
        print(f'{self.bot.user.name} has connected to Discord server!')

    @commands.command(name='ping', help='Ping the bot')
    @commands.has_role('Carrier Owner')
    async def ping(self, ctx):
        """
        Ping the bot and get a response

        :param discord.Context ctx: The Discord context object
        :returns: None
        """
        await ctx.send("**PING? PONG!**")

    # quit the bot
    @commands.command(name='exit', help="Stops the bots process on the VM, ending all functions.")
    @commands.has_role('Admin')
    async def exit(self, ctx):
        """
        Stop-quit command for the bot.

        :param discord.ext.commands.Context ctx: The Discord context object
        :returns: None
        """
        await ctx.send(f"k thx bye")
        await sys.exit("User requested exit.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        A listener that fires off on a particular error case.

        :param discord.ext.commands.Context ctx: The discord context object
        :param discord.ext.commands.errors error: The error object
        :returns: None
        """
        if isinstance(error, commands.BadArgument):
            await ctx.send('**Bad argument!**')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("**Invalid command.**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please include all required parameters.** Use b.help <command> for details.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('**You must be a Carrier Owner to use this command.**')
        else:
            await ctx.send(f"Sorry, that didn't work. Check your syntax and permissions, error: {error}")