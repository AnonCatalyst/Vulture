import requests
import socket
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
import time
import sys
import os
import scanlib.js as js
import json
import googlesearch
import google



#Banner
print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠋⠉⢻⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠉⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠩⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Project: Vulture
⠀⠀⣀⣴⣾⣿⣿⣿⣿⠟⠁⠙⢿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Category: Username Search
⠀⠈⣩⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Developer: AnonCatalyst
⠀⠈⠉⠈⠟⠉⠀⠀⠀⠀⠀⠀⠀⣀⣽⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")


#Input
username = input("\nEnter a username: ")


#Animation 
def load_animation():
    load_str = f"vulture is launching username search..."
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
  
    while (counttime != 100):
        time.sleep(0.075) 
        load_str_list = list(load_str) 
        x = ord(load_str_list[i])
        y = 0                             
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        load_str = res

        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
        
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
        
if __name__ == '__main__': 
    load_animation()


#Username Search
print(f" {Fore.RED}〘{Fore.WHITE} Username Search{Fore.YELLOW}: {Fore.CYAN}{username}{Fore.RED} 〙\n")

from requests.exceptions import TooManyRedirects
def username_search(username):
    for url in open("urls.txt", "r").readlines():
        url = url.strip() + username
        try:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                print(f"{Fore.CYAN}• {Fore.BLUE}{username} {Fore.RED}| {Fore.YELLOW}[{Fore.GREEN}✓{Fore.YELLOW}]{Fore.WHITE} URL{Fore.YELLOW}: {Fore.GREEN}{url}{Fore.WHITE} {status_code}")
            else:
                if status_code == 404:
                    print(f"\n {Fore.CYAN}╘ {Fore.WHITE}Profile page {Fore.RED}not found{Fore.YELLOW}:{Fore.RED} {status_code}{Fore.WHITE}")
                    print(f"{Fore.YELLOW}[{Fore.RED}×{Fore.YELLOW}] {Fore.WHITE}URL{Fore.YELLOW}: {Fore.MAGENTA}{url}{Fore.WHITE}")

        except requests.exceptions.TooManyRedirects as err:
            print(f"\n{Fore.RED}╘{Fore.WHITE} Too many redirects{Fore.RED} !{Fore.WHITE}")
        except ValueError:
            print(f"\n{Fore.RED}╘{Fore.WHITE} Invalid username{Fore.YELLOW}:{Fore.RED} {username}{Fore.WHITE}")
        except IOError:
            print(f"\n{Fore.RED}╘{Fore.WHITE} File not found{Fore.YELLOW}:{Fore.RED} {url}{Fore.WHITE}")

if __name__ == "__main__":
    username_search(username)


print(f"\n {Fore.RED}〘 {Fore.WHITE}Domains Associated With{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")





# Username association
try:
    for link in googlesearch.search(username):
        if username in link:
            print(f"{Fore.CYAN}⊶ {Fore.WHITE}", link)
except google.cloud.exceptions.TooManyRequests:
    print(f"{Fore.RED}[!] Too many requests, please try again later.{Fore.WHITE}")
else:
    print(f"No Other Domains Associated With: {username}")



#Google Search
#print(f"\n {Fore.RED}〘 {Fore.WHITE}Google Search For{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")
#for urlx in googlesearch.search(username):
#    print(f"{Fore.CYAN}⊶ :{Fore.WHITE}",urlx)






import googlesearch
print(f"\n {Fore.RED}〘 {Fore.WHITE}Google Search For{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")
choice = input(f"\n{Fore.YELLOW}[{Fore.CYAN}?{Fore.YELLOW}]{Fore.WHITE} Do you want to print the results? {Fore.CYAN}({Fore.WHITE}y{Fore.MAGENTA}/{Fore.WHITE}n{Fore.CYAN}){Fore.YELLOW}:{Fore.WHITE} ").lower()
if choice == "y":
    with open("usrassosiation.txt", "w") as f:
        for urlx in googlesearch.search(username):
            f.write(f"{urlx}\n")
            print(f"{Fore.CYAN}⊶ :{Fore.WHITE}",urlx)
    print("Results saved to usrassosiation.txt")
else:
    print("Results not saved")






