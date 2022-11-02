import os, sys, wget
from sys import platform
from versions import AvailableVersions
from snapshots import AvailableSnapshots


class color:
   HEADER = '\033[95m' 
   PURPLE = '\033[95m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   CYAN = '\033[96m'
   GREEN = '\033[92m'
   WARNING = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[6m'
   HIGHLIGHT= '\033[7m'
   END = '\033[0m'


vanilla = {
    'vanilla',
    'snapshot'
}
servers = {
    'purpur',
    'paper',
    'spigot',
    'bukkit',
    'tuinity',
    'sponge'
}
modded = {
    'mohist',
    'forge',
    'catServer',
    'fabric'
}
proxies = {
    'bungeeCord',
    'velocity',
    'waterfall',
    'flamecord'
}

SoftwareCheck = {

    'vanilla',
    'snapshot',
    'purpur',
    'paper',
    'spigot',
    'bukkit',
    'tuinity',
    'sponge',
    'mohist',
    'forge',
    'catserver',
    'fabric',
    'bungeeCord',
    'velocity',
    'waterfall',
    'flamecord'
}


WorkinDirectory = os.getcwd()

WD = f'{WorkinDirectory}/'

try:

    while True:
        
        print(f'''
        {color.GREEN}Available Software:{color.END}
        {color.BOLD}{color.GREEN}VANILLA{color.END}
            {color.PURPLE}{vanilla}{color.END}
        {color.BOLD}{color.GREEN}SERVERS:{color.END}
            {color.PURPLE}{servers}{color.END}
        {color.BOLD}{color.GREEN}MODDED{color.END}
            {color.PURPLE}{modded}{color.END}
        {color.BOLD}{color.GREEN}PROXIES{color.END}
            {color.PURPLE}{proxies}{color.END}''')
        Software = input('Software:').lower()

        if Software in SoftwareCheck:
                Version = input('''
                    example: 1.19.2

                    Version: ''')
        if Software not in SoftwareCheck:
            print(f"{color.BLINK}{color.RED}Invalid Software{color.END}")
            
            
        if Software in ['mohist', 'forge', 'catserver', 'fabric'] and Version in AvailableVersions:
            print('1')
            wget.download(f'https://serverjars.com/api/fetchJar/modded/{Software}/{Version}', out=WD)
        if Software in ['bungeecord', 'velocity', 'waterfall', 'flamecord'] and Version in AvailableVersions:
            print('2')
            wget.download(f'https://serverjars.com/api/fetchJar/proxies/{Software}/{Version}', out=WD)
        if Software in{'pupur', 'paper', 'spigot', 'bukkit', 'tuinity', 'sponge'}and Version in AvailableVersions:
            print('3')
            wget.download(f'https://serverjars.com/api/fetchJar/servers/{Software}/{Version}', out=WD)

        StartRam = input('\nHow Much Ram Would you Like to Allocate to server in GB (ex: 13)')
        
        f= open(f'{WD}eula.txt',"a")
        f.write('''
# Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)
eula=true
            ''')
        
        if platform == 'Linux' or platform == 'linux' or platform == 'linux2':
            f= open(f'{WD}start.sh', 'a')
            f.write(f'java -Xmx{StartRam}G -Xms{StartRam}G -jar {Software}-{Version}.jar --nogui')
            break
        elif platform == 'darwin':
            f= open(f'{WD}start.sh', 'a')
            f.write(f'''
# Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)

java -Xmx1024M -jar craftbukkit.jar -o true

                ''')
            break
        elif platform == 'win32':
            f= open(f'{WD}start.bat', 'a')
            f.write(f'''
# Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)

@echo off
title Server Console
java -Xmx{StartRam}G -jar ServerFile.jar
PAUSE
''')
        break        
        

                    
except KeyboardInterrupt:
    print('Keyboard Interrupt')