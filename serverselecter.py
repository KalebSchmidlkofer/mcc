import requests
import json
from loguru import logger
from sys import stderr
import asyncio
import cProfile
from time import sleep
import time

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
    
  async def queue_types(self):
    start=time.time()
    getrequest = f'{self._apie}/fetchTypes'
    logger.trace(getrequest)
    response = await self.fetch(getrequest)
    self.fetchTypes = response['response']
    end=time.time()
    logger.debug(f'Queue_types time: {end-start}')

  async def fetch(self, url):
    response = await asyncio.to_thread(requests.get, url)
    return response.json()

  async def jar_types(self):
    return self.fetchTypes

  async def jar_details(self, jartype, category, version=None):
    if version is None:
      getrequest = f'fetchDetails/{jartype}/{category}'
    else:
      getrequest = f'fetchDetails/{jartype}/{category}/{version}'

  async def fetch_jar(self, category, software, version=None):
    if version == None:
      getrequest = f'{self._apie}/{category}/{software}'
    else: 
      getrequest = f'{self._apie}/{category}/{software}/{version}'

debug_init(True, False)
async def main(jars:ServerJars):
  print(jars.fetchTypes)
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
      
      break
    except KeyError:
      logger.warning('Incorrect Software Type!')
      
  version = input('Mc Version (Leave Blank for latest): ')
  jars.input_data(category, software, version)
  # print(await jars.jar_types())
  print('done')


if __name__ == "__main__":
  jars = ServerJars()
  asyncio.run(jars.queue_types())
  asyncio.run(main(jars))
  