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
  chmod('start.sh', st.st_mode)

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

@app.command()
def purpur(
  version: str = typer.Argument(default=findjar('servers', 'purpur')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='purpur'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, 'purpur')

@app.command()
def paper(
  version: str = typer.Argument(default=findjar('servers', 'paper')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='paper'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, servertype)

@app.command()
def bukkit(
  version: str = typer.Argument(default=findjar('servers', 'bukkit')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='bukkit'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, servertype)

@app.command()
def spigot(
  version: str = typer.Argument(default=findjar('servers', 'spigot')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='spigot'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, servertype)

@app.command()
def tuinity(
  version: str = typer.Argument(default=findjar('servers', 'tuinity')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='tuinity'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, servertype)

@app.command()
def sponge(
  version: str = typer.Argument(default=findjar('servers', 'sponge')),
  ram: str = typer.Argument(default='14'),
  latest: bool = typer.Option(False, '-l', '--latest'),
):
  servertype='sponge'
  if latest:
    print(findjar('servers', servertype))
    # latestjardwnld("servers", servertype)
  else:
    latestjardwnld("servers", servertype, version)
    startsh(ram, version, servertype)


if __name__ == "__main__":
  app()