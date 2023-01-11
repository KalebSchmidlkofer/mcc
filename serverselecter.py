#!/home/kaleb/bin/mccVar/.mcc/bin/python
import sys, wget, stat, requests
from os import getcwd, chmod
from os import stat as sts
from time import sleep
from sys import platform
from mccVar.versions import AvailableVersions
from mccVar.snapshots import AvailableSnapshots

unitColor = '\033[5;91m\033[5;47m'
endColor = '\033[0;0m\033[0;0m'
count = 9

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
    'snapshot(WIP)'
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


def crapcode():
    print("loading bar")



WorkinDirectory = getcwd()



WD = f'{WorkinDirectory}/'
def main():
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

            if Software == 'snapshot':
                print('Unable to download snapshots right now, if you want to download these files please visit https://serverjars.com/#vanilla')
                break
            if Software in SoftwareCheck:
                    Version = input('''
                        latest

                        Version: ''')
            if Software not in SoftwareCheck:
                print(f"{color.BLINK}{color.RED}Invalid Software{color.END}")

                if Software in vanilla:
                    print(f'https://serverjars.com/api/fetchLatest/vanilla/{Software}')
                if Software in servers:
                    print(f'https://serverjars.com/api/fetchLatest/servers/{Software}')
                
                if Software in modded:
                    print(f'https://serverjars.com/api/fetchLatest/modded/{Software}')

                if Software in proxies:
                    print(f'https://serverjars.com/api/fetchLatest/proxies/{Software}')

                # print(f'Latest version is of {Software} is {}')


            if Software in ['vanilla'] and Version in AvailableVersions:
                wget.download(f'https://serverjars.com/api/fetchjar/vanilla/{Software}/{Version}', out=WD)
            if Software in ['mohist', 'forge', 'catserver', 'fabric'] and Version in AvailableVersions:
                wget.download(f'https://serverjars.com/api/fetchJar/modded/{Software}/{Version}', out=WD)
            if Software in ['bungeecord', 'velocity', 'waterfall', 'flamecord'] and Version in AvailableVersions:
                wget.download(f'https://serverjars.com/api/fetchJar/proxies/{Software}/{Version}', out=WD)
            if Software in{'purpur', 'paper', 'spigot', 'bukkit', 'tuinity', 'sponge'}and Version in AvailableVersions:
                wget.download(f'https://serverjars.com/api/fetchJar/servers/{Software}/{Version}', out=WD)
            
                StartRam = (int(input('\nHow Much Ram Would you Like to Allocate to server in GB (ex: 13)')))
                print('Making eula.txt')
                f= open(f'{WD}eula.txt',"a")
                f.write('''
# Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)
eula=true
''')
            
            for i in range(count):
                incre = int(50.0 / count * i)
                sys.stdout.write('\r' + '|%s%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*incre + ' \033[27m', endColor, ' '*(50-incre), 2*incre)) if i != count - 1 else sys.stdout.write('\r' + '|%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*20 + 'COMPLETE!' + ' '*21 + ' \033[27m', endColor, 100))
                sys.stdout.flush()
                sleep(0.1)

            print('\neula.txt Made Continuing')
            print('Making Start File')

            if platform == 'Linux' or platform == 'linux' or platform == 'linux2':
                f= open(f'{WD}start.sh', 'a')
                f.write('#!/bin/bash')
                f.write(f'java -Xmx{StartRam}G -Xms{StartRam}G -jar {Software}-{Version}.jar --nogui')
                st = sts('start.sh')
                chmod('start.sh', st.st_mode | stat.S_IEXEC)

                for i in range(count):
                    incre = int(50.0 / count * i)
                    sys.stdout.write('\r' + '|%s%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*incre + ' \033[27m', endColor, ' '*(50-incre), 2*incre)) if i != count - 1 else sys.stdout.write('\r' + '|%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*20 + 'COMPLETE!' + ' '*21 + ' \033[27m', endColor, 100))
                    sys.stdout.flush()
                sleep(0.1)
                st = sts('start.sh')
                chmod('start.sh', st.st_mode | stat.S_IEXEC)
                break
            elif platform == 'darwin':
                f= open(f'{WD}start.sh', 'a')
                f.write(f'''#!/bin/bash
    # Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)

    java -Xmx{StartRam}G -jar {Software}-{Version}.jar -o true

                    ''')
                st = sts('start.sh')
                chmod('start.sh', st.st_mode | stat.S_IEXEC)


                for i in range(count):
                    incre = int(50.0 / count * i)
                    sys.stdout.write('\r' + '|%s%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*incre + ' \033[27m', endColor, ' '*(50-incre), 2*incre)) if i != count - 1 else sys.stdout.write('\r' + '|%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*20 + 'COMPLETE!' + ' '*21 + ' \033[27m', endColor, 100))
                    sys.stdout.flush()
                sleep(0.1)
                break
            elif platform == 'win32':
                f= open(f'{WD}start.bat', 'a')
                f.write(f'''
    # Made with Minecraft Server Creator by Kaleb Schmidlkofer on github(https://github.com/kalebschmidlkofer)

    @echo off
    title Server Console
    java -Xmx{StartRam}G -jar {Software}-{Version}.jar
    PAUSE
    ''')
                st = sts('start.bat')
                chmod('start.bat')

                for i in range(count):
                    incre = int(50.0 / count * i)
                    sys.stdout.write('\r' + '|%s%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*incre + ' \033[27m', endColor, ' '*(50-incre), 2*incre)) if i != count - 1 else sys.stdout.write('\r' + '|%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*20 + 'COMPLETE!' + ' '*21 + ' \033[27m', endColor, 100))
                    sys.stdout.flush()
                sleep(0.1)


                break        
    except KeyboardInterrupt:
        print('Keyboard Interrupt')

if __name__ == '__main__':
    main()

                    
