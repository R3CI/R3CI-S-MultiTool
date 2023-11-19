version = "1.31"
import os
try:
    from googletrans import Translator
    from pywifi import PyWiFi, const
    from pytube import YouTube
    from colorama import Fore
    import subprocess
    import webbrowser
    import threading
    import datetime
    import requests
    import platform
    import ctypes
    import pywifi
    import random
    import psutil
    import serial
    import string
    import qrcode
    import json
    import time

except Exception as e:
    input(f"Error while importing: {e}\nPress enter to install required pacages")
    imports = [
    "pytube",
    "colorama",
    "datetime",
    "requests",
    "pywifi",
    "psutil",
    "serial",
    "qrcode",
    "googletrans==4.0.0-rc1"
    ]
    i = 0
    for imp in imports:
        i =+ 1
        os.system("cls")
        os.system(f"pip install {imp}")
        print(f"Pacage {imp} installed {i}/22")

if platform.system() == "Windows": pass 
else: input(f"Sorry only windows is supported ur on {platform.system()}, considel using a vm tho Enter to exit"); exit()

r = Fore.RED
y = Fore.LIGHTYELLOW_EX
g = Fore.GREEN
res = Fore.RESET
p = Fore.LIGHTMAGENTA_EX
pl = Fore.MAGENTA
b = Fore.LIGHTBLACK_EX

class autoupdate:
    def get_version():
        response = requests.get(f"https://api.github.com/repos/R3CI/R3CI-S-MultiTool/releases/latest")
        if response.status_code == 200:
            data = response.json()
            changelog = data.get('body', '')
            return data['tag_name'], changelog
        
        else:
            input(f"Failed to get info about the version no internet? response: {response.status_code}")
            return None, None
        
    def check_for_update(locall, github, changelog):
        if locall == github: pass
        else:
            os.system("cls")
            size = os.get_terminal_size().columns
            edges = ["╗", "║", "╚", "╝", "═", "╔"]
            update_banner = f"""
{'███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗'.center(size)}
{'████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║'.center(size)}
{'██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║'.center(size)}
{'██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝'.center(size)}
{'██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗'.center(size)}
{'╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝'.center(size)}                                                                                                     
"""
            for edge in edges:
                update_banner = update_banner.replace(edge, f"{Fore.MAGENTA}{edge}{Fore.RESET}")
            print(update_banner)
            print(f"{Fore.MAGENTA}Current version: {Fore.RESET}{locall}{Fore.MAGENTA}\nNewest version: {Fore.RESET}{github}{Fore.MAGENTA}\n")
            input(f"{Fore.MAGENTA}New features:\n{Fore.RESET}{changelog}")
            webbrowser.open(f"https://github.com/R3CI/R3CI-S-MultiTool/releases/tag/{github}")
            exit()
    
    gh_version, changelog = get_version()
    local_version = version

    if gh_version:
        check_for_update(local_version, gh_version, changelog)

class Create:
    @staticmethod
    def make_folder():
        folders = [
            "data",
            "data/YTDownloader",
            "data/QRCodeGenerator"
        ]
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

    @staticmethod
    def make_file_and_write():
        files = [
            "config.json",
            "READ.txt"
        ]
        for file in files:
            if os.path.exists(file): pass 
            else:
                if file == "config.json":
                    data = {
                    "Random titles": True,
                    "Title delay": "5",
                    "Use some random weird-looking title shit?": False
                    }
                
                    with open("config.json", 'w') as f:
                        json.dump(data, f, indent=4)
                elif file == "READ.txt":
                    data = """
Remember ONLY windows is supported

If u get errors try this

1. Get the error and try to understand it (search it up how to get an error from a py file)
2. Try deleting the config.json and the data folder, as that also could be the issue
"""
                    with open("READ.txt", 'w') as f:
                        f.write(data)

    @staticmethod
    def run():
        tasks = [Create.make_folder, Create.make_file_and_write]
        for task in tasks:
            task()

Create.run()

