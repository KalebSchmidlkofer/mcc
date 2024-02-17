import requests
import typer
import json
from loguru import logger
from sys import stderr
import asyncio

def debug_init(trace, debug):
    logger.remove()
    if debug:
        logger.add(stderr, level='DEBUG')
    elif trace:
        logger.add(stderr, level='TRACE')
    else:
        logger.add(stderr, level='INFO')
        pass
    pass

debug_init(True, False)

class ServerJars:
  def __init__(self):
    self._apie='https://serverjars.com/api'#Api Endpoint
  
  async def queue_data(self):
    getrequest=f'{self._apie}/fetchTypes'
    logger.trace(getrequest)
    JarTypeList = requests.api.get(getrequest)
    parsed = json.loads(JarTypeList.content)
    response=parsed['response']
    dumped = json.dumps(response, indent=4)
    self.fetchTypes=dumped
    
  async def jar_types(self):
    return self.fetchTypes



async def main():
  jars = ServerJars()
  await jars.queue_data()
  input('Fetch Jar Types? ')
  
  print(await jars.jar_types())
  


if __name__ == "__main__":
  asyncio.run(main())