

from os import system
from colorama import Fore,init
from random import choice

init()

def clr():
    system("cls")

def startprint():
    system('mode con: cols=113 lines=32')
    clr()
    print(f"""
                        {Fore.WHITE}██████{Fore.RED}╗ {Fore.WHITE}██{Fore.RED}╗  {Fore.WHITE}██{Fore.RED}╗ {Fore.WHITE}█████{Fore.RED}╗ {Fore.WHITE}██████{Fore.RED}╗  {Fore.WHITE}██████{Fore.RED}╗ {Fore.WHITE}███████{Fore.RED}╗        {Fore.WHITE}██{Fore.RED}╗  {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}
                        ██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔═══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔════╝        ╚{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╔╝{Fore.WHITE}
                        ██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}║{Fore.WHITE}███████{Fore.RED}║{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}███████{Fore.RED}╗         ╚{Fore.WHITE}███{Fore.RED}╔╝ {Fore.WHITE}
                        ██{Fore.RED}╔═══╝ {Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}╔══{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║╚════{Fore.WHITE}██{Fore.RED}║         {Fore.WHITE}██{Fore.RED}╔{Fore.WHITE}██{Fore.RED}╗{Fore.WHITE} 
                        ██{Fore.RED}║     {Fore.WHITE}██{Fore.RED}║ {Fore.WHITE} ██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║  {Fore.WHITE}██{Fore.RED}║╚{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}║        {Fore.WHITE}██{Fore.RED}╔╝ {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}
                        {Fore.RED}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝        ╚═╝  ╚═╝
    
-----------------------------------------------------------------------------------------------------------------
    """)                  
                        
                        
    print(f"                    {Fore.WHITE}                        [{Fore.RED}+{Fore.WHITE}] username {Fore.RED}:{Fore.WHITE} ",end="")
    username=input()
    print(f"                    {Fore.WHITE}                        [{Fore.RED}+{Fore.WHITE}] password {Fore.RED}:{Fore.WHITE} ",end="")
    password=input()
    

startprint()
    

