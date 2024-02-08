
from colorama import Fore, Style

def banner():
  print(f"""\n
    ▒█████   ▄████▄   █    ██  ██▓     ▒█████    ██████ 
    ▒██▒  ██▒▒██▀ ▀█   ██  ▓██▒▓██▒    ▒██▒  ██▒▒██    ▒ 
    ▒██░  ██▒▒▓█    ▄ ▓██  ▒██░▒██░    ▒██░  ██▒░ ▓██▄   
    ▒██   ██░▒▓▓▄ ▄██▒▓▓█  ░██░▒██░    ▒██   ██░  ▒   ██▒
    ░ ████▓▒░▒ ▓███▀ ░▒▒█████▓ ░██████▒░ ████▓▒░▒██████▒▒
    ░ ▒░▒░▒░ ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
      ░ ▒ ▒░   ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░
    ░ ░ ░ ▒  ░         ░░░ ░ ░   ░ ░   ░ ░ ░ ▒  ░  ░  ░  
        ░ ░  ░ ░         ░         ░  ░    ░ ░        ░  
            ░                                           
  """)

def info():
  print(f"""
  {Fore.CYAN}
  Autor: Higor Diego
  Website: http://higordiego.com.br
  Email: me@higordiego.com.br
  {Style.RESET_ALL}
  """)
