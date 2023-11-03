try:
    from pywifi import PyWiFi, const
    from pytube import YouTube
    from colorama import Fore
    import subprocess
    import webbrowser
    import threading
    import fileinput
    import datetime
    import requests
    import platform
    import secrets
    import ctypes
    import pywifi
    import random
    import psutil
    import serial
    import string
    import json
    import time
    import os
except Exception as e: input(f"Error while importing\n-> {e}")
if platform.system() == "Windows": pass 
else: input(f"Sorry only windows is supported ur on {platform.system()}, considel using a vm tho Enter to exit"); exit()

class create:
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/YTDownloader", exist_ok=True)
    data = {
        "Random titles": True,
        "Title delay": "5",
        "Use some random weird-looking title shit?": False
    }
    if os.path.exists("config.json"):
        pass
    else:
        with open("config.json", 'w') as f:
            json.dump(data, f, indent=4)
        input("Needed files and folders were created. Please reopen the file.")

class cfg:
    with open("config.json", "r") as f:
        cfg = json.load(f)
    random_titles_state = cfg.get("Random titles")
    title_delay = cfg.get("Title delay")
    try: title_delay = int(title_delay)
    except Exception as e: input(f"Error while converting the title deleay to a usable format -> {e}")
    wiried_title_state = cfg.get("Use some random wiried ahh looking title shit?")

