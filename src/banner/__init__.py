
from colorama import Fore, Style

def banner():
  print(f"""\n
                    .__                
  ____   ____  __ __|  |  __ __  ______
 /  _ \_/ ___\|  |  \  | |  |  \/  ___/
(  <_> )  \___|  |  /  |_|  |  /\___ \ 
 \____/ \___  >____/|____/____//____  >
            \/                      \/                         
  """)

def info():
  print(f"""
  {Fore.CYAN}
  Autor: Higor Diego
  Website: http://higordiego.com.br
  Email: me@higordiego.com.br
  {Style.RESET_ALL}
  """)
