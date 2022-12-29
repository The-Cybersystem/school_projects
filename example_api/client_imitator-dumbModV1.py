import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix = '!!', intents = intents)
bad_words = []
exclusions = []
autoMod_allowed = []

@client.event
async def on_ready():
    print(f"Logged in as {client.user} with ID: {client.user.id}!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency)*1000}ms")

#@client.event
#async def on_message(message):
#    print(f"{message.guild}: {message.channel}: {message.author}: {message.content}")

@client.command()
async def autoMod(ctx, which_list, mode, word):
    user_id = str(ctx.author.id)
    if user_id != client.user.id:
        for allowed_user_id in autoMod_allowed:
            if user_id == allowed_user_id:
                if mode == 'add':
                    if which_list == 'bad words' or which_list == 'blacklist':
                        bad_words.append(word.lower())
                    elif which_list == 'exclusions':
                        exclusions.append(word.lower())
                    else:
                        await ctx.send("Use `blacklist` or `exclusions` for which_list in `!!autoMod which_list mode word`")
                elif mode == 'remove' or mode == 'delete':
                    if which_list == 'bad words' or which_list == 'blacklist':
                        bad_words.remove(word.lower())
                    elif which_list == 'exclusions':
                        exclusions.remove(word.lower())
                    else:
                        await ctx.send("Use `blacklist` or `exclusions` for which_list in `!!autoMod which_list mode word`")
                else:
                    await ctx.send("Make sure `mode` is 'add' or 'remove' in `!!autoMod which_list mode word`")
            else:
                ctx.send("You can't touch the auto mod. This has been logged.")
                webhook_url = os.environ['Invalid_User_Log']
                payload = (f"Violation @ {ctx.guild}: {ctx.channel}: {ctx.author}: {ctx.content}.")
                webhook = DiscordWebhook(url=webhook_url, content=payload)
                response = webhook.execute()
                if response:
                    print(response)
                else:
                    print("Something went wrong with the **invalid user log webhook**.")
    else:
        pass


    '''#IF USER IS allowed
        IF mode = add
            #add word/exclusion
        ELSE IF mode = remove
            #remove word/exclusion
        ELSE
            
    #ELSE
        #say "You don't have perms to run that command." 
        ##log use who executed command
    '''
    

load_dotenv()
client.run(os.getenv('TOKEN'))
