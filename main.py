import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents, application_id=appid)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected.")

@bot.command(name="hello", help="hello!")
async def hello(ctx):
  ctx.reply("hello, world")

bot.run("token")
