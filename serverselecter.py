import requests
import typer
import serverjars as sj

class ReleaseStates:
  STABLE = 'stable'
  EXPERIMENTAL = 'experimental'
  UNSTABLE = 'unstable'
  TESTING = 'testing'
  SNAPSHOT = 'snapshot'
  
class ServerTypes:
  BEDROCK='bedrock'
  MODDED='modded'
  PROXIES='proxies'
  SERVERS='servers'

class JarTypes:
  NUKKITX='nukkitx'
  POCKETMINE='pocketmine'
  MOHIST='mohist'
  FORGE='forge'
  CATSERVER='catserver'
  FABRIC='fabric'
  BUNGEECORD='bungeecord'
  VELOCITY='velocity'
  WATERFALL='waterfall'
  FLAMECORD='flamecord'
  BUKKIT='bukkit'
  PAPER='paper'
  SPIGOT='spigot'
  PURPUR='purpur'
  TUINITY='tuinity'
  SPONGE='sponge'
  SNAPSHOT='snapshot'
  VANILLA='vanilla'



class ServerJars:
  def __init__(self, software:ServerTypes, jartype):
    self.jartype = jartype
    self.software = software
    
    
  def list_types(self):
    '''Returns a list with all available types'''
    types = sj.fetchTypes()
    return types
  def list_jars(self, software):
    jars = sj.fetchAll(software)
    


soft=software()
jars=ServerJars(software.servers)
print(jars.list_types())
    