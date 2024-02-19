import requests
import json
from loguru import logger
from sys import stderr
import asyncio
from time import time

def debug_init(trace, debug):
    logger.remove()
    if debug:
        logger.add(stderr, level='DEBUG')
    elif trace:
        logger.add(stderr, level='TRACE')
    else:
        logger.add(stderr, level='INFO')

class ServerJars:
  def __init__(self):
    self._apie='https://serverjars.com/api'

  def input_data(self, category, software, version):
    self.category=category
    self.software=software
    self.version=version
    
  async def queue_types(self, category=None):
    start=time()
    getrequest = f'{self._apie}/fetchTypes'
    logger.trace(getrequest)
    response = await self.fetch(getrequest)
    self.fetchTypes = response
    self.categories = list(response.keys())
    end=time()
    logger.debug(f'Queue_types time: {end-start}')

  async def details(self, category, software, version=None):
    getrequest=f'{self._apie}/fetchDetails/{category}/{software}/{"" if None else version}'
    logger.info(getrequest)
    fetch=await self.fetch(getrequest)

  async def fetch(self, url):
    response = await asyncio.to_thread(requests.get, url)
    r=response.json()
    logger.debug(r)
    if r['status'] == 'success':
      return r['response']
    else:
      raise requests.exceptions.HTTPError('Failed to make request')

  async def jar_types(self, category=None):
    if category==None:
      return self.fetchTypes
    else:
      return self.fetchTypes[category]

debug_init(True, False)


async def main(jars:ServerJars):
  print(jars.categories)
  while True:
    category = input('Category: ')
    try:
      cat=jars.fetchTypes[category]
      print(cat)
      break
    except KeyError:
      logger.warning('Incorrect Category Type!')
  while True:
    software = input('Software: ')
    try:
      if software in cat:
        pass
      else:
        raise KeyError
      break
    except KeyError:
      logger.warning('Incorrect Software Type!')

  while True:
    version = input('Mc Version (Leave Blank for latest): ')
    detail=await jars.details(category, software, version)

  jars.input_data(category, software, version)
  print('done')


if __name__ == "__main__":
  jars = ServerJars()
  asyncio.run(jars.queue_types())
  asyncio.run(main(jars))
  