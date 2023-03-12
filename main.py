import os
import threading, requests, time
from colorama import Fore, init
from pystyle import *

init()
os.system("clear")

token = input(f"{Fore.BLUE}[{Fore.WHITE}?{Fore.BLUE}] {Fore.WHITE}Token {Fore.BLUE}: {Fore.WHITE}")
threads = input(f"{Fore.BLUE}[{Fore.WHITE}?{Fore.BLUE}] {Fore.WHITE}Threads {Fore.BLUE}: {Fore.WHITE}")

ids = []
thread_lst = []

#krizz = commands.Bot(command_prefix="krizz", intents=discord.Intents.all(), self_bot=True)

class Counter:
  
  id_count = 0
  
  success  = 0
  failed   = 0


def dm(id, message):

  s = requests.session()

  headers = {
    "Authorization": token, 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
  }
  json = {
    "content": message,
    "tts": False
  }
  
  s_resp = s.post(f"https://discord.com/api/v9/channels/{id}/messages", headers = headers, json = json)

  if s_resp.status_code in (200, 201, 204):

    Counter.success += 1
    print(f"{Fore.BLUE}[{Fore.RED}+{Fore.BLUE}]{Fore.WHITE} Posted Message In {Fore.RED}{id}{Fore.WHITE}")
  
  else:

    Counter.failed += 1
    print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}]{Fore.WHITE} Couldnt Post Message In {Fore.RED}{id}{Fore.WHITE}")

def main():
  global thread_lst
  
  headers = {
    "Authorization": token, 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
  }
  resp = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
  for id in resp.json():
      ids.append(id['id'])
      Counter.id_count += 1

  print(f"{Fore.BLUE}[{Fore.RED}+{Fore.BLUE}]{Fore.WHITE} Scraped {Fore.RED}{Counter.id_count} {Fore.WHITE}Ids To Do")
  time.sleep(5)


  
  banner = """
 ███▄ ▄███▓ ▄▄▄        ██████   ██████    ▓█████▄  ███▄ ▄███▓
▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▒██    ▒    ▒██▀ ██▌▓██▒▀█▀ ██▒
▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄      ░██   █▌▓██    ▓██░
▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒   ░▓█▄   ▌▒██    ▒██ 
▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒   ░▒████▓ ▒██▒   ░██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ▒▒▓  ▒ ░ ▒░   ░  ░
░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░    ░ ▒  ▒ ░  ░      ░
░      ░     ░   ▒   ░  ░  ░  ░  ░  ░      ░ ░  ░ ░      ░   
       ░         ░  ░      ░        ░        ░           ░   
                                           ░                 
                                           
                 discord.gg/transphobic"""
  _banner = Colorate.Horizontal(Colors.blue_to_cyan, banner, 2)
  
  os.system("clear")
  os.system("title Mass Dm Menu gg./transphobic")
  print("")
  print("")
  #print("")
  #print("")
  print(_banner)

                    
  msg = input(f"\n\n{Fore.BLUE}[{Fore.WHITE}?{Fore.BLUE}] {Fore.WHITE}Message {Fore.BLUE}: {Fore.WHITE}")
  time.sleep(3)
  
  print(f"{Fore.BLUE}[+]{Fore.WHITE} Dming {Fore.BLUE}{Counter.id_count}{Fore.WHITE} IDs")
  
  for x in ids:

      thread_m = threading.Thread(target=dm, args=(x,msg))
      thread_lst.append(thread_m)
      thread_m.start()
      #thread_m.join()

      if len(thread_lst) == threads:
        time.sleep(1)
        thread_lst = []

  print(f"\n\n{Fore.BLUE}[+]{Fore.WHITE} Dmed {Fore.BLUE}{Counter.id_count}{Fore.WHITE} IDs")
  print(f"{Fore.BLUE}[+]{Fore.WHITE} Success {Fore.BLUE}{Counter.success}{Fore.WHITE} Requests")
  print(f"{Fore.BLUE}[-]{Fore.WHITE} Failed  {Fore.BLUE}{Counter.failed}{Fore.WHITE} Requests")

  time.sleep(5)
  input()
  exit()
  




os.system("clear")
main()

#krizz.run(token, bot=False)