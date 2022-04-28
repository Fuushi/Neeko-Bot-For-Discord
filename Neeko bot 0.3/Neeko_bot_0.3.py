#when i wrote this program, only god and i know how it works, now only god knows.
#my variable names are not descriptive, half my functions go unused, and you are probly wondering
#why i imported an audio managing module when audio is never touched by the bot
#i am wondering that aswell
#please ignore the racist and offensive variable names, i was likely very frustrated when i wrote them
#have fun reverse engineering the patchwork discord bot
#no i will not refactor this code, ive probly put in over 50 hours working on this bot and a rewrite
#is out of the question at the moment
#if i have open sourced the bot i hope i included atleast basic documentation, in it i probly told you to,
#NEVER TOUCH THE ENCODED_USERNAME VARIABLE, its to late to get rid of it but if you need non-utf8 message contents
#without emojis, there is a function called clean_replace_question(), call that inline when you need to do so, otherwise
#the files are all utf-8 encoded so just pass in the strings you recieve through the discord api

#also dont touch the RGAPI, its a shit show of the highest degree and will break if look at it the wrong way
#regaurds
#--Chase Mattern / Fushi_#6229








#temporary
import user_profile
import audioManager #is included in hierarchy

print(audioManager)

instance1 = audioManager.auGameInstance() #bloat

print(user_profile.profile_manager.generate_user_string('josh#2443', 45, 'weebs')) #bloated startup



#after 3 losses it calls you retarted
#ban teemo mains
import os

from riotwatcher import LolWatcher, ApiError
#import pandas as pd
import json
from json import JSONEncoder
import ast
import random
import multiprocessing as mp #i cant find any calls
import asyncio
import time
from datetime import date
import string
import platform

my_os = platform.system()





## idle RPG like battle mode
## trophies
## easter eggs
## notification sound togglable by combination hotkey


###### Next feature will be role shop
###### add skins
###### finish battles
###### generate splash art with champ skins for battles
###### add free for alls
###### inventories

###### possible uses for gifs
   



## in progress
    #Guild quests
    #watch quest system for bugs

    #rework debug system so commands with the @! modifier are only read by the debug server(s) (think of a way to prevent off by one errors caused by the additional charachter)
        #error fixing ideas here (Code in user profile)
    #fix challenge system
    #make adventures use @ tags

    #allow creation of bot channels to allow advertisements, promptless calls and more
    #make "!start quest" check if you are already in a quest
        #add new quests

        #make guilds more interactive

#fix neeko chat####----------------------------
        #i fixed it but only on live, same with a bunch of other things i cant remember and im going to hate myself for this useless note


def get_key_from_file():
    try:
        with open("key.txt", "r+") as fp:
            return(str(fp.readlines()[0]))
    except:
        return(None)

print("Teemo is god..")

path = r"D:\D drive downloads\Neeko"
#path = r"C:\Users\chase\Desktop\League Tracker\League tracker 0.3\\"
#path = find correct path before pushing to live version
print(path)

global api_key
global custom_message_data
global live_version
live_version = True
global debug_channels
debug_channels = []

custom_message_data = ['globalID: 1000']

api_key = get_key_from_file()
print(api_key, type(api_key))

watcher = LolWatcher(api_key)
my_region = 'na1'
try:
    me = watcher.summoner.by_name(my_region, 'Kikosamadesu')
    print(me)
except:
    print('api key expired')


print()

from riotwatcher import LolWatcher

lol_watcher = LolWatcher(api_key)


# use v5 explicitly
try:
    matchlist = lol_watcher.match_v5.matchlist_by_puuid('AMERICAS', 'n4w9uyietB6qWMNDGfz7zsSWoU0m3vtPNCd-5HLbZxhhRpOXBmVTpOfFpw4L4CPpzGbkmrqgLz0AXw')
    temo = lol_watcher.match_v5.by_id('AMERICAS', matchlist[0])
    print(temo)
    print(matchlist[0])
except:
    print("api key expired") #im pretty sure this will always call expired



list_of_files = []

def load_guild_data_old(): #consolidate load and save functions
    try:
        for i in range(1):
            with open("guilds.txt", "r+") as fp:
                b = json.load(fp)
                print(b)
                print()
                b = b[1:(len(b) - 1)]
                b2 = eval(b)
                print(b2, type(b2))
                return(b2)
    except:
        return([])# fix guild create to allow empty list return

def load_guild_data():
    try:
        file = open("guilds.txt", "r+")
        file_lines = file.readlines()
        live_data = []
        for line in file_lines:
            line = eval(line)
            print(line, type(line))
            live_data.append(line)
        file.close()
        return(live_data) ### look into writelines function https://www.w3schools.com/python/ref_file_writelines.asp
    except:
        return([])

def load_welcomed_user_data():
    try: #change to try:except
        file = open("welcomed_users.txt", "r+")
        file_lines = file.readlines()
        live_data = []
        for line in file_lines:
            line = eval(line)
            #print(line, type(line))
            live_data.append(line)
        file.close()
        return(live_data) ### look into writelines function https://www.w3schools.com/python/ref_file_writelines.asp
    except:
        return([])

def load_known_servers():
    try:
        file = open("servers.txt", "r+")
        file_lines = file.readlines()
        live_data = []
        for line in file_lines:
            line = '"' + line.rstrip() + '"'
            #print(line, type(line))
            line = eval(line)
            #print(line, type(line))
            live_data.append(line)
        file.close()
        return(live_data) ### look into writelines function https://www.w3schools.com/python/ref_file_writelines.asp
    except Exception as error:
        print(error)
        return([])

def save_guild_data_old(Guild_data):
    try:
        print('yes this bit was ripped from github')
        print(type(Guild_data))
        encoded_data = MyEncoder().encode(str(Guild_data)).rstrip()
        print(encoded_data, type(encoded_data))
        with open("guilds.txt", "w+") as fp:
            json.dump(encoded_data, fp)
            print('success')
        return(True)
    except:
        return(False)

def save_guild_data(full_guild_data):
    #
     #
    save_data = []
    for guild in full_guild_data: #might be pointless
        save_data.append(str(guild))
        #print(User)
    file = open("guilds.txt", "w+")
    #print(save_data)
    file.writelines('')
    file.close()

    file = open("guilds.txt", "a")
    #print(file)
    for guild in full_guild_data:
        file.write((str(guild) + '\n'))
    file.close()
    print('     -saving guild_data')
    return(True)
#
def save_welcomed_users(welcomed_users):
    save_data = []
    for welcomed_user in welcomed_users:
        save_data.append(str(welcomed_user))
    file = open("welcomed_users.txt", "w+")
    file.writelines('')
    file.close()
    #
    file = open("welcomed_users.txt", "a")
    for welcomed_user in welcomed_users:
        file.write((str(JSONencode(welcomed_user)) + '\n'))
    file.close()
    print('    -saving welcomed users')
    return(True)

async def phone_home(client, errorMessage, locationTag):
    user = client.get_user(355951979429625862)
    await user.send("--\nPhone home\n" + str(locationTag) + "\nAn error has occured with status:\n" + str(errorMessage))

async def phone_home_announce(client, tag, relevant_data):
    user = client.get_user(355951979429625862)
    await user.send("--\nPhone home anouncment\n" + str(tag) + '\n' + str(relevant_data))



def save_known_servers(known_servers): #use global since this will likely be compared on every message
    #
     #
    
    file = open("servers.txt", "w+")
    #print(save_data)
    file.writelines('')
    file.close()

    file = open("servers.txt", "a")
    #print(file)
    for guild in known_servers:
        print(guild)
        try:
            file.write((str(guild).rstrip() + '\n'))
        except:
            pass
    file.close()
    print('     -saving server_data')
    return(True)
#
def get_voice_line():
    import platform
    my_os = platform.system()
    if str(my_os) == "Windows":
        path = r'C:\Users\chase\source\repos\Neeko bot 0.3\Neeko bot 0.3\neeko'
    else:
        path = r'/home/pi/Desktop/Neekobot/neeko'
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root,file))
    INdex = random.randint(0, len(list_of_files))
    print(list_of_files)
    file_name = list_of_files[INdex]
    return(file_name)

def get_index(author):
    i = 0
    author = str(author)
    # pass in encoded_username
    for container in player_data:
        encoded_data = MyEncoder().encode(str(container[1])).rstrip()
        print(encoded_data, author)
        if encoded_data == author:
            return(i)
        i += 1
    return(None)

def get_guild_index(selected_name):
    JSONencode(selected_name)
    index = 0
    for Guild in guild_data:
        print(Guild[0])
        if selected_name in Guild[0]:
            print(Guild[0], Guild)
            return(index)
        index += 1
    return(None)
    #encode selected name?


def randomString(len):
    output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(len))
    return(output_string)
    pass

