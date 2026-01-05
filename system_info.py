import os
import sys
import json
from datetime import datetime
from pystyle import Colorate, Colors
from colorama import Fore
import getpass
import socket

os.system("title System Tool")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def log(message):
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def get_info():
    return {
        "user": getpass.getuser(),
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": sys.platform,
        "path": os.getcwd(),
        "files_count": len(os.listdir()),
        "python_version": sys.version,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

def show_info():
    info = get_info()
    for k, v in info.items():
        print(f"{k}: {v}")
    log("INFO DISPLAYED")

def save_info():
    info = get_info()
    filename = f"info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(info, f, indent=4)
    log(f"INFO SAVED -> {filename}")
    print(Fore.GREEN + f"SAVED TO {filename}" + Fore.RESET)

def help_menu():
    print(Fore.CYAN + """
Options:
  [1] Info       -> show system info
  [2] Save Info  -> save info to JSON
  [3] Help       -> show help
  [0] Exit       -> exit tool
""" + Fore.RESET)

while True:
    print(Colorate.Horizontal(Colors.blue_to_white, '''
  _________               __                     .___        _____       
 /   _____/__.__. _______/  |_  ____   _____     |   | _____/ ____\____  
 \_____  <   |  |/  ___/\   __\/ __ \ /     \    |   |/    \   __\/  _ \ 
 /        \___  |\___ \  |  | \  ___/|  Y Y  \   |   |   |  \  | (  <_> )
/_______  / ____/____  > |__|  \___  >__|_|  /   |___|___|  /__|  \____/ 
        \/\/         \/            \/      \/             \/             
                          
        [1] Info
        [2] Save Info
        [3] Help
        [0] Exit
    '''))

    option = input(Colorate.Horizontal(Colors.white_to_blue, "Option > "))

    if option == "1":
        show_info()
        input("Press Enter to continue...")
        clear()

    elif option == "2":
        save_info()
        input("Press Enter to continue...")
        clear()

    elif option == "3":
        help_menu()
        log("HELP OPENED")
        input("Press Enter to continue...")
        clear()

    elif option == "0":
        log("TOOL CLOSED")
        break

    else:
        print(Fore.RED + "Invalid option" + Fore.RESET)
        log("INVALID INPUT")
        input("Press Enter to continue...")
        clear()
