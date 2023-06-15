import requests, os, colorama
from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style
import threading
import random
from flask import Flask, render_template, request
from colorama import Fore, Back, Style
import time
import sys
import os
import scanlib.js as js
import googlesearch
import urllib3
import logging
import urllib.parse
import platform
import getpass
os.system("clear")
print("""
 Project: Vulture
 Category: Username Search
 Developer: AnonCatalyst
   [1] ~ Terminal
   [2] ~ Web UI
--------------------
 00 ~ close program""")
menu_options = {
    ' 1': 'Terminal',
    ' 2': 'Web UI',
    " 00": 'Exit',
    }
def option1():
     os.system("clear && python3 term.py")
def option2():
     os.system("clear && python3 web.py")
if __name__=='__main__':
    while(True):
        option = ''
        try:
            option = int(input('\n Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 00:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
        break
