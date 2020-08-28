from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.content.startswith('!shorturl'):
        embed = discord.Embed()
        embed.set_author(name="短縮URLにしたよ", url="https://google.com")
        embed.add_field(name="undefined", value="undefined", inline=False)
        await self.bot.say(embed=embed)
bot.run(token)