class run:
    def CheckIP(ip):
        os.system(f"ping {ip}")
    
    def BluetoothAttack(COMXX, baudrate, data):
        # Funfact I myself dont know how do use this lol
        while True:
            try:
                ser = serial.Serial(COMXX, baudrate)
                ser.write(data)
                ser.close()
            except Exception as e:
                print(f"{g}>{pl} Error while getting a connection -> {e}")
    
    def FakeWifiSignals(name, numb, wait):
        # Not tested or anyhtign dont know if it even works or should lol
        wifi = pywifi.PyWiFi()
        adapters = wifi.interfaces()
        if not adapters: input("Sorry no wifi adapters found!"); exit()
        else: 
            print(f"{y}>{pl} Anvaible adapters ->\n")
            for _, adapter in enumerate(adapters ):
                print(f"{g}>{pl}Adapter {_}: {adapter.name()}")
        for _ in range(numb):
            time.sleep(wait)
            iface = wifi.interfaces()[0]
            profile = pywifi.Profile()
            profile.ssid = name 
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_NONE)
            profile.cipher = const.CIPHER_TYPE_NONE
            temp = iface.add_network_profile(profile)
            iface.connect(temp)
            if iface.status() == const.IFACE_CONNECTED: print(f"{g}>{pl} Created -> {name}")
            else: print(f"{r}>{pl} Failed status -> {iface.status()}")
    
    def YoutubeVideoDownloader(url):
        def progress(stream, chunk, remaining):
            # Tbh this progress shit was from chat gpt bc i didint know how to do it and i dont have time for research
            total = stream.filesize
            downloaded = total - remaining
            percentage = (downloaded / total) * 100
            print(f"{y}>{pl} Downloading... {percentage:.2f}%")
        try:
            yt = YouTube(url, on_progress_callback=progress)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download("data/YTDownloader")
            print(f"{g}>{pl} Succes!")
            os.startfile("data\YTDownloader")
        except Exception as e:
            print(f"{r}>{pl} Error downloading -> {e}")
    
    def GetSpecs():
        print(f"\n{g}>{pl} CPU INFO")
        print(f"{y}>{pl} CPU Cores -> {psutil.cpu_count(logical=False)}")
        print(f"{y}>{pl} CPU Threads -> {psutil.cpu_count(logical=True)}")
        print(f"{y}>{pl} CPU Frequency -> {psutil.cpu_freq().current}Mhz")

        print(f"\n{g}>{pl} RAM INFO")
        memory = psutil.virtual_memory()
        print(f"{y}>{pl} Total -> {memory.total // (1024**3)} GB")
        print(f"{y}>{pl} Available -> {memory.available // (1024**3)} GB")
        print(f"{y}>{pl} Used -> {memory.used // (1024**3)} GB")
        print(f"{y}>{pl} Free -> {memory.free // (1024**3)} GB")

        print(f"\n{g}>{pl} DISK INFO")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"{y}>{pl} Device -> {partition.device}")
            print(f"{y}>{pl} Mountpoint -> {partition.mountpoint}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"{y}>{pl} Total Size: {partition_usage.total // (1024**3)} GB")
                print(f"{y}>{pl} Used: {partition_usage.used // (1024**3)} GB")
                print(f"{y}>{pl} Free: {partition_usage.free // (1024**3)} GB")
            except Exception: print(f"Error while getting disk info -> {e}")

r = Fore.RED
y = Fore.LIGHTYELLOW_EX
g = Fore.GREEN
res = Fore.RESET
p = Fore.LIGHTMAGENTA_EX
pl = Fore.MAGENTA
b = Fore.LIGHTBLACK_EX

banner = (f"""
        {pl}             ██████╗ ██████╗  ██████╗██╗    ███████╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
        {pl}             ██╔══██╗╚════██╗██╔════╝██║    ██╔════╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
        {pl}             ██████╔╝ █████╔╝██║     ██║    ███████╗    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
        {p}             ██╔══██╗ ╚═══██╗██║     ██║    ╚════██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
        {p}             ██║  ██║██████╔╝╚██████╗██║    ███████║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
        {p}             ╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝    ╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝   

Made by R3CI <3                                                                                                              
""")

class gui:
    def title_changer(tit_state, deleay, randomtitleniggastatelolidk):
        if randomtitleniggastatelolidk == True:
            while True:
                kotlet_schabowy = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1000))
                ctypes.windll.kernel32.SetConsoleTitleW(kotlet_schabowy)
        else: pass
        if tit_state == True: pass
        else: ctypes.windll.kernel32.SetConsoleTitleW(f"R3CI'S Multitool | Welcome {os.getlogin()} !"); return
        ctypes.windll.kernel32.SetConsoleTitleW(f"Welcome {os.getlogin()} !")
        time.sleep(5)   
        while True:
            time_rn = datetime.datetime.now(); timee = time_rn.strftime("%H:%M:%S")
            titles = [
            "Thanks for using my multitool",
            "Made with love by R3CI",
            "Discord -> https://discord.gg/5cgQmfNj6W",
            "This repo -> https://github.com/R3CI/R3CI-S-MultiTool",
            "My discord user is -> r3ci.",
            f"Its {timee} rightnow",
            "Vencord is the best discord mod",
            "Dogjump to kurwa jebana",
            "My fav tool for discord -> https://github.com/itschasa/Discord-Backup",
            "Minecraft is a dead game",
            "Minecraft survival > minigames",
            "Xbox 360 was the best console ever made",
            "Karmaleaks is a dead discord",
            "Requests are the worst pice of shit to work with",
            "Doing a discord raiding tool is not fun at all",
            "There are no good discord tools out there",
            "Dazeer V4 is a pice of shit",
            "History is the most boring subject",
            "Discord is a shit platform but there are no better ones (if people had brains they could switch to guilded)",
            "Baba od polaka to jebana stara kurwa",
            "Dogs > cats",
            "Haze is some 17yo that sits and cheats in games and never goes out",
            "Python is a really nice launguage but only for simple things",
            "C++ is hard to learn :(",
            "Ironic is a really greate youtuber and deserves more subs",
            "Russian songs are really good btw",
            "Currently sitting here adding those random things beacouse i have nothing better to do",
            "Robalini's steam account email is jupł212212@wp.pl",
            "Proton is a actualy good email host",
            "Mullvad vpn on top",
            "lgbt is not normal",
            "Im writing this on 30.10.2023",
            "Ets2 is a awansome game",
            "Think how good ets3 would be",
            "Nothing here",
            "I was vacbanned 2 times",
            "This randomization system is fucking ass",
            "CS2 is a really good and bad game at the same time",
            "csgo hvh is ass",
            "Im bored but there is no school tmrw",
            "I just raged from my authistic teammates",
            "Cracked games > buying games",
            "My english is shit ass lol",
            "Nothing here...",
            "I actualy want to have as many random shit here as possible",
            "This script is not a multitool but i named it a multitool bc why not?",
            "I will prob stop updating this very fast",
            "UUUUUUU ajajaj",
            "I hate and love py at the same time",
            "Yellowy-green is my fav colour atm",
            "There are spiders living in my pc and im not even kidding i can see thier webs in it",
            "Have a brain",
            "I read Dziady 2 and tbh that book seems kinda intresting",
            "Rust is a nice game but to have to be a nolife",
            "This feeling - speedup <3",
            "My fav playlist atm https://open.spotify.com/playlist/1xgPtyk0QyabtwvLjWVG09?si=7c9834dff8a84627",
            "BTD6 is a well made game but gets boring really fast",
            "Discords support is shittier than u may thing",
            "My legs are hurting me rn lol",
            "These titles may be written randomly...",
            "400 is the worst fucking error",
            "I should do options but im writing this shit instead lol",
            "Just waiting for the old senson of fn to download",
            "Next week will be the worst one that i ever had",
            "Jebac rosyjski i ta babe od niego",
            "Zdrastfujcie"
            ]
            ctypes.windll.kernel32.SetConsoleTitleW(random.choice(titles))
            time.sleep(deleay)

    thread1 = threading.Thread(target=title_changer, args=(cfg.random_titles_state, cfg.title_delay, cfg.wiried_title_state,))
    thread1.start()
    subprocess.check_call('mode con: cols=150 lines=30', shell=True)
    while True:
        os.system("cls"); print(banner)
        print(f"""
                                                                    {pl}<{p}?{pl}> {pl}-> {p}Settings
        {pl}<{p}1{pl}> {pl}-> {p}Pinger                  {pl}<{p}10{pl}> {pl}-> {p}???                              
        {pl}<{p}2{pl}> {pl}-> {p}Bluetooth attack        {pl}<{p}11{pl}> {pl}-> {p}???
        {pl}<{p}3{pl}> {pl}-> {p}Fake wifi signals       {pl}<{p}12{pl}> {pl}-> {p}???
        {pl}<{p}4{pl}> {pl}-> {p}Youtube downloader      {pl}<{p}13{pl}> {pl}-> {p}???
        {pl}<{p}5{pl}> {pl}-> {p}Specs info              {pl}<{p}14{pl}> {pl}-> {p}???
        {pl}<{p}6{pl}> {pl}-> {pl}???                     {pl}<{p}15{pl}> {pl}-> {pl}???
        {pl}<{p}7{pl}> {pl}-> {pl}???                     {pl}<{p}16{pl}> {pl}-> {pl}???
        {pl}<{p}8{pl}> {pl}-> {pl}???                     {pl}<{p}17{pl}> {pl}-> {pl}???
        {pl}<{p}9{pl}> {pl}-> {pl}???                     {pl}<{p}18{pl}> {pl}-> {pl}???

""")
        c = input(f"{os.getlogin()} {res}>{pl} ")
        print("")
        if c == "?": 
            os.startfile("config.json")

        elif c == "1": 
            os.system("cls"); print(banner)
            IP = input(f"IP {res}>{pl} ")
            run.CheckIP(IP)
            input(f"\n{y}>{pl} Waiting...")

        elif c == "2": 
            os.system("cls"); print(banner)
            COMMX = input(f"IP {res}>{pl} ")
            BD = input(f"BaudRate (defalout is 9600) {res}>{pl} ")
            Data = input(f"Data {res}>{pl} ")
            run.BluetoothAttack(COMMX,BD,Data)
            input(f"\n{y}>{pl} Waiting...")

        elif c == "3":
            os.system("cls"); print(banner)
            name = input(f"Name {res}>{pl} ")
            numb = input(f"Number to create {res}>{pl} ")
            wait = input(f"Wait {res}>{pl} ")
            try:
                numb = int(numb)
            except ValueError:
                input(f"{r}>{pl} Invalid numbers of creation number"); exit()
            try:
                wait = int(wait)
            except ValueError:
                input(f"{r}>{pl} Invalid wait number"); exit()
            run.FakeWifiSignals(name, numb, wait)
            input(f"\n{y}>{pl} Waiting...")

        elif c == "4": 
            os.system("cls"); print(banner)
            url = input(f"Video URL {res}>{pl} ")
            run.YoutubeVideoDownloader(url)
            input(f"\n{y}>{pl} Waiting...")
        
        elif c == "5":
            os.system("cls"); print(banner)
            run.GetSpecs()
            input(f"\n{y}>{pl} Waiting...")

        else: input(f"{r}>{pl} Sorry! This option does not exist")