def daily_champions(): #make procedural with probabilty weights #[champ, value, level, rarity] (low rarity is rarest)(1-3)
    all_champions = [
        ['aatrox', 15000, 1, 2],
        ['ahri', 10000, 1, 3],
        ['akali', 10000, 1, 3],
        ['akshan', 30000, 1, 1],
        ['alistar', 10000, 1, 3],
        ['amumu', 15000, 1, 2],
        ['anivia', 15000, 1, 2],
        ['annie', 15000, 1, 2],
        ['aphelios', 20000, 1, 1],
        ['ashe', 10000, 1, 3],
        ['aurelion sol', 16000, 1, 1],
        ['azir', 10000, 1, 3],
        ['bard', 15000, 1, 1],
        ['blitzcrank', 10000, 1, 3],
        ['brand', 10000, 1, 2],
        ['braum', 20000, 1, 2],
        ['caitlyn', 15000, 1, 3],
        ['camille', 22000, 1, 3],
        ['cassiopeia', 12000, 1, 3],
        ["cho'gath", 22000, 1, 1],
        ['corki', 15000, 1, 2],
        ['darius', 14000, 1, 3],
        ['diana', 20000, 1, 2],
        ['draven', 500, 1, 1],
        ["dr. mundo", 22000, 1, 1],
        ['ekko', 20000, 1, 2],
        ['elise', 17000, 1, 2],
        ['evelynn', 15000, 1, 2],
        ['ezreal', 10000, 1, 3],
        ['fiddlesticks', 10000, 1, 3],
        ['fiora', 15000, 1, 2],
        ['fizz', 20000, 1, 1],
        ['galio', 10000, 1, 3],
        ['gangplank', 15000, 1, 2],
        ['garen', 10000, 1, 3],
        ['gnar', 15000, 1, 2],
        ['gragas', 15000, 1,2],
        ['graves', 20000, 1, 1],
        ['gwen', 22000, 1, 1],
        ['hecarim', 10000, 1, 3],
        ['heimerdinger', 15000, 1, 2],
        ['illaoi', 20000, 1, 2],
        ['irelia', 20000, 1, 1],
        ['ivern', 10000, 1, 3],
        ['janna', 15000, 1, 2],
        ['jaravan iv', 15000, 1, 2],
        ['jax', 20000, 1, 1],
        ['jayce', 10000, 1, 3],
        ['jhin', 20000, 1, 2],
        ['jinx', 10000, 1, 3],
        ["kai'sa", 12000, 1, 2],
        ['kalista', 10000, 1, 2],
        ['karma', 15000, 1, 2],
        ['karthus', 22000, 1, 1],
        ['kassadin', 15000, 1, 2],
        ['katarina', 15000, 1, 2],
        ['kayle', 20000, 1, 1],
        ['kayn', 10000, 1, 3],
        ['kennen', 18000, 1, 2],
        ["kha'zix", 20000, 1, 1],
        ['kinred', 22000, 1, 1],
        ['kled', 15000, 1, 2],
        ["kog'maw", 15000, 1, 2],
        ['leblanc', 15000, 1, 2],
        ['lee sin', 20000, 1, 1],
        ['leona', 20000, 1, 1],
        ['lillia', 20000, 1, 2],
        ['lissandra', 15000, 1, 2],
        ['lucian', 10000, 1, 3],
        ['lulu', 20000, 1, 2],
        ['lux', 10000, 1, 3],
        ['malphite', 20000, 1, 2],
        ['malzahar', 15000, 1, 2],
        ['maokai', 10000, 1 ,3],
        ['master yi', 20000, 1, 1],
        ['miss fortune', 10000, 1, 3],
        ['mordekaiser', 22000, 1, 1],
        ['morgana', 15000, 1, 3],
        ['nami', 15000, 1, 2],
        ['nasus', 10000, 1, 3],
        ['nautilus', 15000, 1, 2],
        ['neeko', 22000, 1, 1],
        ['nidalee', 10000, 1, 3],
        ['nocturne', 20000, 1, 1],
        ['nunu and willump', 15000, 1, 2],
        ['olaf', 20000, 1, 2],
        ['orianna', 20000, 1, 1],
        ['ornn', 20000, 1, 1],
        ['pantheon', 20000, 1, 1],
        ['poppy', 20000, 1, 2],
        ['pyke', 15000, 1, 2],
        ['qiyana', 15000, 1, 3],
        ['quinn', 10000, 1, 3],
        ['rakan', 15000, 1, 2],
        ['rammus', 15000, 1, 1],
        ["rek'sai", 20000, 1, 1],
        ['rell', 15000, 1, 3],
        ['renekton', 10000, 1, 3],
        ['rengar', 20000, 1, 1],
        ['riven', 20000, 1, 1],
        ['rumble', 20000, 1, 1],
        ['ryze', 10000, 1, 3],
        ['samira', 15000, 1, 2],
        ['sejuani', 10000, 1, 3],
        ['senna', 20000, 1, 2],
        ['seraphine', 10000, 1, 2],
        ['sett', 22000, 1, 1],
        ['shaco', 12000, 1, 3],
        ['shen', 15000, 1, 2],
        ['shyvana', 10000, 1, 3],
        ['singed', 10000, 1, 2],
        ['sion', 20000, 1, 1],
        ['sivir', 15000, 1 ,2],
        ['skarner', 20000, 1, 2],
        ['sona', 10000, 1, 3],
        ['soraka', 10000, 1, 3],
        ['swain', 20000, 1, 1],
        ['sylas', 22000, 1, 1],
        ['syndra', 15000, 1, 2],
        ['tahm kench', 20000, 1, 1],
        ['taliyah', 15000, 1, 2],
        ['talon', 10000, 1, 3],
        ['taric', 10000, 1, 3],
        ['teemo', 10000, 1, 3],
        ['thresh', 10000, 1, 3],
        ['tristana', 15000, 1, 2],
        ['trundle', 10000, 1, 3],
        ['tryndamere', 22000, 1, 1],
        ['twisted fate', 15000, 1, 2],
        ['twitch', 10000, 1, 3],
        ['udyr', 20000, 1, 1],
        ['urgot', 22000, 1, 1],
        ['varus', 10000, 1, 3],
        ['vayne', 10000, 1, 2],
        ['veigar', 20000, 1, 1],
        ["vel'koz", 15000, 1, 2],
        ['vi', 15000, 1, 2],
        ['viego', 22000, 1, 1],
        ['viktor', 10000, 1, 3],
        ['vladimir', 15000, 1, 2],
        ['volibear', 20000, 1, 1],
        ['warwick', 20000, 1, 1],
        ['wukong', 15000, 1, 2],
        ['xayah', 15000, 1, 3],
        ['xerath', 10000, 1, 3],
        ['xhin zhao', 15000, 1, 2],
        ['yasuo', 10000, 1, 2],
        ['yone', 20000, 1, 1],
        ['yorick', 15000, 1, 2],
        ['yuumi', 22000, 1, 1],
        ['zac', 10000, 1, 3],
        ['zed', 10000, 1, 3],
        ['ziggs', 15000, 1, 2],
        ['zilean', 22000, 1, 1],
        ['zoe', 20000, 1, 1],
        ['kadon', 30000, 1, 3],
        ['zeri', 30000, 1, 3]
        ]
    indices = random.sample(range(0, len(all_champions)), 4)
    return([all_champions[indices[0]][0:3], all_champions[indices[1]][0:3], all_champions[indices[2]][0:3], all_champions[indices[3]][0:3]])
   

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

# golbal variables


def check_player_name(player_id, region): # <- should probably allow non- na1 users
    watcher = LolWatcher(api_key)
    my_region = region
    me = watcher.summoner.by_name(my_region, player_id)
    print(me)
    return(me)

def get_puuid(user, region):
    name = user[0]
    watcher = LolWatcher(api_key)
    my_region = region

    me = watcher.summoner.by_name(my_region, name)['puuid']
    return(me)


def daily(last_date, index): #day month year list
    today = date.today()
    new_day = int(today.strftime("%d"))
    new_month = int(today.strftime("%m"))
    new_year = int(today.strftime("%y"))
    if last_date == 'none':
        player_data[index][5] += 300
        player_data[index][6] = [new_day, new_month, new_year]
        return(True)
    if new_year > int(last_date[2]):
        player_data[index][5] += 300
        player_data[index][6] = [new_day, new_month, new_year]
        return(True)
    elif new_month > int(last_date[1]):
        player_data[index][5] += 300
        player_data[index][6] = [new_day, new_month, new_year]
        return(True)
    elif new_day > int(last_date[0]):
        player_data[index][5] += 300
        player_data[index][6] = [new_day, new_month, new_year]
        return(True)
    else:
        return(False)

def new_quest(index_of_user): #add more quests
    index = random.randint(0,9)
    print(index) #make index [1] quest reward

    all_quests = [
        ['greatera 5', 400, 'Get 5 or more assists in 1 game!'],
        ['greatera 7', 500, 'Get 7 or more assists in 1 game!'],
        ['greaterk 5', 300, 'Get 5 or more kills in 1 game!'],
        ['greaterk 7', 400, 'Get 7 or more kills in 1 game!'],
        ['greaterm 15000', 350, 'Deal Greater than 15000 Magic Damage in 1 Game!'],
        ['greaterm 20000', 700, 'Deal Greater than 20,000 Magic Damage in 1 Game!'],
        ['greaterv 15', 300, 'Finish a Game with a Vision Score of 15 or more!'],
        ['greaterv 30', 600, 'Finish a Game with a Vision Score of 30 or more!'],
        ['greatwin', 100, 'Win a game!'],
        ['pentaone', 1000, 'Get a PentaKill!']
        ]
    return(all_quests[index]) #make return index of quest for requirement searching

def quest_check(user, lol_watcher, region): #[(conditional), (start_conditions/date), (description), (tag)]
    def region_conversion(region):
        valid_regions = ['na1', 'eun1', 'euw1', 'la1', 'la2', 'ru1', 'br1', 'tr1', 'jp1', 'kr1', 'pbe']
        americas_regions = ['na1', 'br1', 'la1', 'la2']
        european_regions = ['ru1', 'eun1', 'euw1', 'tr1']
        asian_regions = ['oce', 'oc1', 'jp1']
        if region in americas_regions:
            return('AMERICAS')
        if region in european_regions:
            return('EUROPE')
        if region in asian_regions:
            return('ASIA')
        return('AMERICAS')
    my_region = region_conversion(region)

    quest_data = user[3]
    watcher = LolWatcher(api_key)
    my_region = my_region
    print(api_key)
    print(my_region)
    puuid = watcher.summoner.by_name(region, user[0])['puuid']
    print(puuid)
    recent_match_id = watcher.match_v5.matchlist_by_puuid(my_region, puuid)[0] #something is wrong here
    #temp = watcher.match_v5.matchlist_by_puuid()#missing arguements
    recent_match = lol_watcher.match_v5.by_id(my_region, recent_match_id)
    print(recent_match)
    #print(quest_data)
    return(recent_match)## FIXED AS FUCK BITCHES

async def get_recent_games(user_name, lol_watcher): #[(conditional), (start_conditions/date), (description), (tag)]
    #THIS IS NEVER CALLED AND THAT SCARES ME, either way i made it async so i need to fix any calls i couldnt find

    quest_data = None
    watcher = LolWatcher(api_key)
    my_region = 'na1'
    print(api_key)
    puuid = watcher.summoner.by_name(my_region, user_name)['puuid']
    print(puuid)
    recent_match_id = watcher.match_v5.matchlist_by_puuid('AMERICAS', puuid) #something is wrong here
    print(recent_match_id, len(recent_match_id))

    recent_games_data = []
    recent_games_timestamp = []

    for ID in recent_match_id:
        recent_match = lol_watcher.match_v5.by_id('AMERICAS', ID)
        print(ID)
        recent_games_data.append(recent_match)
        recent_games_timestamp.append(recent_match['info']['gameStartTimestamp'])
    print(recent_games_data)
    print(recent_games_timestamp)

    #temp = watcher.match_v5.matchlist_by_puuid()#missing arguements
    recent_match = lol_watcher.match_v5.by_id('AMERICAS', recent_match_id[0]) #takes index 0(most recent match and gets data)
    print(recent_match)
    #print(quest_data)
    #i might wat to run the data fetch on a separate function since this is going to take a while to pull all data
    #i might be able to await a socket function while a separate script pulls data from the rgapi list
    #it sucks that i have to call the RGAPI twice to get most recent match but thats just their shitty api for you
    return(None)## FIXED AS FUCK BITCHES
