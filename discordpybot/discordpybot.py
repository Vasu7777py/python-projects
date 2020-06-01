#from discordbot_commands import Commands

import discord

token = "NzE1MDQ3NTI1OTc0ODAyNDQy.Xs3o8A.YapIPaYsOounV-4skUAcXwjKotc"

client = discord.Client()

@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    if (client.user.mentioned_in(message)):
        remove = "<@" + str(client.user.id) + "> "
        Content = (message.content.strip(remove)).lower()
        if (Content == "help"):
            await message.channel.send(f"""{message.author.mention} hi\nhow can i help u""")
            await message.channel.send(f"""commands : \n1> help\n2> show\n3> list\n4> leaderboard""")
        elif(Content.startswith("help")):
            Content = Content.strip("help")
            await message.channel.send(f"""{message.author.mwntion} kk wait a sec""")
            print(Content)
        elif (Content.startswith("hi")):
            await message.channel.send(f"""{message.author.mention} hi\nhow ru doing""")
        else:
            await message.channel.send(f"""{message.author.mention} sorry im in devlopement stage, \nand this command is still not finished try again later""")

client.run(token)
