import ctypes
import os
ctypes.windll.kernel32.SetConsoleTitleW("Loading...")
print("Loading... please wait")
version = "1.6"
discord = "https://discord.gg/vTsvhtNR"
try:
    from googletrans import Translator
    from pytube import YouTube
    from colorama import Fore
    import subprocess
    import webbrowser
    import threading
    import datetime
    import requests
    import platform
    import ctypes
    import psutil
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
    "psutil",
    "qrcode",
    "googletrans==4.0.0-rc1"
    ]
    i = 0
    for imp in imports:
        i += 1
        os.system(f"pip install -q {imp}")
        print(f"Pacage {imp} installed {i}/7    ")
    input("Installed pacages restart")
    exit()
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
                print(f"{lred}New features:\n{red}{changelog}")
                input(f"{red}> {red}REMEMBER! before running an updated version deleate ur config.json as i may have made some changes")

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
            "data/QRCodeGenerator",
            "data/ProxyScraper"
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
                        "Nothing here for now...": True
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

#class cfg:
#    try:
#        with open("config.json", "r") as f:
#            cfg = json.load(f)
#        random_titles_state = cfg.get("Random titles")
#        title_delay = cfg.get("Title delay")
#        try: title_delay = int(title_delay)
#        except Exception as e: input(f"Error while converting the title deleay to a usable format: {e}")
#        wiried_title_state = cfg.get("Use some random wiried ahh looking title shit?")
#    except Exception as e: input(f"Error reading the config: {e}\nFirst time running?"); exit()

