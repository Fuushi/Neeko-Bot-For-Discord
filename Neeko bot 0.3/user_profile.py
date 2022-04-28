import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageEnhance

print(PIL, Image)

class profile_manager(object):
    def generate_user_string(name, level, guild):
        #temp test code block



        #wait = input()
        pass
    def debug_verification(message_contents, debug_guild_list, guild): #true return runs this, fatman is the only debug channel under these circumstances, bring back debug channels but use files for persistance
        #Try to keep io time down on debug verification, thus this will be the short term performant option even if it makes development mildly harder
        if '!debug guild' in message_contents:
            if guild not in debug_guild_list:
                debug_guild_list.append(guild)
                return(True, debug_guild_list)
            #else its already a debug channel
        if '!live guild' in message_contents:
            if guild in debug_guild_list:
                debug_guild_list.remove(guild)
                return(True, debug_guild_list)
        if guild not in debug_guild_list:
            return(True, debug_guild_list) # < - Not tested but i already feel like a genuis for this
        return(False, debug_guild_list)
        #remember the implementation in live

        

        #create a list of disabled channels and store it in ram
            #as soon as i push this to live i can fix the discord name change feature

    def admin_authenticator(message_author): #do not encode, encoding will be done on the fly as needed
        #make reference a file admins.txt perhaps allow addition of new admins over the air, hard code my name as full power.
        return(True) #bruh

    def list_to_lined_string(leaderboard):
        lined_string = ''
        for leader in leaderboard:
            lined_string = lined_string + (leader + '\n')
        lined_string.rstrip()
        lined_string = lined_string[0:(len(lined_string) - 2)]
        return(lined_string)

    def list_to_lined_string_modified(leaderboard):
        lined_string = ''
        for leader in leaderboard:
            lined_string = lined_string + (leader[2] + ' : ' + leader[0] + '\n')
        lined_string.rstrip()
        lined_string = lined_string[0:(len(lined_string) - 2)]
        return(lined_string)

    def remove_empty_queue(queues_data): # <- takes queues but goes under different varaiable name to prevent global occlusion
        removal_index = 0
        for queue in queues_data:
            if len(queue[0]) == 0:
                print('removing empty queue')
                queues_data.remove(queues_data[removal_index]) # <- removes a maximum of 1 empty queue per run
                return(queues_data)

            removal_index += 1

        return(queues_data)

    def server_log(messageguild):
        #open from file, this will cause considerably increased io time but it is allows it to take only 1 line to implement on the on_message function

        def save_guild_data(full_guild_data):
            save_data = []
            for guild in full_guild_data: #empties the file
                save_data.append(str(guild))
            file = open("servers.txt", "w+")
            file.writelines('')
            file.close()
            file = open("servers.txt", "a")
            for guild in full_guild_data: #fills the file with new data
                file.write((str(guild) + '\n'))
            file.close()
            return(True)
        def load_known_servers():
            try:
                file = open("servers.txt", "r+")
                file_lines = file.readlines()
                live_data = []
                for line in file_lines:
                    line = '"' + line.rstrip() + '"'
                    line = eval(line)
                    live_data.append(line)
                file.close()
                return(live_data) ### look into writelines function https://www.w3schools.com/python/ref_file_writelines.asp
            except Exception as error:
                pass
        known_servers = load_known_servers()
        if str(messageguild) not in known_servers:
            print('new server!') #if it returns true you would want to respond with a message asking a user for adding the bot to their server
            known_servers.append(str(messageguild))
            save_guild_data(known_servers)
            return(True)
        else:
            return(False)

# >> inline implementation >> server_log(str(message.guild))

