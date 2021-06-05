from ptn.boozebot.commands.DatabaseInteraction import DatabaseInteraction
from ptn.boozebot.commands.DiscordBotCommands import DiscordBotCommands
from ptn.boozebot.commands.Helper import Helper
from ptn.boozebot.commands.Unloading import Unloading
from ptn.boozebot.constants import bot, TOKEN, _production
from ptn.boozebot.database.database import build_database_on_startup

print(f'Booze bot is connecting against production: {_production}.')


def run():
    """
    Logic to build the bot and run the script.

    :returns: None
    """
    build_database_on_startup()
    bot.add_cog(DiscordBotCommands(bot))
    bot.add_cog(Unloading())
    bot.add_cog(DatabaseInteraction())
    bot.add_cog(Helper())
    bot.run(TOKEN)


if __name__ == '__main__':
    run()