#get_recent_games('Kikosamadesu', lol_watcher)
#wait = input()

   # if 'greater' in quest_data[0]:#check damage dealt in last game
       #pass
def JSONencode(data):
    encoded_data = MyEncoder().encode(str(data)).rstrip()
    return(encoded_data)
#message.author is for front end, encoded_username is for backend

def append_file(input_data, file_name_wTxt):
    #
    try:
        save_data = []
        for User in input_data: #simplify because only a string is input
            save_data.append(input_data)
            #print(User)
        file = open(file_name_wTxt, "a")
        #print(file)
        file.write(input_data)
        file.close()
        return(True)
    except:
        print("NON-FATAL FILE ERROR")
        return(False) #might cause problems since i added this without checking references

def save_player_data(player_Data):
    #
    save_data = []
    for User in player_Data:
        save_data.append(str(User))
        #print(User)
    file = open("playerdata.txt", "w+", encoding='utf8')
    #print(save_data)
    file.writelines('')
    file.close()

    file = open("playerdata.txt", "a", encoding='utf8')
    #print(file)
    for user in player_data:
        file.write((str(user) + '\n'))
    file.close()
    print('     -saving player_data')
    return(True)

def call_player_data():
    try:
        file = open("playerdata.txt", "r+", encoding='utf8')
        file_lines = file.readlines()
        live_data = []
        for line in file_lines:
            line = eval(line)
            print(line, type(line))
            live_data.append(line)
        file.close()
        return(live_data) ### look into writelines function https://www.w3schools.com/python/ref_file_writelines.asp
    except Exception as error:
        print(error)
        return([])
    


def get_key_from_input(unparsed_content):#absolutely does not do what it claims to do
    try:
        return(unparsed_content)[1:2] #find correct indices
    except:
        return(None)

def refactor_player_data(data): #i forgor
    pass #


##################3
#discord bot


GUILD = 'Weeb Heaven'
global player_data
global todays_champions
global active_adventures
global active_combat
global accepted_combat
global guild_data
global welcomed_user_data
global queues
global signing_up

todays_champions = daily_champions()
api_key = get_key_from_file()

guild_data = load_guild_data()
active_adventures = []
accepted_combat = []
active_combat = []
queues = []
signing_up = []
welcomed_user_data = load_welcomed_user_data()
player_data = call_player_data()
try:
    player_data = call_player_data()#[('temp', 1, 0.1), ('temp2', 7, 0.4)]
except:
    player_data = []
global user_registration
user_registration = False
print(player_data)
User_signing_up = False

data_list = [(0), (0)]
def clean_replace_question(s): # im pretty sure this just removes emojis from server and channel names, idk why i didnt just reference IDs since these outputs are unusable for frontent anyways
    #to the extent of my knowledge this and its dependancies are only used to print to console without crashing on utf-8, which is cool i guess 
    return ''.join(c if ord(c) < 65536 else '?' for c in s)


import os

import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter


converter = MemberConverter()


#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')




intents=intents=discord.Intents.all()

client=commands.Bot(command_prefix='!',intents=intents)



@client.event
async def on_ready():
    global custom_message_data
    lastRun = 0
    def user_count(client):
       i = 0
       for tGuild in client.guilds:
           for tMember in tGuild.members:
               i += 1
       return(i)
    def server_count(client):
        i = 0
        for tGuild in client.guilds:
            i += 1
        return(i)
    print(f'{client.user.name} has connected to Discord!') # yeah, i wrote this, for sure, -_-
    try:
        #update loop
        while True:
            try:
                if (time.time() - lastRun) >= 86500: #runs every hour (86400)
                    lastRun = time.time()
                    append_file((str(str(server_count(client)) + " : " + str(user_count(client))) + "\n"), "aLogs.txt") #reverse list eventually or smth
                
                    #run code

                ##
                #regular update code
                #runs too often, use time.time()
            except Exception as error:
                print(error)
                await phone_home(client, "handled", "regular updates")
            #updates
            try:
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(str(server_count(client)) + ' Servers'))) #
                await asyncio.sleep(10)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(str(user_count(client)) + ' Users')))
                await asyncio.sleep(10)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Dev Fushi_#6228'))
                await asyncio.sleep(10)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!Neeko Help'))
                await asyncio.sleep(10)
                print(custom_message_data, '--data in on_ready call')
                for i in range(len(custom_message_data) - 1):
                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=custom_message_data[(i + 1)])) ##
                    await asyncio.sleep(10)
            except Exception as error:
                print(error)
                await phone_home(client, 'Handled error', 'status script')
        pass

    except Exception as error:
        #
        #phone home
        try:
            await phone_home(client, error, 'status script') #important code bit
            print('phone home called')
            #phone home attempt
            pass
        except Exception as error2:
            print(error2)
            #this is the desparate contact part of things, maybe initialize a socket to ping my desktop and let me know things are going bad
            pass
        pass


@client.event
async def on_member_join(member):
    global welcomed_user_data
    #print(welcomed_user_data, load_welcomed_user_data(), JSONencode(str(member)), JSONencode(welcomed_user_data[0]))
    match = False
    for Tmember in welcomed_user_data:
        if JSONencode(Tmember) == JSONencode(str(member)):
            match = True
    if match:

        ###############################Use for loop and jsonencode saved data
        #no need to welcome
        print("Match found")
    else:
    #
    
        await member.send('Welcome to the server!')
        print("---member join event flagged")
    
        welcomed_user_data.append(str(member))
        save_welcomed_users(welcomed_user_data) #saves to file

