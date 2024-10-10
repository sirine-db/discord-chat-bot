from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents,Client,Message
from responses import get_response

#STEP0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
#print (TOKEN)

#STEP 1: BOT SETUP

intents: Intents= Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

#STEP2: MSG FUNC

async def send_message(message: Message,user_message: str) -> None:
    if not user_message:
        print('(Message was empty bcs intents were not enables probably)')
        return
        
    if is_private :=user_message[0] == '?':      # to response in private
        user_message= user_message[1:]
    try :
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await  message.channel.send(response)
    except Exception as e:
        print(e) 

#STEP 3: HANDLING THE START UP FOR MY BOT

@client.event
async def on_ready()-> None:
    print(f'{client.user} is nowrunning! ')

#STEP 3: HANDLING INCOMING MSG
@client.event
async def on_message (message: Message) -> None:
    if message.author == client.user:
        return # to be sure that the bot doesnt response to himself
    username : str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print (f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#STEP 5: MAIN 
 
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()