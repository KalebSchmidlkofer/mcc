#!/home/kaleb/bin/mccVar/.mcc/bin/python
import typer
import requests
import json
import click
from os import getcwd, chmod, stat as sts
from tqdm import tqdm
import time

class NaturalOrderGroup(click.Group):
  def list_commands(self, ctx):
      return self.commands.keys()       

startscript = '''
#!/bin/bash
java -Xmx{StartRam}G -jar {Software}-{Version}.jar -o true
'''.strip()

serverjar="https://serverjars.com"
WorkinDirectory = getcwd()
WD = f'{WorkinDirectory}/'
app = typer.Typer(add_completion=False, )

def startsh(ram, version, jartype):
  f= open(f'{WD}start.sh', 'a')
  f.write('#!/bin/bash\n')
  f.write(f'java -Xmx{ram}G -Xms{ram}G -jar {jartype}-{version}.jar --nogui -o true')
  st = sts('start.sh')
  chmod(f'{WD}start.sh', 0o755)

def latestjar(type, category):
  url = f"{serverjar}/api/fetchLatest/{type}/{category}"
  response=requests.get(url)
  if response.status_code == 200:
    data=json.loads(response.text)
    version = data["response"]["version"]
    return version
  else:
    return 'Failed to fetch data from api'

def latestjardwnld(category, type, version=None):
  url = f"{serverjar}/api/fetchJar/{category}/{type}"
  response = requests.get(url, stream=True)
  if not version == None:
      if response.status_code == 200:
          file = f"{type}-{findjar(category, type)}.jar" if version else f"{type}.jar"
          total_size = int(response.headers.get("Content-Length", 0)) or 100000000 # set a default size of 100MB
          block_size = 1024
          progress = tqdm(total=total_size, unit="B", unit_scale=True)
          with open(file, "wb") as f:
              for data in response.iter_content(block_size):
                  progress.update(len(data))
                  f.write(data)
          progress.close()
  else:
      if response.status_code == 200:
        file = f"{type}-{version}.jar" if version else f"{type}.jar"
        total_size = int(response.headers.get("Content-Length", 0)) or 100000000 # set a default size of 100MB
        block_size = 1024
        progress = tqdm(total=total_size, unit="B", unit_scale=True)
        with open(file, "wb") as f:
          for data in response.iter_content(block_size):
            progress.update(len(data))
            f.write(response.content)
        progress.close()

def findjar(type, category, version=None):
  if version == None:
    return (latestjar(type, category))
  url = f'{serverjar}/api/fetchDetails/{category}/{type}/{version}'
  response=requests.get(url)
  if response.status_code == 200:
    data=json.loads(response.text)
    filename=data["response"]["file"]
    return filename

@app.command('vanilla')
def vanilla(
  version: str = typer.Argument(default=findjar('vanilla', 'vanilla')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='vanilla'
  apilocation='vanilla'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, apilocation)

@app.command('snapshot')
def snapshot(
  version: str = typer.Argument(default=findjar('vanillia', 'snapshot')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='snapshot'
  apilocation='vanilla'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('purpur')
def purpur(
  version: str = typer.Argument(default=findjar('servers', 'purpur')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='purpur'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('paper')
def paper(
  version: str = typer.Argument(default=findjar('servers', 'paper')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='paper'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('bukkit')
def bukkit(
  version: str = typer.Argument(default=findjar('servers', 'bukkit')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='bukkit'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('spigot')
def spigot(
  version: str = typer.Argument(default=findjar('servers', 'spigot')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='spigot'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('tuinity')
def tuinity(
  version: str = typer.Argument(default=findjar('servers', 'tuinity')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='tuinity'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)

@app.command('sponge')
def sponge(
  version: str = typer.Argument(default=findjar('servers', 'sponge')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='sponge'
  apilocation='servers'
  if latest:
    print(findjar(apilocation, servertype))
  else:
    latestjardwnld(apilocation, servertype, version)
    startsh(ram, version, servertype)


if __name__ == "__main__":
  app()