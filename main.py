import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = your status and url = your your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "/help | sunflower  ", url = "https://twitch.tv/developer"))



alive.alive()
client.run(os.getenv("TOKEN"), bot=True)