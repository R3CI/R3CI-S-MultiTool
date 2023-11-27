import ctypes
import os
ctypes.windll.kernel32.SetConsoleTitleW("Loading...")
print("Loading... please wait")
version = "1.5"
discord = "https://discord.gg/vTsvhtNR"
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

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
res = Fore.RESET
purple = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
black = Fore.LIGHTBLACK_EX

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
            if locall > github: pass
            else:
                os.system("cls")
                size = os.get_terminal_size().columns
                edges = ["╗", "║", "╚", "╝", "═", "╔"]
                update_banner = f"""{lred}
    {'███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗'.center(size)}
    {'████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║'.center(size)}
    {'██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║'.center(size)}
    {'██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝'.center(size)}
    {'██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗'.center(size)}
    {'╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝'.center(size)}                                                                                                     
    """
                for edge in edges:
                    update_banner = update_banner.replace(edge, f"{red}{edge}{lred}")
                print(update_banner)
                print(f"{lred}Current version: {res}{locall}{lred}\nNewest version: {res}{github}{lred}\n")
                input(f"{lred}New features:\n{red}{changelog}")
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
    def send_a_suggestion(author, suggestion):
        valid = False
        wb = "https://discord.com/api/webhooks/1178756355499241482/xSePgUa1-zxEFZ2WBhkOXnIeCJsmXs9qBxfIm-umcOhW1Dm7OHLw8xw-f93BXGINjDrN"
        try:
            valid = True
            r = requests.head(wb, timeout=5)
            r.raise_for_status()
        except:
            valid = False
            print(f"{red}> {lred}Sorry, the webhook seems to be deleted. Try joining my discord and suggesting there.")

        if valid:
            payload = {"content": f"<@1125147653970337896>\nNew suggestion!\nAuthor: {author}\nSuggestion: {suggestion}"}
            headers = {"Content-Type": "application/json"}
            r = requests.post(wb, data=json.dumps(payload), headers=headers)
            if r.status_code == 204:
                print(f"{green}> {lred}Message sent successfully!")
            else:
                print(f"{red}> {lred}Failed to send the suggestion")
    
    def check_ip(ip):
        os.system(f"ping {ip}")
    
    def make_a_bluetooth(COMXX, baudrate, data):
        # Funfact I myself dont know how do use this lol
        while True:
            try:
                ser = serial.Serial(COMXX, baudrate)
                ser.write(data)
                ser.close()
            except Exception as e:
                print(f"{green}>{purple} Error while getting a connection: {e}")
    
    def make_a_fake_wifi(name, numb, wait):
        # Not tested or anyhtign dont know if it even works or should lol
        wifi = pywifi.PyWiFi()
        adapters = wifi.interfaces()
        if not adapters: input("Sorry no wifi adapters found!"); exit()
        else: 
            print(f"{yellow}>{purple} Anvaible adapters: \n")
            for _, adapter in enumerate(adapters ):
                print(f"{green}>{purple}Adapter {_}: {adapter.name()}")
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
            if iface.status() == const.IFACE_CONNECTED: print(f"{green}>{purple} Created: {name}")
            else: print(f"{red}>{purple} Failed status: {iface.status()}")
    
    def download_video_from_youtube(url):
        def progress(stream, chunk, remaining):
            # Tbh this progress shit was from chat gpt bc i didint know how to do it and i dont have time for research
            total = stream.filesize
            downloaded = total - remaining
            percentage = (downloaded / total) * 100
            print(f"{yellow}>{purple} Downloading... {percentage:.2f}%")
        try:
            yt = YouTube(url, on_progress_callback=progress)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download("data/YTDownloader")
            print(f"{green}>{purple} Succes!")
            os.startfile("data\YTDownloader")
        except Exception as e:
            print(f"{red}>{purple} Error downloading: {e}")
    
    def get_specs():
        print(f"\n{green}>{purple} CPU INFO")
        print(f"{yellow}>{purple} CPU Cores: {psutil.cpu_count(logical=False)}")
        print(f"{yellow}>{purple} CPU Threads: {psutil.cpu_count(logical=True)}")
        print(f"{yellow}>{purple} CPU Frequency: {psutil.cpu_freq().current}Mhz")

        print(f"\n{green}>{purple} RAM INFO")
        memory = psutil.virtual_memory()
        print(f"{yellow}>{purple} Total: {memory.total // (1024**3)} GB")
        print(f"{yellow}>{purple} Available: {memory.available // (1024**3)} GB")
        print(f"{yellow}>{purple} Used: {memory.used // (1024**3)} GB")
        print(f"{yellow}>{purple} Free: {memory.free // (1024**3)} GB")

        print(f"\n{green}>{purple} DISK INFO")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"{yellow}>{purple} Device: {partition.device}")
            print(f"{yellow}>{purple} Mountpoint: {partition.mountpoint}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"{yellow}>{purple} Total Size: {partition_usage.total // (1024**3)} GB")
                print(f"{yellow}>{purple} Used: {partition_usage.used // (1024**3)} GB")
                print(f"{yellow}>{purple} Free: {partition_usage.free // (1024**3)} GB")
            except Exception: print(f"{red}>{purple} Error while getting disk info -> {e}")

    def request(url, method, payload, header, loop):
        # I dont even know if this will work correctly i dont have any request to test it on
        if loop == "y":
            while True:
                try:
                    if payload and header: response = requests.request(method, url, json=payload, headers=header)
                    elif payload: response = requests.request(method, url, json=payload)
                    elif header: response = requests.request(method, url, headers=header)
                    else: response = requests.request(method, url)
                    
                    if response.status_code: print(f"{yellow}>{purple} Status code: {response.status_code}")
                    if response.json(): print(f"{yellow}>{purple} Response: {response.json()}")

                except Exception as e:
                    print(f"{red}>{purple} Error while doing a request: {e}")
        else:
            while True:
                try:
                    if payload and header: response = requests.request(method, url, json=payload, headers=header)
                    elif payload: response = requests.request(method, url, json=payload)
                    elif header: response = requests.request(method, url, headers=header)
                    else: response = requests.request(method, url)
                    
                    if response.status_code: print(f"{yellow}>{yellow} Status code: {response.status_code}")
                    if response.json(): print(f"{yellow}>{yellow} Response: {response.json()}")

                except Exception as e:
                    print(f"{red}>{yellow} Error while doing a request: {e}")
    
    def generate_a_qr_code(data, name):
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

    def translate(text,target_language='en'):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text

    def calculate(problem):
        try:
            result = eval(problem)
        except Exception as e:
            input(f"{red}>{yellow} Failed error: {e}")
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
                "Discord -> https://discord.gg/vTsvhtNR",
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
                "Zdrastfujcie",
                "Havent updated those in a bit"
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
            edges = ["░", "▒"] 
            banner = f"""{Fore.LIGHTRED_EX}
{' ██▀███   ▄████▄   ██▓     ██████     ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    '.center(size)}
{'▓██ ▒ ██▒▒██▀ ▀█  ▓██▒   ▒██    ▒    ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    '.center(size)}
{'▓██ ░▄█ ▒▒▓█    ▄ ▒██▒   ░ ▓██▄      ▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    '.center(size)}
{'▒██▀▀█▄  ▒▓▓▄ ▄██▒░██░     ▒   ██▒   ▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    '.center(size)}
{'░██▓ ▒██▒▒ ▓███▀ ░░██░   ▒██████▒▒   ▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒'.center(size)}
{'░ ▒▓ ░▒▓░░ ░▒ ▒  ░░▓     ▒ ▒▓▒ ▒ ░   ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░'.center(size)}
{'  ░▒ ░ ▒░  ░  ▒    ▒ ░   ░ ░▒  ░ ░   ░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░'.center(size)}
{'  ░░   ░ ░         ▒ ░   ░  ░  ░     ░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   '.center(size)}
{'   ░     ░ ░       ░           ░            ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░'.center(size)}
{'         ░                                                                                                     '.center(size)}
"""

            for edge in edges:
                banner = banner.replace(edge, f"{red}{edge}{lred}")
            print(banner)

            edges = ["─", "╭", "│", "╰", "╯", "╮", "-"]
            numbers = ['?', '$', '@', 'dsc', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '>>']
            options = f"""{res}
{'? - Settings   $ - Credits   @ - Suggest a feature dsc - Discord'.center(size)}
{'╭─────────────────────────────────────────────────────────────────────────────────────────────╮'.center(size)}
{'│ 01 - Pinger            06 - Request            11 - ???              16 - ???               │'.center(size)}
{'│ 02 - Bluetooth attack  07 - QR code maker      12 - ???              17 - ???               │'.center(size)}
{'│ 03 - Fake wifi         08 - Translator         13 - ???              18 - ???               │'.center(size)}
{'│ 04 - Yt downloader     09 - Calculator         14 - ???              19 - ???               │'.center(size)}
{'│ 05 - Specs info        10 - Osint              15 - ???              >> - Next page         │'.center(size)}
{'╰─────────────────────────────────────────────────────────────────────────────────────────────╯'.center(size)}
"""
            for edge in edges:
                options = options.replace(edge, f"{red}{edge}{lred}")
            for number in numbers:
                options = options.replace(number, f"{res}{number}{red}")
            print(options)
        
        asci_render(size)

        c = input(f"{lred}{os.getlogin()} {res}>{red} ")
        print("")

        if c == "?": 
            os.startfile("config.json")

        if c == "$": 
            os.system("cls"); print(banner)
            print(f"{green}> {lred} No credits atm auggest to be here!")
            input(f"\n{yellow}>{lred} Waiting...")
        
        if c == "@": 
            os.system("cls"); print(banner)
            author = input(f"{lred}Author {res}>{red} ")
            suggestion = input(f"{lred}Suggestion {res}>{red} ")
            if "@everyone" in suggestion: input("""
Traceback (most recent call last):
    line 971, in json
    return complexjson.loads(self.text, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
    line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
    in <module>
    line 457, in render
    run.send_a_suggestion(author, suggestion)
    line 176, in send_a_suggestion
    line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
"""); exit()
            run.send_a_suggestion(author, suggestion)
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "dsc": 
            os.system("cls"); print(banner)
            webbrowser.open(discord)
            input(f"\n{yellow}>{lred} Waiting...")


        elif c == "1": 
            os.system("cls"); print(banner)
            IP = input(f"{lred}IP {res}>{red} ")
            run.check_ip(IP)
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "2": 
            os.system("cls"); print(banner)
            COMMX = input(f"{lred}IP {res}>{red} ")
            BD = input(f"{lred}BaudRate (defalout is 9600) {res}>{red} ")
            Data = input(f"{lred}Data {res}>{red} ")
            run.make_a_bluetooth(COMMX,BD,Data)
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "3":
            os.system("cls"); print(banner)
            name = input(f"{lred}Name {res}>{red} ")
            numb = input(f"{lred}Number to create {res}>{red} ")
            wait = input(f"{lred}Wait {res}>{red} ")
            try:
                numb = int(numb)
            except ValueError:
                input(f"{red}>{lred} Invalid numbers of creation number"); exit()
            try:
                wait = int(wait)
            except ValueError:
                input(f"{red}>{lred} Invalid wait number"); exit()
            run.make_a_fake_wifi(name, numb, wait)
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "4": 
            os.system("cls"); print(banner)
            url = input(f"{lred}Video URL {res}>{red} ")
            run.download_video_from_youtube(url)
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "5":
            os.system("cls"); print(banner)
            run.get_specs()
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "6":
            os.system("cls"); print(banner)
            url = input(f"{lred}URL {res}>{red} ")
            method = input(f"{lred}Method {res}>{red} ")
            payload = input(f"{lred}Payload/json (blank if none) {res}>{red} ")
            header = input(f"{lred}Header (blank if none) {res}>{red} ")
            loop = input(f"{lred}Loop the request? (y/n) {res}>{red} ")
            run.request(url, method, payload, header, loop)
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "7":
            os.system("cls"); print(banner)
            url = input(f"{lred}URL {res}>{red} ")
            name = input(f"{lred}File name {res}>{red} ")
            run.generate_a_qr_code(url, name)
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "8":
            os.system("cls"); print(banner)
            text = input(f"{lred}Text {res}>{red} ")
            lang = input(f"{lred}Language {res}>{red} ")
            try:
                translated_text = run.translate(text, lang)
            except Exception as e: print(f"{red}>{lred} Failed to translate error: {e}")
            print(f"{green}>{lred} Translated text: {translated_text}")
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "9":
            os.system("cls"); print(banner)
            problem = input(f"{lred}Problem {res}>{red} ")
            result = run.calculate(problem)
            print(f"{green}>{lred} Resoult: {result}")
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == "10":
            os.system("cls"); print(banner)
            webbrowser.open("https://search.0t.rocks")
            input(f"\n{yellow}>{lred} Waiting...")

        elif c == ">>":
            os.system("cls"); print(banner)
            print(f"{red}>{lred} Not made yet")
            input(f"\n{yellow}>{lred} Waiting...")

        else: input(f"{red}>{lred} Sorry! This option does not exist")