class run:
    
    def check_ip(ip):
        os.system(f"ping {ip}")
    
    def download_video_from_youtube(url):
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download("data/YTDownloader")
            print(f"{green}>{purple} Succes!")
            os.startfile("data\YTDownloader")
        except: pass
    
    def get_specs():
        print(f"\n{green}>{red} CPU INFO")
        print(f"{yellow}>{lred} CPU Cores: {psutil.cpu_count(logical=False)}")
        print(f"{yellow}>{lred} CPU Threads: {psutil.cpu_count(logical=True)}")
        print(f"{yellow}>{lred} CPU Frequency: {psutil.cpu_freq().current}Mhz")

        print(f"\n{green}>{red} RAM INFO")
        memory = psutil.virtual_memory()
        print(f"{yellow}>{lred} Total: {memory.total // (1024**3)} GB")
        print(f"{yellow}>{lred} Available: {memory.available // (1024**3)} GB")
        print(f"{yellow}>{lred} Used: {memory.used // (1024**3)} GB")
        print(f"{yellow}>{lred} Free: {memory.free // (1024**3)} GB")

        print(f"\n{green}>{red} DISK INFO")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"{yellow}>{lred} Device: {partition.device}")
            print(f"{yellow}>{lred} Mountpoint: {partition.mountpoint}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"{yellow}>{lred} Total Size: {partition_usage.total // (1024**3)} GB")
                print(f"{yellow}>{lred} Used: {partition_usage.used // (1024**3)} GB")
                print(f"{yellow}>{lred} Free: {partition_usage.free // (1024**3)} GB")
            except: pass

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
    def title():
        while True:
            time_rn = datetime.datetime.now(); timee = time_rn.strftime("%H:%M:%S")
            ctypes.windll.kernel32.SetConsoleTitleW(f"R3CI'S Multitool | Running on {os.getlogin()} | {timee}")
        
    thread1 = threading.Thread(target=title)
    thread1.start()
    while True:
        size = os.get_terminal_size().columns
        os.system("cls")
        def asci_render(size):
            global banner
            global options
            global options2
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

            for edge in ["░", "▒"]:
                banner = banner.replace(edge, f"{red}{edge}{lred}")
            print(banner)
            options = f"""{res}
{'? - Settings  |  $ - Credits  |  ! - Discord  |  % - exit'.center(size)}
{'╭─────────────────────────────────────────────────────────────────────────────────────────────╮'.center(size)}
{'│ 01 - Pinger            06 - Request            11 - Token login      16 - ???               │'.center(size)}
{'│ 02 - ???               07 - QR code maker      12 - Clock            17 - ???               │'.center(size)}
{'│ 03 - ???               08 - Translator         13 - Proxy scraper    18 - ???               │'.center(size)}
{'│ 04 - Yt downloader     09 - Calculator         14 - ???              19 - ???               │'.center(size)}
{'│ 05 - Specs info        10 - Osint              15 - ???              >> - Next page         │'.center(size)}
{'╰─────────────────────────────────────────────────────────────────────────────────────────────╯'.center(size)}
"""
            for edge in ["─", "╭", "│", "╰", "╯", "╮", "-"]:
                options = options.replace(edge, f"{red}{edge}{lred}")
            for number in ['?', '$', '@', '!', '%', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '>>']:
                options = options.replace(number, f"{res}{number}{red}")
            print(options)
        
            options2 = f"""{res}
{'╭─────────────────────────────────────────────────────────────────────────────────────────────╮'.center(size)}
{'│ 20 - ???               25 - ???                30 - ???              35 - ???               │'.center(size)}
{'│ 21 - ???               26 - ???                31 - ???              36 - ???               │'.center(size)}
{'│ 22 - ???               27 - ???                32 - ???              37 - ???               │'.center(size)}
{'│ 23 - ???               28 - ???                33 - ???              38 - ???               │'.center(size)}
{'│ 24 - ???               29 - ???                34 - ???              << - Return            │'.center(size)}
{'╰─────────────────────────────────────────────────────────────────────────────────────────────╯'.center(size)}
"""
            for edge in ["─", "╭", "│", "╰", "╯", "╮", "-"]:
                options2 = options2.replace(edge, f"{red}{edge}{lred}")
            for number in ['?', '$', '@', '!', '%', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '>>']:
                options2 = options2.replace(number, f"{res}{number}{red}")
        
        asci_render(size)

        c = input(f"{lred}{os.getlogin()} {res}>{red} ")
        print("")

        if c == "?": 
            os.startfile("config.json")

        if c == "$": 
            os.system("cls"); print(banner)
            print(f"{green}> {lred} No credits atm auggest to be here!")
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "!": 
            os.system("cls"); print(banner)
            webbrowser.open(discord)
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "%": 
            exit()

        elif c == "1": 
            os.system("cls"); print(banner)
            IP = input(f"{lred}IP {res}>{red} ")
            run.check_ip(IP)
            input(f"\n{yellow}>{lred} Waiting...")

        #elif c == "2": 
        #    os.system("cls"); print(banner)
        #    input(f"\n{yellow}>{lred} Waiting...")

        #elif c == "3":
        #    os.system("cls"); print(banner)
        #    input(f"\n{yellow}>{lred} Waiting...")

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
        
        elif c == "11":
            os.system("cls"); print(banner)
            token = input(f"{lred}token {res}>{red} ")
            webbrowser.open(f"https://discord.com/?discordtoken={token}")
            input(f"\n{yellow}>{lred} Waiting...")
        
        elif c == "12":
            os.system("cls"); print(banner)
            while True:
                time.sleep(1)
                os.system("cls"); print(banner)
                time_rn = datetime.datetime.now(); timee = time_rn.strftime("%H:%M:%S")
                clock = f"{f'{red}{timee}'.center(size)}"
                for dwukropek in [":"]:
                    clock = clock.replace(dwukropek, f"{res}{dwukropek}{red}")
                print(clock)      

        elif c == ">>":
            os.system("cls"); print(banner)
            print(options2)
            c = input(f"{lred}{os.getlogin()} {res}>{red} ")
            if c == "<<":
                 print(options)
            elif c == "22":
                input("works")

        else: input(f"{red}>{lred} Sorry! This option does not exist")