@client.event
async def on_message(message):
    global custom_message_data
    global player_data
    global live_version
    global debug_channels
    global active_combat
    global accepted_combat
    global api_key
    global guild_data
    global welcomed_user_data
    global queues #<- I FUCKING HATE THE INCONSISTANCY OF GLOBALS
    global signing_up


    #ignore IDS
    if str(message.author) == "Save Slot#7493":
        return()





    # <- block end

    if 'linus' in message.content.lower(): #make linus counter, do a simular thing for rick rolls
        try:
            import platform
            if str(platform.system()) == "Windows":
                await message.channel.send("", file=discord.File('linus.jpg')) 
            else:
                await message.channel.send("", file=discord.File('linus.jpeg')) #FILL
            await phone_home_announce(client, "Lins", str(message.author))
        except:
            await phone_home(cliet, 'linus cannot send', 'linus')
            pass


    if '!' in message.content.lower():
        if str(message.author) == "Fushi_#6228":
            if '!exit' in message.content.lower():
                pass #find some way to exit since i cannot crash out

        ############## server, channel log block, could use hella optimizing, loads and saves at every call, calls at every tagged message
        channel_logging = False
        if channel_logging:
            known_servers = load_known_servers()
            current_server = str(message.guild)
            #print(known_servers, current_server)
            if current_server not in known_servers:
                print('---------- new server detected', current_server)
                known_servers.append(str(message.guild))
                save_known_servers(known_servers)
                ####
                await message.channel.send("***Thank you for adding Neeko bot to your server!\n for more info type __!__Neeko help***")
                #keep numbed out until i can fix the error with server logging
                    #steal code from save slot if it keeps causing issues

                ####
            else:
                pass #server known
            pass
        
        
        #
        print(message.content.lower())
        print(debug_channels)

        run_bool, debug_channels = user_profile.profile_manager.debug_verification(message.content.lower(), debug_channels, message.guild) #push to live channel as soon as i get back to ensure call parity\
                #i dont know if this fucker works
        #run_bool = True #temporary constant until i figure out an event flag for debugging
        #print("run bool" + str(run_bool))
        if run_bool == True: #change to ! true for live version #figure it out when compiling live version
            if True: #remove not tag for live version
                #global active_adventures5
                clean_message = clean_replace_question(str(message.content))
                clean_author = clean_replace_question(str(message.author))
                clean_channel = clean_replace_question(str(message.channel))
                clean_guild = clean_replace_question(str(message.guild))
                print(clean_message, '--------', clean_author, clean_channel, clean_guild)
                encoded_username = JSONencode(str(message.author))

                if '!neeko chat' in message.content.lower():
                    fPath = get_voice_line()
                    await message.channel.send("", file=discord.File(fPath)) ####fix neeko shat

                if '!neeko vote' in message.content.lower():
                    await message.channel.send('***https://discordbotlist.com/bots/neeko-bot/upvote***')
                    pass

                if '!neeko bot' in message.content.lower():
                    print(str(message.author))
                    if encoded_username == "Kaiden999\ud83d\udda4#2141":
                        await message.channel.send(r"run Kaiden, I'm in your house")
                    elif str(encoded_username) == 'Fushi_#6228':
                        await message.channel.send('Sup Homie')
                    else:
                        #await message.channel.send('you called?')
                        await message.channel.send('You called?')
                        #await message.channel.send(player_data[0])
                        print('test')
                        print(message.content.lower())

                if '!leaderboard' in message.content.lower():
                    ##### main
                    #loop through player data and create a new array of simple data
                        #this code is going to be very inefficient with large datasets
                    


                    top_10_index = []
                    temp_data = [] #creates sandboxed clone of player data
                    for player in player_data:
                        temp_data.append(player)
                    for i in range(10):
                        if len(temp_data) > 0:
                            largest_score = 0
                            cIndex = 0 #tracks index
                            largest_score_index = 0
                            for player in temp_data: #find largest, remove largest from data, do 10 times
                                if int(player[5]) > largest_score: #create new player_data index to hold a permanent score that does not decrease
                                    #print(largest_score, cIndex)
                                    largest_score = int(player[5])
                                    largest_score_index = cIndex
                                cIndex += 1
                                #print(cIndex)
                            #print(cIndex, largest_score, temp_data)
                            top_10_index.append(temp_data[largest_score_index][0]) #adds top value to top 10
                            temp_data.remove(temp_data[largest_score_index]) #removes top
                            #print(top_10_index) #player data might be globally linked to temp data
                        else:
                            pass
                            #print('no more members')
                        #print(top_10_index)
                    #print('- -')
                    print('top 10 index', top_10_index)
                    user_list = user_profile.profile_manager.list_to_lined_string(top_10_index)
                    sender_message = '***The top 10 Leader board contains:\n' + user_list + '\nCongrats!***'
                    await message.channel.send(sender_message)

                    #front end



                    



                    #


                    pass

                if '!retf' in message.content.lower():
                    if str(message.author) == "Fushi_#6228":
                        #authenticated
                        print("authentication complete")
                        file_name = message.content[6:len(str(message.content))]
                        await message.channel.send(str(file_name))
                        try:
                            file = open("servers.txt", "r+")
                            await message.channel.send("ligma balls", file=discord.File(file_name))
                        except Exception as error:
                            print(error)
                            try:
                                await message.channel.send(str(error, "shits fucked somehow"))
                            except:
                                await message.channel.send("crashed so hard the error logging code crashed")

                    else:
                        await message.channel.send("Authentication Failed")
                    pass

                if '!start adventure' in message.content.lower():
                    #add code to check if already in an adventure(store in player_data for reduced processing times)
                    print(encoded_username)
                    index = get_index(str(encoded_username)) #not sure if encoded_username works in this context on old accounts
                    print(index)
                    if index != 'nil':
                        if player_data[index][8] == 'nil':
                            id = randomString(5).lower() #change range to include other charachters if volume swells to prevent collusion
                            await message.channel.send("***User " + str(message.author) + " has started an adventure,\n to join the adventure type*** !***__join adventure " + str(id) + "__***")
                            print(id)
                            player_data[index][8] = id
                            today = date.today()
                            day = str(int(today.strftime("%d")))
                            month = str(int(today.strftime("%m")))
                            year = str(int(today.strftime("%y")))
                            print(active_adventures)
                            active_adventures.append([id, [str(encoded_username)], [day, month, year], str(int(time.time()))])
                            print(int(time.time()))
                            await asyncio.sleep(30)
                            #contain entire adventure logic within this block
                            #goin to want a code block to send something along the lines of (adventure started) and delete the previous auto message
                            #
                            #get adventure index in globlal list
                            adventure_index = 0
                            for adventurE in active_adventures:
                                if adventurE[0] == id:
                                    break
                                adventure_index += 1
                            preMessage = "__***"
                            for participating_user in active_adventures[adventure_index][1]:
                                print(participating_user)
                                preMessage = preMessage + participating_user + "\n"
                            preMessage = preMessage + "***__"
                            preMessage2 = "***Adventure has begun with user(s)\n***" + preMessage + "\n ***Adventure will end in 24 hours***"
                            await message.channel.send(preMessage2)
                            #
                            # #advenure complete (@ all involved users) (larger groups reward more XP per player) (have XP variable) (offer non XP rewards such as trophies, champions, or exclusive roles)
                            await asyncio.sleep(86400) #86400
                            await message.channel.send("@Fushi_#6228") #finish ****
                            #complete block.
                            for adventure in active_adventures:
                                if adventure[0] == id:
                                    active_adventures.remove(adventure)
                                    print(active_adventures, "yo this is the active shit")
                                    #found adventure
                                    for active_user in adventure[1]:
                                        print(active_user)
                                        active_user_index = get_index(active_user) # make sure its encoded!!!!!!!!!!!
                                        if active_user_index != None:
                                            player_data[active_user_index][5] += 2000 #balance
                                            player_data[active_user_index][8] = 'nil'
                                        else:
                                            await message.channel.send("Something went wrong prolly fucked up encoding")
                                    try:
                                        await message.channel.send("***Adventure with user(s)\n " + preMessage + " has completed, earning members 2000 points each!***")
                                    except:
                                        await phone_home(client, "start adventure crashed", "start adventure")
                                        await message.channel.send("***something! fucked up, DM Fushi_#6228 to report the error***")

                            #

                        else:
                            await message.channel.send("***Player is aleady on an adventure***")
                    else:
                        await message.channel.send("Player is not registered")

                if '!join adventure' in message.content.lower():
                    #add code to check if already in another adventure
                    id = str(message.content.lower()[16:21].lower())
                    player_index = get_index(encoded_username)
                    if player_index != None:
                        if player_data[player_index][8] == 'nil':
                            print(id)
                            index = 0
                            currTime = int(time.time())
                            for adventure in active_adventures:
                                if id == adventure[0]:
                                    if currTime - int(adventure[3]) < 30:
                                        #code block
                                        regi = False
                                        for user in adventure[1]:
                                            if str(encoded_username) == user:
                                                await message.channel.send("***User " + str(message.author) + " is already in the adventure!*** *** ***")
                                                #user already registered
                                                regi = True
                                        if regi == False:
                                            #
                                            await message.channel.send("***User " + str(message.author) + " has joined the adventure***")
                                            #prolly gonna need index of adventure
                                            print(index)
                                            player_data[player_index][8] = id
                                            active_adventures[index][1].append(str(encoded_username))
                                            print(active_adventures[index])  
                                    else:
                                        await message.channel.send("***Adventure is already in progress***")
                                index += 1
                        else:
                            await message.channel.send("***Player is already on an adventure!***")
                    else:
                        await message.channel.send("***Player is not registered!***")

                if '!adventure status' in message.content.lower():
                    index = get_index(encoded_username)
                    print(player_data[index][8])
                    if player_data[index][8] != 'nil':
                        adventure_index = 0
                        for adventure in active_adventures:
                            print(adventure[0], player_data[index][8])
                            if adventure[0] == player_data[index][8]:
                                break
                            adventure_index += 1
                            print(adventure_index)
                        print(active_adventures[adventure_index][3])
                        now = time.time()
                        time_since_start = int(now) - int(active_adventures[adventure_index][3])
                        seconds_remaining = 86400 - time_since_start
                        print(time_since_start, seconds_remaining)
                        #
                        hours_remaining = int(seconds_remaining / 3600)
                        await message.channel.send("***There are " + str(hours_remaining) + " remaining on the adventure!***")
                    else:
                        await message.channel.send("***You are not in an adventure!***")

                if '!neeko help' in message.content.lower():
                    if 'about' in message.content.lower():
                        await message.channel.send("***Welcome to Neeko Bot's help page! \n Neeko Bot is a Discord bot to help you track your league of legends statistics and interact with your friends!*** *** ***")
                        pass
                    elif 'signup' in message.content.lower():
                        await message.channel.send(('***To sign up for Neeko bot league tracker here are a few commands!\n__ -__!__new user <league account region>\n -__!__discord name change <league summoner name>\n -__!__unregister account__***'))
                        pass
                    elif 'levels' in message.content.lower():
                        await message.channel.send('***Level commands:***\n __-my level (league of legends)\n -player card (neeko bot)\n -daily__')
                        pass
                    elif 'quests' in message.content.lower():
                        await message.channel.send("***Take and complete Quests in league of legends to gain rewards perks and bonuses!\n Commands:***\n__ -start quest\n -active quest\n -redeem quest\n -player card__ *** ***")
                        pass
                    elif 'adventures' in message.content.lower():
                        await message.channel.send("***Adventures and group raids are not currently in development, however they will be added in a future update***")
                        pass
                    elif 'champions' in message.content.lower():
                        await message.channel.send("***You can purchase, level, upgrade, and unlock skins for your favorite champions to use in battles!\n Commands:***\n__ -my champions\n -my skins\n -shop__ *** ***")
                        pass
                    elif 'battles' in message.content.lower():
                        await message.channel.send("***You can battle friends and foes with champions collected through quests and rewards!\n Commands:***\n__ -challenge <target>\n -Start free for all\n -join free for all<make channel based?>__ *** ***")
                        pass
                    elif 'shop' in message.content.lower():
                        await message.channel.send("***You can purchase champions, roles, and rewards with points earned through quests and challenges!\n Commands:***\n__ -champion shop\n -role shop\n -player card__ *** ***")
                        pass
                    elif 'guilds' in message.content.lower(): #might cause collision errors with guild flag
                        await message.channel.send("***You can participate in allied guilds to connect with your friends!\n Commands:***\n -__!__Guild create\n -__!__Guild join\n -__!__Guild status\n -__!__Guild rank\n -__!__Guild manage")
                        pass
                    elif 'credits' in message.content.lower():
                        await message.channel.send('***Credits:\n -Pfp: aeriiyu on Instagram\n -Backend: Fushi_#6228\n    chase.mattern on insta***')
                    elif 'add bot' in message.content.lower():
                        await message.channel.send('https://discordbotlist.com/bots/neeko-bot')
                    elif 'queues' in message.content.lower():
                        await message.channel.send('***Queues\n -find queue\n -leave queue\nQueues have a maximum wait time of 1 hour***')
                    elif 'donate' in message.content.lower():
                        await message.channel.send('Bitcoin Address -> bc1qzl27adqtrscp7kgvzzgeud0jmsqd77upg8cpdf \nEtherium -> 0x88D383756e4CB3ede780651135f372E9E0fc6a51\nThanks for your support!')
                    elif 'opg' in message.content.lower():
                        await message.channel.send('***OPG Game\n Join a voice channel and type *!*opg to start a game\nThe game is to guess the anime opening that will play***')
                    else:
                        await message.channel.send("***For more help type !neeko  help <Category>***\n __Categories:\n  -about\n -opg\n  -signup\n -levels\n -quests\n -adventures\n -champions\n -battles\n -shop\n -guilds\n -queues\n -credits\n -add bot\n -Donate!__ *** ***")

                if '!donate' in message.content.lower():

                    await message.channel.send('Bitcoin Address -> bc1qzl27adqtrscp7kgvzzgeud0jmsqd77upg8cpdf \nEtherium -> 0x88D383756e4CB3ede780651135f372E9E0fc6a51\nThanks for your support!')

                if '!new user' in message.content.lower(): #check if user is signed up
                    for user in player_data:
                        if str(user[1]) == str(message.author):
                            user_not_registered = False
                            break
                    else:
                        user_not_registered = True
                            #

       
                    if user_not_registered:
                        #check signing_up list
                        
                        foundSS = False
                        for pp in signing_up:
                            if str(message.author) in pp:
                                foundSS = True

                        if not foundSS:
                            valid_regions = ['na1', 'eun1', 'euw1', 'la1', 'la2', 'ru1', 'br1', 'tr1', 'jp1', 'kr1', 'pbe']
                            
                            selected_region = message.content.lower()[10:len(message.content.lower())] #<- rstrip if invalid
                            if selected_region in valid_regions:

                                signing_up.append([str(message.author), selected_region])
                                await message.channel.send('***Selected region:***' + selected_region + '***\n now to finish sign up please type...\n***!***new user <league name>***')
                                return() #<< carful for continuity errors!
                            else:
                                await message.channel.send('***What region is your league account in?\n !Na1\n !Eun1\n !Euw1\n !La1\n !La2\n !Ru1\n !Br1\n !Tr1\n !Jp1\n !Kr1\n !Pbe\nPlease Type ***!***new user <your region>\nto continue!***')
                                await message.channel.send('err no invalid tag')
                                return()
                        else:
                            ##this is where your name is on the list and you entered a valid name
                            #pull region here and continue runtime
                            for user21 in signing_up:
                                if str(message.author) in user21:
                                    user_region = user21[1]

                                
                               
                            #region finder here
                            


                        try:
                           print('signing up')
                           riot_username = str(message.content)[10:len(message.content)]
                           print()
                           temp1 = message.content
                           print()
                           temp2 = message.author
                           temp3 = (check_player_name(str(message.content[10:len(temp1)]), user_region))
                           player_data.append([temp1[10:len(temp1)], str(temp2), str(temp3['summonerLevel']), [None, None], 'empty', (int(temp3['summonerLevel']) * 300), 'none', [], 'nil', 'nil', user_region])### not debugged
                           print('data handled safely but not yet saved')
                           print(len(str(temp2)))

               
                           print(temp3)
                           riotN = (temp3['name'])
                           save_player_data(player_data) ## it is crashing in save function
                           await message.channel.send("Discord user " + str(temp2) + " registered to riot account " + riotN + " level " + str(temp3['summonerLevel']) + "...")
                           await message.channel.send("To unregister your riot account from your discord account please DM Fushi_#6228 for more details")
                           await phone_home_announce(client, "Sign up", str(temp2)) ## UNTESTED FIX
                        except Exception as error:
                            await phone_home(client, error, 'signup')
                            await message.channel.send('summoner name invalid, err code...')
                            await message.channel.send(str(error))
                    else:
                        await message.channel.send('User already registered')

                if '!discord name change' in message.content.lower():
                    player_index = get_index(encoded_username)
                    if player_index != None:
                        await message.channel.send("***Your name is up to date!***")
                        pass
                    else:
                        entered_leage_id = str(message.content)[20:len(str(message.content))]
                        #await message.channel.send(entered_leage_id)
                        #print(entered_leage_id, len(entered_leage_id))
                        #search for player_data index with matching league account
                        player_index = 0
                        for user in player_data:
                            if user[0].lower() in entered_leage_id.lower():
                                #print("non case match found", player_index)
                                #match at index found
                                old_player_name = player_data[player_index][1]
                                player_data[player_index][1] = eval(encoded_username) # < - i want to test this but i cannot make
                                    #live ignore the test command, if it does it is a destructive change on live, i dont want to plug in my keyboard
                                    #i need to add a debug channel method
                                save_player_data(player_data)
                                await message.channel.send("***User __" + str(old_player_name) + "__ has changed their user name to __" + str(message.author) + "__***")

                                #
                            player_index += 1
                        pass

                if '!unregister account' in message.content.lower():
                    await message.channel.send("***A request has been sent to be manually reviewed\nDM Fushi_#6228 for more***")
                    await phone_home_announce(client, 'unregister', str(message.author))
                    pass

                if '!summoner name change' in message.content.lower():
                    #wait message.channel.send("remember to add backend")
                    user_index = get_index(encoded_username)
                    old_summoner = player_data[user_index][0]
                    inputed_summoner_name = str(message.content)[22:len(str(message.content))]
                    try:
                        region = 'na1' ##ERRPR ERROR BAD FIX FUCK
                        validation = check_player_name(inputed_summoner_name, region)
                        validation = True
                    except Exception as error:
                        validation = False
                        if str(error)[0:20] == (r"404 Client Error: Not Found for url: https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Kikoiihidd")[0:20]:
                            print('expected error, client rejection')
                            await message.channel.send("***Summoner Name is not valid***")
                        else:
                            print('unexpected error', error)
                            await phone_home(client, "rgapi key", "summoner name change")
                            await message.channel.send("***Unknown error: riot probably changed my api key again }:(***\n add error parser Fushi_")
                    if validation:
                        #name change code block
                        #name is verified and index is found
                            #lastly test if new and old names are equal?
                        player_data[user_index][0] = inputed_summoner_name
                        save_player_data(player_data)
                        await message.channel.send("***User __" + str(message.author) + "__ has changed summoner name from __" + str(old_summoner) + "__ to __" + str(inputed_summoner_name) + "!__***")
                        pass
                    #get index
                    #extract inputed summoner name
                    #validate new summoner name
                    #over write summoner name at index
                    #frontent processing

                if '!gif test' in message.content.lower():
                    await message.channel.send("https://tenor.com/view/league-lol-wanna-play-league-riot-games-peanut-butta-man-gif-21327741")
                    pass

                if '!exec' in message.content.lower(): #holy fuck for the love of god remove this soon
                    temp = str(message.content[6:len(message.content)])
                    if str(message.author) == "Fushi_#6228":
                        await message.channel.send("admin command found")
                        try:
                            exec(temp)
                        except Exception as error:
                            await message.channel.send(str(error))
                    else:
                        await message.channel.send("unauthorized user")

                if '!my level' in message.content.lower():
                    #await message.channel.send('you havent added that yet')
                    player_index = get_index(encoded_username)
                    if player_index != None:
                        league_id = player_data[player_index][0]
                        current_level = check_player_name(league_id, player_data[get_index(encoded_username)][10])['summonerLevel']
                        if int(player_data[player_index][2]) < int(current_level):
                            old_level = int(player_data[player_index][2])
                            player_data[player_index][2] = current_level
                            gained_levels = current_level - old_level
                            print(gained_levels)
                            bonus_XP = gained_levels * 500
                            await message.channel.send('You have leveled up!\n __-' + str(bonus_XP) + ' XP reward!__')
                            player_data[player_index][5] += bonus_XP
                            print(len(player_data))
                            await message.channel.send('Leauge of Legends Account ' + player_data[player_index][0] +  ' is level: ' + str(player_data[player_index][2]))
                   
                        else:
                            await message.channel.send('Leauge of Legends Account ' + str(player_data[player_index][0]) +  ' is level: ' + str(player_data[player_index][2]))
                    else:
                        await message.channel.send('User Not Registered')

                if '!player card' in message.content.lower(): #missing backend
                    index = get_index(encoded_username)
                    if index != None:
                        await message.channel.send('You have ' + str(player_data[index][5]) + ' EXP!')
                    else:
                        await message.channel.send('User Not Registered')

                if '!daily' in message.content.lower():
                    ##
                    authorIndex = get_index(encoded_username)
                    if daily(player_data[authorIndex][6], authorIndex):
                        await message.channel.send('__You have recieved 300 XP!__\n   Come again tommorow!')
                    else:
                        await message.channel.send('__Try again tommorow!__\n . . .')

                if '!my champions' in message.content.lower():
                    user_index = get_index(str(encoded_username))
                    Tmessage = ''
                    for champion in player_data[user_index][7]:
                        #print(champion)
                        Tmessage = (Tmessage + ' ' + str(champion[0]) + ', ')
                    Tmessage = Tmessage[0:len(Tmessage) - 2]
                    #print(Tmessage, len(Tmessage))
                    Fmessage = "***Your champions are __" + str(Tmessage) + "__*** *** ***"
                    print(player_data[user_index][7])
                    if player_data[user_index][7] == []:
                        await message.channel.send("***You do not own any champions***")
                    else:
                        await message.channel.send(Fmessage)
     
                if '!champion shop' in message.content.lower(): #owned champions at index 7, 2 degree array content[champion, level, skins]
                    user_index = get_index(str(encoded_username))
                    if user_index == None:
                        await message.channel.send('*** User not registered***')
                        return
                    else:
                        Tmessage = '***purchase the following champions with the !__champion purchase <champion>__ command***\n'
                        #todays_champions
                        champion_message = ("__ -" + str(todays_champions[0][0]) + ' ' + str(todays_champions[0][1]) + "XP\n -" + str(todays_champions[1][0]) + ' ' + str(todays_champions[1][1]) + 'XP\n -' + str(todays_champions[2][0]) + ' ' + str(todays_champions[2][1]) + 'XP\n -' + str(todays_champions[3][0]) + ' ' + str(todays_champions[3][1]) + 'XP__')
                        #make change by day with rarity weighting ^^^^
                        final_message = Tmessage + champion_message
                        await message.channel.send(final_message)
                        pass

                if '!champion purchase' in message.content.lower():
                    user_index = get_index(str(encoded_username))
                    if user_index == None:
                        await message.channel.send("user not registered")
                    else:
                        champion_purchased = False
                        for champion_name in todays_champions:
                            #print(champion_name)
                            if champion_name[0] in message.content.lower():
                                #print(champion_name[0])
                                already_owned = False
                                for owned_champ in player_data[int(user_index)][7]:
                                    #print(champion_name, owned_champ)
                                    if str(owned_champ[0]) == str(champion_name[0]):
                                        already_owned = True
                                        #print('already owned')
                                if already_owned == False:

                                    #print('not owned')
                                    if int(player_data[int(user_index)][5]) > int(champion_name[1]):
                                        #print('enough money')
                                        #purchase block
                                        player_data[int(user_index)][5] -= int(champion_name[1])
                                        player_data[int(user_index)][7].append(champion_name)
                                        champion_purchased = True
                                        await message.channel.send("***User " + str(message.author) + " has purchased " + str(champion_name[0]) + " for " + str(champion_name[1]) + " points***")
                                    else:
                                        #not enough money
                                        await message.channel.send("***Not enough Points!***")
                                        champion_purchased = True
                                else:
                                    await message.channel.send("***You already own this champion!***")
                                    champion_purchased = True
                        #for and if in loop from global todays_champions
                        if champion_purchased == False:
                            await message.channel.send('Champion not for sale')
                            pass
                        pass
                        # get player XP, index, and champion data
                if '!refactor player_data' in message.content.lower():
                    if str(message.author) == 'Fushi_#6228': #make reference external verification script
                        i = 0
                        for player in player_data:
                            player_data[i].append('nil')
                            i += 1
                    save_player_data(player_data)
                    #i dont accually know if this works
                if '!active quest' in message.content.lower():
                    index = get_index(encoded_username)
                    #get user index
                        #sends active quest
                    if index != "None":
                        try:
                            await message.channel.send('Active quest: ' + str(player_data[index][3][0][1])) #?
                        except:
                            await phone_home(client, 'i think you messed up the index fix', 'active quest')
                    else:
                        
                        await message.channel.send('user not registered')
                        i += 1
                    #await message.channel.send('placeholder responce')
                    #get player register index from username

           
                if '!start quest' in message.content.lower():
                    i = get_index(encoded_username)
                    #check if user is registered
                    if i != None:
                        #await message.channel.send('user registered at index: ' + str(i))
                        newQuest = new_quest(player_data[i])
                        player_data[i][3][0] = newQuest
                        await message.channel.send('Your new quest is: ' + str(newQuest[2])) #yeah
                    else:
                        await message.channel.send('user not registered') #ensure function exits
                    #await message.channel.send('placeholder responce, _init_ new quest')

                if '!redeem quest' in message.content.lower(): #need to add backend
                    #
                    #check if previous game has already been used to redeem quest
                    #save last redeemed game ID in user data list index [4]
                    i = get_index(encoded_username)
                    #
                    if i != None:
                        for run1 in range(1):
                            if 'greatera' in str(player_data[i][3][0]):
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                req = (int(player_data[i][3][0][0][8:len(player_data[i][3][0][0])]))
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']:
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']

                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['assists'], req)
                                if int(game['assists']) >= req:
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])

                            elif 'greaterk' in str(player_data[i][3][0]):
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                req = (int(player_data[i][3][0][0][8:len(player_data[i][3][0][0])]))
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']: ## add to other code blocks
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']
                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['kills'], req)
                                if int(game['kills']) >= req:
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])
                            elif 'greaterm' in str(player_data[i][3][0]):
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                req = (int(player_data[i][3][0][0][8:len(player_data[i][3][0][0])]))
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']: ## add to other code blocks
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']
                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['magicDamageDealt'], req)
                                if int(game['magicDamageDealt']) >= req:
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])
                            elif 'greaterv' in str(player_data[i][3][0]):
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                req = (int(player_data[i][3][0][0][8:len(player_data[i][3][0][0])]))
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']: ## add to other code blocks
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']
                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['visionScore'], req)
                                if int(game['visionScore']) >= req:
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])
                            elif 'greatwin' in str(player_data[i][3][0]): #test
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']: ## add to other code blocks
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']
                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['win'])
                                if str(game['win']) == str(True): #test
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])
                            elif 'pentaone' in str(player_data[i][3][0]):
                                puuid = get_puuid(player_data[i], player_data[i][10])
                                req = 1
                                game = quest_check(player_data[i], lol_watcher, player_data[i][10])
                                metadata = game['metadata']
                                info = game['info']
                                participants = info['participants']
                                if player_data[i][4] == metadata['matchId']: ## add to other code blocks
                                    await message.channel.send('You have not met the quest requirements!')
                                    break
                                player_data[i][4] = metadata['matchId']
                 
                                for temp in participants:
                                    game = temp
                                    if temp['puuid'] == puuid:
                                        print('match found')
                                        break
                                print(game)
                                print(game['pentaKills'], req)
                                if int(game['pentaKills']) >= req:
                                    print('success')
                                    await message.channel.send('Your most recent game fullfilled the quest requirements')
                                    await message.channel.send('Your reward is... ' + str(player_data[i][3][0][1]) + ' exp')
                                    player_data[i][5] = int(player_data[i][5]) + int(player_data[i][3][0][1])
                                    player_data[i][3] = [None, None, None]
                                else:
                                    await message.channel.send('You have not fulfilled the quest requirements, to complete this quest: ')

                                    await message.channel.send(player_data[i][3][0][2])
                            else:
                                await message.channel.send('You have no active quests')
                                pass

                   
   
                            #

                            #
                            if str(player_data[i][3]) == None:#### add backed (doesnt work)
                                await message.channel.send('No active quest')
                            else:
                                #check for quest requirements
                                pass
                            break
                        i += 1
                    else:
                        await message.channel.send('user not registered')

                if '!status announce' in message.content.lower():
                    if str(message.author) == "Fushi_#6228":
                        custom_message_data.append(str(message.content.lower()[17:len(message.content)]))
                    else:
                        await message.channel.send("You dont have permission to use this command")

                if '!clear status' in message.content.lower():
                    ## no reply, use status check command 
                    if str(message.author) == "Fushi_#6228":
                        custom_message_data = [custom_message_data[0]]

                if '!nk check status' in message.content.lower():
                    for i in range(len(custom_message_data) - 1):
                        await message.channel.send(custom_message_data[i + 1])
                    await message.channel.send('---')




                if '!guild' in message.content.lower(): #
                    if 'create' in message.content.lower():
                        if player_data[get_index(encoded_username)][9] == 'nil':
                            #user not in any guilds, guild create code block
                            if len(message.content.lower()) > 16:
                                selected_name = message.content[14:len(message.content)]
                                #use for loop to check for selected name in guild data
                                tempBool = load_guild_data()
                                existing_guild = False
                                if tempBool == False:
                                    pass
                                else:
                                    guild_data = tempBool
                                for Guild in guild_data:
                                    if selected_name == 'nil':
                                        existing_guild = True
                                    print(Guild[0])
                                    if selected_name in Guild[0]:
                                        existing_guild = True
                                if existing_guild != True:
                                
                                    appending_data = [selected_name, [[str(message.author), 0, 'nil']], str(message.author), 'nil']
                                    guild_data.append(appending_data)
                                    player_data[get_index(encoded_username)][9] = selected_name
                                    print(save_guild_data(guild_data))
                                    save_player_data(player_data)
                                    #### save guild data to file
                                    await message.channel.send("Guild created")
                                    await phone_home_announce(client, 'guild', str(message.author))
                                    pass
                                else:
                                    await message.channel.send("***A guild already exists with this name!***")
                            else:
                                await message.channel.send("***Please input a valid name.***")
                            pass
                        else:
                            await message.channel.send("***You are already in a guild!***")
                        #await message.channel.send("missing backend")
                        pass

                    if 'join' in message.content.lower():
                        guild_data = load_guild_data()
                        selected_name = message.content[12:len(message.content)].lower()
                        print(len(selected_name))
                        if len(selected_name) < 4:
                            await message.channel.send("***Invalid guild name***")
                        else:
                            player_index = get_index(encoded_username)
                            print(encoded_username, selected_name, guild_data)
                            if player_index != None:
                                guild_index = get_guild_index(selected_name)
                                print(player_data[player_index][9])
                                if 'nil' in player_data[player_index][9]:
                                    print('it went')
                                    if guild_index != None:
                                        data_guild = guild_data[guild_index]
                                        if encoded_username not in data_guild[1][0]: #maybe add [0] tag if it doesnt work
                                            #
                                            await message.channel.send("guild found")
                                            #sub code block
                                            print(encoded_username)
                                            guild_data[guild_index][1].append([str(message.author), 1, 'nil']) #temp list
                                            player_data[player_index][9] = selected_name
                                            save_guild_data(guild_data) #saves guild data to file
                                        else:
                                            await message.channel.send("***You are already in this guild!***")
                                    else:
                                        await message.channel.send("***This guild does not exist!***")
                                else:
                                    print('fucking fuck fuck')
                                    await message.channel.send("***You are already in a guild***")

                                #main code
                            else:
                                await message.channel.send("***User not registered***")
                            #get selected name
                            #await message.channel.send("missing backend")
                            pass
                        print('function execution completed')

                    if 'status' in message.content.lower():
                        player_index = get_index(encoded_username)
                        if player_index != None:
                            if player_data[player_index][9] != 'nil':
                                current_guild_index = get_guild_index(message.content[14:len(message.content)].lower())
                                current_guild_name = guild_data[current_guild_index][0]
                                #
                                temp_index = 0
                                for registered_user in guild_data[current_guild_index][1]:
                                    if registered_user[0] == str(message.author):
                                        guild_data_index = temp_index
                                    temp_index += 1
                                print(guild_data_index)

                                #get guild_data_index
                                #
                                rank = guild_data[current_guild_index][guild_data_index][1]#
                                owner = guild_data[current_guild_index][2]
                                if str(message.author) in owner:
                                    owner_bool = True
                                else:
                                    owner_bool = False
                                other_guild_data = []
                                #Front end
                                await message.channel.send("***You are in the " + str(current_guild_name) + " guild!\n---This guild is owned by " + str(owner) + "!***")


                                #

                            else:
                                await message.channel.send("***You are not in a guild!***")
                        else:
                            await message.channel.send('***You are not registered!, for more info type !Neeko help***')

                    if 'rank' in message.content.lower():
                        ## if owner == str(message.author): You are owner, otherwise you are member rank, more ranks will be added
                        #server owner is stored at index 2
                        player_index = get_index(encoded_username)
                        if player_index != None:
                            if 'nil' not in player_data[player_index][9]:
                                guild_name = player_data[player_index][9]
                                print(guild_name)
                                guild_index = get_guild_index(guild_name)
                                print(guild_index)
                                if guild_index != None: #await an error if not this case
                                    ## main
                                    if str(message.author) == guild_data[guild_index][2]:
                                        #owner
                                        await message.channel.send('***You are the owner!***')
                                    else:
                                        await message.channel.send('***You are a member!***')
                                else:
                                    await message.channel.send('***something went wrong, an error report has already been send to Fushi_#6228***')
                                    #an error report was definitely not sent
                            else:
                                await message.channel.send('***You are not in a guild***')
                        else:
                            await message.channel.send('***You are not registered!, for more info type __!__Neeko help***')
                                    ##
                                #

                        #await message.channel.send('***indev***')
                        pass

                    if 'manage' in message.content.lower():

                        #delete guild, kick members (have the command user @user), transfer ownership (@<user> new owner), check if status is owner
                           #later allow admin ranks to access the kick members command
                        ## if owner == str(message.author): You are owner, otherwise you are member rank, more ranks will be added
                        #server owner is stored at index 2
                        
                        player_index = get_index(encoded_username)
                        if player_index != None:
                            if 'nil' not in player_data[player_index][9]:
                                guild_name = player_data[player_index][9]
                                guild_index = get_guild_index(guild_name)
                                if guild_index != None: #await an error if not this case
                                    ## main
                                    if str(message.author) == str(guild_data[guild_index][2]):
                                        #owner
                                        if 'delete guild' in message.content.lower(): ####WORKS DONT FUCK WITH IT ###WORKS DONT TOUCH FOR THE LOVE OF GOD
                                            ## go through all players' guild data and replace with 'nil'
                                            ## remove guild from guild_data
                                            i = 0
                                            for player in player_data: 
                                                if player[9] == guild_name:
                                                    #player is in target guild
                                                    player_data[i][9] = 'nil'
                                                i += 1
                                            guild_data.remove(guild_data[guild_index]) #potential error point
                                            #save guild data
                                            save_guild_data(guild_data)
                                            await message.channel.send('***Guild deleted successfully***')

                                            pass ####IF YOU BREAK THIS I WILL FUCKING SHIT YOURSELF
                                        elif 'kick member' in message.content.lower():
                                            #@ the member at the end of the message
                                            if '@' not in message.content.lower():
                                                await message.channel.send('***@ the member you intend to kick at the end of your command***')
                                            else:
                                                #!guild manage kick member @ 
                                                    #[28:len(message.content.lower())]
                                                kicked_user_raw = str(message.mentions[0])
                                                kicked_user = str(JSONencode(str(message.mentions[0]))) #works and supports emoji names
                                                kicked_user_index = get_index(kicked_user)
                                                player_data[kicked_user_index][9] = 'nil'
                                                i = 0
                                                for guild_member in guild_data[guild_index][1]:
                                                    if JSONencode(guild_member[0]) in str(kicked_user):
                                                        new_guild_data = []
                                                        i2 = 0
                                                        for guild_user in guild_data[guild_index][1]:
                                                            if i2 != i:
                                                                #add to new data
                                                                new_guild_data.append(guild_user)
                                                            i2 += 1

                                                        guild_data[guild_index][1] = new_guild_data
                                                        print('---------user found and kicked')
                                                        pass
                                                    #print(str(guild_member[0]), str(kicked_user), '--')
                                                    i += 1
                                                    #^not exactly sure why its crashing
                                                await message.channel.send("***User removed from guild!***")

                                            pass ####WORKS DO NOT FUCKING TOUCH
                                        elif 'transfer ownership' in message.content.lower():
                                            #await message.channel.send('***Coming soon!***')
                                            #x = 0 / 0
                                            if '@' not in message.content.lower():
                                                await message.channel.send('***@ the member you intend to transfer ownership to...***')
                                            else:
                                                new_owner_raw = str(message.mentions[0])
                                                new_owner = str(JSONencode(str(message.mentions[0])))

                                                new_owner_index = get_index(new_owner)
                                                #detect if new owner is in guild, compare your player_data[9] to the new owners
                                                if player_data[get_index(encoded_username)][9] == player_data[new_owner_index][9]: #index is returning a none type
                                                    ##new owner is in your guild
                                                    #remove yourself as owner, (keeps you in guild as a member \ admin when they are added)
                                                    guild_data[guild_index][2] = eval(new_owner) #THIS FUCKER IS BREAKING IT
                                                    i = 0
                                                    for guild_member in guild_data[guild_index][1]:
                                                        if guild_member[0] == eval(new_owner):
                                                            print('new owner value updated', i)
                                                            guild_data[guild_index][1][i][1] = 0 #changes rank number to 0
                                                            #new owner found, MAKE SURE THIS ISNT FUCKED
                                                        i += 1
                                                    i = 0
                                                    for guild_member in guild_data[guild_index][1]:
                                                        if guild_member[0] == eval(encoded_username):
                                                            print('new member value updated', i)
                                                            guild_data[guild_index][1][i][1] = 1 #changes rank number to 1
                                                            #new owner found, MAKE SURE THIS ISNT FUCKED
                                                        i += 1

                                                    #promote new owner
                                                    ##
                                            save_guild_data(guild_data)
                                            pass### DOESNT WORK AND I DONT KNOW WHY
                                        else:
                                            await message.channel.send('***Guild manager! to manage your guild, type __!__guild manage <option>!\n -delete guild\n -kick member\n -transfer ownership\n -leave guild (ownership will be transfered to a random member)***')
                                    else:
                                        await message.channel.send('***You dont have permission to manage the guild!***')
                                else:
                                    await message.channel.send('***something went wrong, an error report has already been send to Fushi_#6228***')
                                    print('err--', guild_name, guild_index)
                                    print('guild data corrupted')
                                    #an error report was definitely not sent
                            else:
                                await message.channel.send('***You are not in a guild***')
                        else:
                            await message.channel.send('***You are not registered!, for more info type __!__Neeko help***')
                                    ##
                                #

                        #await message.channel.send('***indev***')
                        pass



                if '!challeng.old' in message.content.lower(): #this is insecure!
                    await message.add_reaction(u'\u2705') #adds confirmation react
                    author = str(message.author)
                    index = get_index(encoded_username)
                    try:
                        target = str(message.mentions[0])
                    except:
                        await message.channel.send('No target detected')
                        return
                    await message.channel.send(str(author) + ' has challenged ' + str(target) + ' to Battle!' )
                    await asyncio.sleep(5) #sleeps without inturupt
                    if int(str(message.reactions)[35]) >= 2: # detect
                        #print(author, target)
                        await message.channel.send(str(target) + ' Has accepted')
                        #code block


                        #
                    else:
                        await message.channel.send('react not found')
                        #rejection block
                if '!challenge' in message.content.lower():
                    author = encoded_username #check if user is already battling someone
                    #await message.channel.send("Chase add the fucking backend you procrastinating shit")
                    #print(message.mentions)
                    if message.mentions != []:
                        target = str(message.mentions[0])
                        encoded_target = JSONencode(target)
                        print(target, '!', encoded_target)
                        #await message.channel.send((target, type(target)))
                        await message.channel.send("***User " + str(message.author) + " has challenged " + target + " to a battle!\n To accept a battle, type __!__accept***")
                        active_combat.append(encoded_target)
                        await asyncio.sleep(20)
                        #combat block
                        print('battle acceptance scan')
                        active_combat.remove(encoded_target)
                        if encoded_target in accepted_combat:
                            #print("target Accepted")
                            accepted_combat.remove(encoded_target)
                            await message.channel.send("***Beggining Battle!***")
                            await asyncio.sleep(10)
                            #combat logic
                            rand_num = random.randint(0,100)
                            if rand_num % 2 == 0:
                                target_index = get_index(encoded_target)
                                player_data[target_index][5] += 100
                                save_player_data(player_data)
                                await message.channel.send("***" + encoded_target + " wins\n    there is a 100 point reward!***")
                                #player 1 wins
                            else:
                                challenger_index = get_index(encoded_username)
                                player_data[challenger_index][5] += 100
                                save_player_data(player_data)
                                await message.channel.send("***" + str(message.author) + " wins\n    there is a 100 point reward!***")
                                #player 2 wins



                            #
                        else:
                            await message.channel.send("***User " + target + " did not accept***")

                    else:
                        await message.channel.send("***You didnt challenge anyone***")

                if '!accept' in message.content.lower():
                    print(encoded_username, active_combat)
                    if encoded_username in active_combat:
                        print('accepted')
                        accepted_combat.append(encoded_username)
                        await message.channel.send("***You have accepted the challenge!***")
                    else:
                        await message.channel.send("***You haven't been challenged to a battle!***")
                    pass


                if '!close' in message.content.lower():
                    temp = message.content[6:len(message.content)]
                    if str(message.author) == "Fushi_#6228":
                        await message.channel.send("dumping global; player_data to JSON Directory")
                        await message.channel.send('Neeko Bot is Now Offline')
                        #
                        #code block
                        save_player_data(player_data)


                        #
                        #
                    else:
                        await message.channel.send("unauthorized user")

                if '!open' in message.content.lower():
                    temp = message.content[6:len(message.content)]
                    if str(message.author) == "Fushi_#6228":
                        await message.channel.send("downloading global; player_data from JSON Directory")
                        await message.channel.send('Neeko Bot is Now Online')
                        #
                        #code block
                        player_data = call_player_data()

                        #
                        #
                    else:
                        await message.channel.send("unauthorized user")

                if '!get activity logs' in message.content.lower():
                    await message.channel.send("Activity logs", file=discord.File('aLogs.txt'))
                    

                if '!generate back door' in message.content.lower():
                    print('generating')
                    if str(message.author) == "Fushi_#6228":
                        for ssssss in client.guilds:
                            try:
                                invite = await ssssss.text_channels[0].create_invite()
                                await message.channel.send(invite)
                            except:
                                await message.channel.send("Permission error")

                if '!generate back 2' in message.content.lower():
                    pass #retired

                if '!live server check' in message.content.lower():
                    ms = ''
                    INT = 0
                    for ssssss in client.guilds:
                        i2 = 0
                        for UUUU in ssssss.members:
                            i2 += 1
                        ms = ms + str(ssssss.name) +  ' ' + str(i2) + '\n'
                        INT += 1
                    await message.channel.send(ms)
                    await message.channel.send("Found Active servers:" + str(INT) + ":")

                if '!live user number check' in message.content.lower():
                    i = 0
                    for tGuild in client.guilds:
                        for tMember in tGuild.members:
                            i += 1
                    await message.channel.send("Neeko bot servers: " + str(i) + " discord users")

                if '!announce outage' in message.content.lower(): ##untested due to its nature
                    if str(message.author) == "Fushi_#6228":
                        await phone_home_announce(client, 'outage announcement', str(message.author))
                        INT = 0
                        for ssssss in client.guilds:
                            if True:
                                try:
                                    print('exclusive server found')
                                    print(ssssss.channels)
                                    tempObject = ssssss.channels[0]
                                    tempObject = tempObject.text_channels[0]
                                    await tempObject.send('***Neeko bot will have a temporary planned outage lasting 1-3 hours, thanks for your patience\nThis is not a regular occurence and you should not expect to see this message again\n DM Fushi_#6228 for details***')
                                    await asyncio.sleep(10)
                                    print('server announced')
                                except Exception as error:
                                    print('announcement failed')
                                    print(error)

                            INT += 1
                        await message.channel.send('Done')
                        print("done")
                        
                    else:
                        await message.channel.send("You dont have permission to use this command")

                if '!full user announcement' in message.content.lower():
                    if str(message.author) == 'Fushi_#6228':
                        await message.channel.send("***You havent coded this yet***")
                    else:
                        await message.channel.send("***You dont have permission to use this command***")
                
                if '!ver' in message.content.lower():

                    await message.channel.send('ver 2.15 LIVE <NEEKO_BOT> FUSHI_#6228\n ***RELEASE BUILD***')

                if '!date initialized' in message.content.lower():
                    await message.channel.send('Placeholder Responce')
                if '!update api key' in message.content.lower():
                    if encoded_username == "Fushi#6228":
                        api_key = message.content[16:len(message.content)]
                        await message.channel.send("API key successfully updated")
                        await phone_home_announce(client, 'API key update', str(message.author))
                    else:
                        await message.channel.send("Unauthorized User")
                    print(message.content[16:len(message.content)])
                if '!pull api key' in message.content.lower():
                    pass
       
                if '!list registered users' in message.content.lower():
                    if str(message.author) == "Fushi_#6228":
                        await message.channel.send("logs printed to console")
                        for i in range(len(player_data)):
                            await message.channel.send(str(player_data[i - 1][0]))
                    else:
                        await message.channel.send("unauthorized user")

                #####Queue finder

                #for queue pool separation add a region check in the search loops
                if '!find queue' in message.content.lower():
                    #add code to check if already in an adventure(store in player_data for reduced processing times)
                    index = get_index(str(encoded_username)) #encoded_username might be reduntand
                    if index != 'None': #only triggers if user is registered, might take None
                        if player_data[index][8] == 'nil': #i believe this checks if you are currently on an adventure, definitely accepts nil
                            id = randomString(5).lower() #--This will be converted to take a random queue, or most filled queue
                            
 
                                #[[users], time_init(ms), region], --remember all users have to be in same region, 
                                    #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]
                            #print(int(time.time())) # <- might work for timeMs

                            #
                            #get adventure index in globlal list <- removed as index will be random, if no queues in region, create queue

                            queue_found = False
                            queue_index = 0
                            i4 = 0
                            already_in_queue = False

                            for queue in queues: #< - have it check if you are already in a queue
                                # goes through all queues
                                my_region = player_data[get_index(encoded_username)][10] #Not sure about this
                                print(my_region)
                                if queue[2] == my_region:
                                    queue_index = i4
                                    queue_found = True
                                    for queue_Member in queue[0]:
                                        if queue_Member[0] == player_data[get_index(encoded_username)][0]: # <- check encoding
                                            already_in_queue = True
                                i4 += 1 #<- might be on wrong indentation, if fucked indent once
                            if already_in_queue:
                                await message.channel.send("***You are already in a queue***") # <- maybe have it update on here
                                return()
                            else:
                                await message.channel.send("***You have joined Queue, estimated time remaining: ***") #---add queue timer estimate, if over a set time change format
                            if queue_found: #true adds you to queue, false creates new queue
                                queues[queue_index][0].append([player_data[get_index(encoded_username)][0], my_region, str(message.author)]) #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]
                                #the code above is long and untested /\ might need to switch to raw-username

                                #send queue members and loop until queue is full or until you leave queue
                                    #front end on leaving queue will be handled on separate function as this will only update every 5 or so seconds
                                members_in_queue = len(queues[queue_index][0])
                                queue_timeout = True
                                preMessage3 = user_profile.profile_manager.list_to_lined_string_modified(queues[queue_index][0])
                                await message.channel.send('Members in queue:\n' + preMessage3) # <- make proper front end handling
                                for i in range(720): #allows an hour while checking every 5 seconds
                                    #check if member is in queue, <- remember to add to join function
                                    left_queue = True
                                    for queueCheckMember in queues[queue_index][0]: # <- in an ideal world if you leave queue this runs through loops and times out
                                        if queueCheckMember[0] == player_data[get_index(encoded_username)][0]: # <- i dont trust this worth shit
                                            left_queue = False
                                    if left_queue:
                                        print('queue leave detected')
                                        queues = user_profile.profile_manager.remove_empty_queue(queues)
                                        return() # <- instead of waiting through remaining loops this just clean fucking kills it
                                    
                                    current_members_in_queue = len(queues[queue_index][0])
                                    if current_members_in_queue != 5: #5 members in queue
                                        if current_members_in_queue != members_in_queue:
                                            #change in member count
                                            #print('change in member count detected on join', current_members_in_queue, members_in_queue)
                                            preMessage3 = user_profile.profile_manager.list_to_lined_string_modified(queues[queue_index][0])
                                            await message.channel.send('Members in queue:\n' + preMessage3) # <- make proper front end handling
                                                #i think i wrote a function for list-string compilation, use that if it exists
                                            members_in_queue = current_members_in_queue
                                    else:
                                        first_run = True
                                        # This runs if full queue
                                        if first_run:
                                            #on full code here
                                            await message.channel.send('You have a full queue' + str(queues[queue_index][0])) # <-make proper front end
                                            first_run = False
                                            queue_timeout = False
                                        else:
                                            pass #runs through all remaining loops instantly




                                    await asyncio.sleep(5)
                                if queue_timeout:
                                    if left_queue == False: # <- should trust but i dont
                                        await message.channel.send('***Queue Timeout***')
                                    queue_index = 0
                                    queue_player_index = 0
                                    i6 = 0 #queue index
                    
                                    for queue in queues: # <- #[[users], time_init(ms), region], --remember all users have to be in same region, 
                                                 #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]
                                        i7 = 0 # <- queue player index
                                        for queue_member in queue[0]:
                                           if queue_member[2] == str(message.author): # <- uses raw data
                                              queue_index = i6
                                              queue_player_index = i7 # <- these values are fucky wucky
                                           i7 += 1
                                        i6 += 1 #queue_index  
                    # remove yourself from queue
                                    new_value = queues[queue_index][0]
                                    new_value.remove(new_value[queue_player_index]) # <- never sure if it uses index or value, im kinda confident in this tho
                                    #print(new_value) # <- remove print statement fucktard
                                    queues[queue_index][0] = new_value


                                    

                                pass
                                #on exit of for loop send time out message
                            else: #creates new queue
                                await message.channel.send('you have joined queue') # <- new frontend fucking needed
                                timeMs = int(time.time()) # <- simple but it hurts my head
                                my_region = player_data[get_index(encoded_username)][10]
                                print(my_region)
                                user_prep = [[player_data[get_index(encoded_username)][0], my_region, str(message.author)]] # <- might need raw-username
                                queue_prep = [user_prep, timeMs, my_region]
                                queues.append(queue_prep) # <- #[[users], time_init(ms), region], --remember all users have to be in same region, 
                                                    #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]

                                #Run same update loop as on join queue
                                members_in_queue = len(queues[queue_index][0])
                                queue_timeout = True
                                for i in range(720): #allows an hour while checking every 5 seconds
                                    try: # <- if this is triggering its prolly cause someone left and in that case its kind working lmao
                                        current_members_in_queue = len(queues[queue_index][0])
                                    except:
                                        return()
                                    left_queue = True
                                    for queueCheckMember in queues[queue_index][0]: # <- in an ideal world if you leave queue this runs through loops and times out
                                        if queueCheckMember[0] == player_data[get_index(encoded_username)][0]: # <- i dont trust this worth shit
                                            left_queue = False
                                    if left_queue:
                                        print('queue leave detected')
                                        queues = user_profile.profile_manager.remove_empty_queue(queues) # <- call might be fucked
                                        return() # <- instead of waiting through remaining loops this just clean fucking kills it


                                    if current_members_in_queue != 5: #5 members in queue
                                        if current_members_in_queue != members_in_queue:
                                            #change in member count
                                            #print('change in member count detected on create', current_members_in_queue, members_in_queue)
                                            preMessage3 = user_profile.profile_manager.list_to_lined_string_modified(queues[queue_index][0])
                                            await message.channel.send('Members in queue:\n' + preMessage3) # <- make proper front end handling
                                                #i think i wrote a function for list-string compilation, use that if it exists
                                            members_in_queue = current_members_in_queue # <- check for spelling
                                            #print(current_members_in_queue, members_in_queue, 'if these are the same im going to be sad')
                                    else:
                                        first_run = True
                                        # This runs if full queue
                                        if first_run:
                                            #on full code here
                                            await message.channel.send('You have a full queue' + str(queues[queue_index][0])) # <-make proper front end
                                            first_run = False
                                            queue_timeout = False
                                        else:
                                            pass #runs through all remaining loops instantly




                                    await asyncio.sleep(5)
                                if queue_timeout:
                                    await message.channel.send('***Queue Timeout***')
                                    queue_index = 0
                                    queue_player_index = 0
                                    i6 = 0 #queue index
                    
                                    for queue in queues: # <- #[[users], time_init(ms), region], --remember all users have to be in same region, 
                                                 #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]
                                        i7 = 0 # <- queue player index
                                        for queue_member in queue[0]:
                                           if queue_member[2] == str(message.author): # <- uses raw data
                                              queue_index = i6
                                              queue_player_index = i7 # <- these values are fucky wucky
                                           i7 += 1
                                        i6 += 1 #queue_index  
                    # remove yourself from queue
                                    new_value = queues[queue_index][0]
                                    new_value.remove(new_value[queue_player_index]) # <- never sure if it uses index or value, im kinda confident in this tho
                                    #print(new_value) # <- remove print statement fucktard
                                    queues[queue_index][0] = new_value


                                    queues = user_profile.profile_manager.remove_empty_queue(queues) # <- call might be fucked
                                pass

                            #notes <- there is neither, leave queue function nor implementation
                if '!leave queue' in message.content.lower(): #user wants to leave queue
                    # so im going to want to find a few key pieces of info
                        #the queues index
                        #the players index in the queue player list
                        #the player name <- easy

                    #and im going to want to remove the player from queues

                    #then lastly im going to need to make the for loops in queue join reconize that you have left
                        #the queue on-update code might cause problems on player leave but im confident it will be fine since its != instead of <

                        # occasionally save
                    queue_index = 0
                    queue_player_index = 0
                    i6 = 0 #queue index
                    
                    for queue in queues: # <- #[[users], time_init(ms), region], --remember all users have to be in same region, 
                                                 #users: [name(or puuid), region, discord_name(utf-8 <- might be able to use raw data)]
                        i7 = 0 # <- queue player index
                        for queue_member in queue[0]:
                            if queue_member[2] == str(message.author): # <- uses raw data
                                queue_index = i6
                                queue_player_index = i7 # <- these values are fucky wucky
                            i7 += 1
                        i6 += 1 #queue_index  
                    # remove yourself from queue
                    new_value = queues[queue_index][0]
                    new_value.remove(new_value[queue_player_index]) # <- never sure if it uses index or value, im kinda confident in this tho
                    #print(new_value) # <- remove print statement fucktard
                    queues[queue_index][0] = new_value
                    queue_remove_index = 0
                    for queue in queues:
                        if len(queue) == 0:
                            queue.remove(queue[queue_remove_index]) # <-- might be fucky wucky, add to queue leave function
                        queue_remove_index += 1
                    await message.channel.send('***You have left Queue***')
                    pass

                ## end of response block
                save_deternimant = random.randint(0,10)
                if save_deternimant == 6:
                    save_player_data(player_data)



 
       
def pull_client_key_from_file():
    try:
        with open("ClientKey.txt", "r+") as fp:
            return(str(fp.readlines()[0]))
    except:
        return(None)

clientKey = pull_client_key_from_file()

client.run(clientKey)






## maybe run level up checker on separate thread


#riotwatcher
#im gonna need a n
#new key probly


#New this patch
   
#GUILD SYSTEM
#RETF SYSTEM
#server networking improved
    #Neeko chat will be fixed
    #improve security
#

#develop a stripped down version of neeko bot with only read functionality for network tests