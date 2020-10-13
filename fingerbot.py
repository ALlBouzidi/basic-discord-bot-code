import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="")

rules = [" Please be tolerant towards each other. Even if you don't like someone, please go to another channel! You shouldn't stress yourself or others. \n- Do not insult anyone's feelings \n- Do not ignite conflict \n- Apologize if you created any sort of conflict. We are all human beings, we tend to get carried away, you must acknowledge your mistakes!"," Feel free to complain to admins (& about admins), we will sort everything out. \n!!! A personal request - do not spam channels that are not designed for this. My eyes and soul scream in terror when they see this mess."," If there isn't enough channels for some conversations - we will create them, just write us in #❓│sᴜɢɢᴇsᴛɪᴏɴs. (Or any other suggestions)"," If you want others to know more about you, introduce yourself in #📱│sᴇʟғ-ᴘʀᴏᴍᴏᴛɪᴏɴ."," If you want to get a role, please, check the roles above or write to one of the heads (@deleted-role @Pussy power @The best 👑)."," If you want to become an admin, you must earn our trust."," If you want to teach lessons on philosophy, languages, anything - no problem. Feel free to write to @Pussy power","Use #💢│sᴘᴀᴍ  to share links!!"]

@client.event
async def on_ready():
	print("Bot is ready")


@client.command()
async def finger(ctx):
	await ctx.send("don't talk to me bish")

@client.command()
async def hi(ctx):
	await ctx.send("No")

@client.command()
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','finga'])
async def _8ball(ctx,*, question):

	responses = ["Yes",
				 "No",
				 "No... I mean yes... Well... Ask again later",
				 "The answer is unclear... Seriously I double checked",
				 "It's a coin flip really...",
				 "Yes, he will... Sorry I wan't really listening",
				 "I could tell you but I'd have to permanently ban you",
				 "Yes, No, Maybe... I don't know, could you repeat the question?",
				 "Do you REALLY want me to answer that? OK... Maybe ",
				 "YesNoYesNoYesNoYesNoYesNo "
				 "Ask yourself this question in the mirror three times, the answer will become clear ",
				 "You want an answer? OK, here's your answer: "]
	await ctx.send(f'{random.choice(responses)}')



client.run("NzY1MjMwNDg1NDUwMjYwNTMw.X4RybQ.TnqHju1dcQzyLxaCKfQACyqC21U")