class cfg:
    try:
        with open("config.json", "r") as f:
            cfg = json.load(f)
        random_titles_state = cfg.get("Random titles")
        title_delay = cfg.get("Title delay")
        try: title_delay = int(title_delay)
        except Exception as e: input(f"Error while converting the title deleay to a usable format: {e}")
        wiried_title_state = cfg.get("Use some random wiried ahh looking title shit?")
    except Exception as e: input(f"Error reading the config: {e}\nFirst time running?"); exit()

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
                print(f"{g}>{pl} Error while getting a connection: {e}")
    
    def FakeWifiSignals(name, numb, wait):
        # Not tested or anyhtign dont know if it even works or should lol
        wifi = pywifi.PyWiFi()
        adapters = wifi.interfaces()
        if not adapters: input("Sorry no wifi adapters found!"); exit()
        else: 
            print(f"{y}>{pl} Anvaible adapters: \n")
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
            if iface.status() == const.IFACE_CONNECTED: print(f"{g}>{pl} Created: {name}")
            else: print(f"{r}>{pl} Failed status: {iface.status()}")
    
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
            print(f"{r}>{pl} Error downloading: {e}")
    
    def GetSpecs():
        print(f"\n{g}>{pl} CPU INFO")
        print(f"{y}>{pl} CPU Cores: {psutil.cpu_count(logical=False)}")
        print(f"{y}>{pl} CPU Threads: {psutil.cpu_count(logical=True)}")
        print(f"{y}>{pl} CPU Frequency: {psutil.cpu_freq().current}Mhz")

        print(f"\n{g}>{pl} RAM INFO")
        memory = psutil.virtual_memory()
        print(f"{y}>{pl} Total: {memory.total // (1024**3)} GB")
        print(f"{y}>{pl} Available: {memory.available // (1024**3)} GB")
        print(f"{y}>{pl} Used: {memory.used // (1024**3)} GB")
        print(f"{y}>{pl} Free: {memory.free // (1024**3)} GB")

        print(f"\n{g}>{pl} DISK INFO")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"{y}>{pl} Device: {partition.device}")
            print(f"{y}>{pl} Mountpoint: {partition.mountpoint}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"{y}>{pl} Total Size: {partition_usage.total // (1024**3)} GB")
                print(f"{y}>{pl} Used: {partition_usage.used // (1024**3)} GB")
                print(f"{y}>{pl} Free: {partition_usage.free // (1024**3)} GB")
            except Exception: print(f"{r}>{pl} Error while getting disk info -> {e}")

    def MakeARequest(url, method, payload, header, loop):
        # I dont even know if this will work correctly i dont have any request to test it on
        if loop == "y":
            while True:
                try:
                    if payload and header: response = requests.request(method, url, json=payload, headers=header)
                    elif payload: response = requests.request(method, url, json=payload)
                    elif header: response = requests.request(method, url, headers=header)
                    else: response = requests.request(method, url)
                    
                    if response.status_code: print(f"{y}>{pl} Status code: {response.status_code}")
                    if response.json(): print(f"{y}>{pl} Response: {response.json()}")

                except Exception as e:
                    print(f"{r}>{pl} Error while doing a request: {e}")
        else:
            while True:
                try:
                    if payload and header: response = requests.request(method, url, json=payload, headers=header)
                    elif payload: response = requests.request(method, url, json=payload)
                    elif header: response = requests.request(method, url, headers=header)
                    else: response = requests.request(method, url)
                    
                    if response.status_code: print(f"{y}>{pl} Status code: {response.status_code}")
                    if response.json(): print(f"{y}>{pl} Response: {response.json()}")

                except Exception as e:
                    print(f"{r}>{pl} Error while doing a request: {e}")
    
    def QRGenerator(data, name):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"data\QRCodeGenerator\{name}.png")
        os.startfile("data\QRCodeGenerator")

    def Translate(text,target_language='en'):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text

    def Calculate(problem):
        try:
            result = eval(problem)
        except Exception as e:
            input(f"{r}>{pl} Failed error: {e}")
        try: return result
        except: pass

class render:
    subprocess.check_call('mode con: cols=150 lines=30', shell=True)
    def title_changer():
        def title_randomizer(tit_state, deleay, randomtitleniggastatelolidk):
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

        thread1 = threading.Thread(target=title_randomizer, args=(cfg.random_titles_state, cfg.title_delay, cfg.wiried_title_state,))
        thread1.start()

    title_changer()

    while True:
        size = os.get_terminal_size().columns
        os.system("cls")
        def asci_render(size):
            global banner
            # podjebalem z heliuma ale tylko dlatego bo chcialem ten border ok???
            edges = ["╗", "║", "╚", "╝", "═", "╔"]
            banner = f"""
{'██████╗ ██████╗  ██████╗██╗    ███████╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     '.center(size)}
{'██╔══██╗╚════██╗██╔════╝██║    ██╔════╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     '.center(size)}
{'██████╔╝ █████╔╝██║     ██║    ███████╗    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     '.center(size)}
{'██╔══██╗ ╚═══██╗██║     ██║    ╚════██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     '.center(size)}
{'██║  ██║██████╔╝╚██████╗██║    ███████║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗'.center(size)}
{'╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝    ╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝'.center(size)}
{pl}Made by R3CI <3                                                                                                              
"""

            for edge in edges:
                banner = banner.replace(edge, f"{pl}{edge}{res}")
            print(banner)

            edges = ["─", "╭", "│", "╰", "╯", "╮", "»", "«"]
            options = f"""
{'╭─────────────────────────────────────────────────────────────────────────────────────────────╮'.center(size)}
{'│ «01» Pinger            «06» Request            «11» ???              «16» ???               │'.center(size)}
{'│ «02» Bluetooth attack  «07» QR code maker      «12» ???              «17» ???               │'.center(size)}
{'│ «03» Fake wifi         «08» Translator         «13» ???              «18» ???               │'.center(size)}
{'│ «04» Yt downloader     «09» Calculator         «14» ???              «19» ???               │'.center(size)}
{'│ «05» Specs info        «10» ???                «15» ???              «20» ???               │'.center(size)}
{'╰─────────────────────────────────────────────────────────────────────────────────────────────╯'.center(size)}
"""
            for edge in edges:
                options = options.replace(edge, f"{pl}{edge}{res}")
            print(options)
        
        asci_render(size)

        c = input(f"{pl}{os.getlogin()} {res}>{pl} ")
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
        
        elif c == "6":
            os.system("cls"); print(banner)
            url = input(f"URL {res}>{pl} ")
            method = input(f"Method {res}>{pl} ")
            payload = input(f"Payload/json (blank if none) {res}>{pl} ")
            header = input(f"Header (blank if none) {res}>{pl} ")
            loop = input(f"Loop the request? (y/n) {res}>{pl} ")
            run.MakeARequest(url, method, payload, header, loop)
            input(f"\n{y}>{pl} Waiting...")

        elif c == "7":
            os.system("cls"); print(banner)
            url = input(f"URL {res}>{pl} ")
            name = input(f"File name {res}>{pl} ")
            run.QRGenerator(url, name)
            input(f"\n{y}>{pl} Waiting...")

        elif c == "8":
            os.system("cls"); print(banner)
            text = input(f"Text {res}>{pl} ")
            lang = input(f"Language {res}>{pl} ")
            try:
                translated_text = run.Translate(text, lang)
            except Exception as e: print(f"{r}>{pl} Failed to translate error: {e}")
            print(f"{g}>{pl} Translated text: {translated_text}")
            input(f"\n{y}>{pl} Waiting...")
        
        elif c == "9":
            os.system("cls"); print(banner)
            problem = input(f"Problem {res}>{pl} ")
            result = run.Calculate(problem)
            print(result)
            input(f"\n{y}>{pl} Waiting...")

        else: input(f"{r}>{pl} Sorry! This option does not exist")
