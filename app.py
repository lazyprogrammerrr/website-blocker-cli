'''
    #IMPORTANT
    - YOU WILL NEED ADMIN PERMISSION TO ACCESS HOST FILE IN WINDOWS AND FOR LINUX or MAC 'SUDO'
    - YOU NEED TO CREATE A FILE WITH ALL THE SITES YOU WANT TO BLOCK FOR CERTAIN TIME.
'''


#IMPORTING MODULES
import time
from datetime import datetime as dt

#redirecting to 127.0.0.1 and HOST FILE PATH FOR WINDOWS
redirect = '127.0.0.1'
host_file = r'C:\Windows\System32\drivers\etc\hosts'


# host_file = 'hosts_temp'                                     #------>       FOR DEBUGGING! YOU HAVE TO CREATE A TEMP HOST FILE YOU CAN NAME IT ANYTHING
# websites= ['www.facebook.com','facebook.com']                #------>       YOU CAN ALSO HARDCODE WEBSITES IN SCRIPTS ITSELF


#AUTO BLOCKER FUNCTION
def auto_blocker():
    while True:
        path = input("ENTER PATH HERE FOR YOUR WEBSITES LIST FILE -> ").replace('"','')         #------>    ASKING USER FOR WEBSITE LIST TEXT FILE PATH
        try:
            with open(path,'r') as f:
                websites = f.readlines()
                break
        except FileNotFoundError:
            print("\nNo Such File or Directory Found! Please Check Again.\n")                     #------>    HANDLING [ERROR2]

    print("\nENTER TIME IN 24-HOURS CLOCK FORMAT!")
    while True:
        try:
            from_time = int(input("\nEnter (From) Time Here -> "))                              #------>    ASKING USER FOR TIME (FROM) FOR EXAMPLE 12-15 (12)
            if (from_time > 23):                                                                #------>    IF USER ENTERS TIME GREATER THAN 23 THIS WILL THROW ERROR!
                print("\nWRONG TIME! PLEASE ENTER BETWEEN 00-23 (24-HOURS CLOCK FORMAT)")
            else:
                break
            # exit()
        except Exception as e:                                                                  #------>    PRINTING EXCEPTION AS IT IS
            print(e)

    while True:
        try:
            to_time = int(input("\nEnter (To) Time Here -> "))
            if (to_time > 23):
                print("\nWRONG TIME! PLEASE ENTER BETWEEN 00-23 (24-HOURS CLOCK FORMAT)")
            else:
                break
        except Exception as e:
            print(e)

#MAIN TRY BLOCK

    try:
        while True:
            if dt(dt.now().year,dt.now().month,dt.now().day,from_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,to_time):   #------>    COMAPARING TIME
                with open(host_file,'r+') as f:                                                 #------>    OPENING HOST FILE
                    content = f.read()                                                          #------>    READING CONTENTS HERE
                    for website in websites:                                                    #------>    LOOPING THROUGH WEBSITE LIST TEXT FILE
                        if website in content:                                                  #------>    IF CONTENT IS ALREADY PRESENT IN HOST FILE DO NOTHING!
                            pass
                        else:                                                                   #------>    ELSE WRITE CONTENT IN HOST FILE
                            f.write(redirect +" "+website+"\n")
                print('\nSites Blocked!\n')
            else:                                                                               #------>    THIS BLOCK WILL EXECUTE WHEN GIVEN TIME IS OVER
                with open(host_file,'r+') as f:
                    content = f.readlines()
                    f.seek(0)                                                                   #------>    SEEKING CURSOR TO STARTING
                    for line in content:
                        if not any(webiste in line for webiste in websites):                    #------>    IF ANY WEBSITE EXISTS IN HOST FILE
                            f.write(line)
                        f.truncate()                                                            #------>    REMOVING WEBSITES FROM HOST FILE
                print('\nNow You Can Access Blocked Sites!\n')
                exit()
            time.sleep(360)                                                                     #------>    SLEEPING FOR 5 MINUTES YOU CAN CHANGE VALUE
    except PermissionError as e:
        print("\n",e,"\n\nYOU NEED ADMIN PRIVILEGE TO ACCESS THIS FILE (RUN THIS SCRIPT AS ADMIN)")
    except Exception as e:
        print("\n Some Error Occured\n",e)

#STOP FUNCTION
#THIS WILL STOP THE SCRIPT IN BETWEEN GIVEN HOURS BY REMOVING WEBSITES FROM HOST FILE
def stop_script():
    while True:
        path = input("ENTER PATH HERE FOR YOUR WEBSITES LIST FILE -> ").replace('"','')
        try:
            with open(path,'r') as f:
                websites = f.readlines()
                break
        except FileNotFoundError:
            print("\nNo Such File or Directory Found! Please Check Again.")
    
    try:
        with open(host_file,'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(webiste in line for webiste in websites):
                    f.write(line)
                f.truncate()
            print('\nNow You Can Access Blocked Sites!\n')
            time.sleep(2)
    except PermissionError as e:
        print("\n",e,"\n\nYOU NEED ADMIN PRIVILEGE TO ACCESS THIS FILE (RUN THIS SCRIPT AS ADMIN)")
    except Exception as e:
        print("\n Some Error Occured\n",e)

#MAIN FUNCTION

if __name__ == '__main__':
    print("WELCOME TO WEBSITE BLOCKER!\n")
    print("Press (CTRL + C) TO Go BACK IN MENU.")
    while True:
        print('''\nOPTIONS:
                1. PRESS 1 or (AUTO) TO BLOCK AND UNBLOCK SITES AUTOMATICALLY
                2. PRESS 2 or (STOP) TO STOP THE SCRIPT
                3. PRESS 3 or (EXIT) TO EXIT THE SCRIPT''')
        option_input = input("\nTYPE OPTIONS HERE -> ").casefold()

        if option_input == '1' or option_input == 'AUTO'.casefold():
            auto_blocker()
        elif option_input == '2' or option_input == 'STOP'.casefold():
            stop_script()
            exit()
        elif option_input == '3' or option_input == 'EXIT'.casefold():
            print("THANK YOU FOR USING THIS SCRIPT.")
            time.sleep(2)
            exit()
        else:
            print("\nWRONG OPTION SELECTED! PLEASE SELECT FROM THE GIVEN OPTIONS ONLY!")
            time.sleep(1)