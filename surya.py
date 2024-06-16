# Decode by sukhix3pawan

from platform import system
import mechanize
import os
import time
import getpass
import requests
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
from platform import system
import sys

def testPY():
    if sys.version_info[0] < 3:
        print('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()
Z = '\x1b[0;90m'
M = '\x1b[38;5;196m'
H = '\x1b[38;5;46m'
K = '\x1b[38;5;226m'
B = '\x1b[38;5;44m'
U = '\x1b[0;95m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
HJ = '\x1b[38;5;208m'
A = '\x1b[38;5;248m'
xx = '\x1b[0;93m'
kk = '\x1b[93m'
hh = '\x1b[1;92m'
hi = '\x1b[32m'
uu = '\x1b[95m'
kk = '\x1b[33m'
bb = '\x1b[1;96m'
pp = '\x1b[0;34m'
Z2 = '[#000000]'
M2 = '[#FF0000]'
H2 = '[#00FF00]'
K2 = '[#FFFF00]'
B2 = '[#00C8FF]'
U2 = '[#AF00FF]'
N2 = '[#FF00FF]'
O2 = '[#00FFFF]'
P2 = '[#FFFFFF]'
J2 = '[#FF8F00]'
A2 = '[#AAAAAA]'

def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            pass
        else:
            try:
                if sys.version_info[0] < 3:
                    os.system('cd C:\\Python27\\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print(' [+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print(' [-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass
    return None
import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import rich
from rich import print as printer
from rich.panel import Panel
from platform import system
from datetime import datetime
try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()
requests.packages.urllib3.disable_warnings()

class FacebookBot:

    def _init_(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.set_handle_refresh(False)
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]

    def clear_screen(self):
        os.system('clear' if system() == 'Linux' else 'cls')

    def wait(self, seconds):
        time.sleep(seconds)

    def display_logo(self):
        clear = '\x1b[0m'
        colors = [35, 33, 36]
        logo_content = '\n..######..##.....##.########..##....##....###...\n.##....##.##.....##.##.....##..##..##....##.##..\n.##.......##.....##.##.....##...####....##...##.\n..######..##.....##.########.....##....##.....##\n.......##.##.....##.##...##......##....#########\n.##....##.##.....##.##....##.....##....##.....##\n..######...#######..##.....##....##....##.....##'
        for N, line in enumerate(logo_content.split('\n')):
            sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
            self.wait(0.3)

    def profile(self):
        profile_url = 'https://m.facebook.com/profile.php'
        response = self.browser.open(profile_url)
        html = response.read().decode('utf-8')
        account_name = None
        if '<title>' in html:
            start_index = html.index('<title>') + len('<title>')
            end_index = html.index('</title>')
            account_name = html[start_index:end_index]
            account_name = account_name.strip()
        if account_name:
            print('Active Account Name:', account_name)
        else:
            print(BOLD + GREEN + 'Unable to retrieve the account name.')
    print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')

    def login(self):
        login_url = 'https://m.facebook.com/login'
        self.browser.open(login_url)
        print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
        print(self.browser.title())
        emailx = getpass.getpass('➣Enter your email: ')
        pwx = getpass.getpass('➣Enter your password: ')
        self.browser.select_form(nr=0)
        self.browser.form['email'] = emailx
        self.browser.form['pass'] = pwx
        r = self.browser.submit()
        print(self.browser.title())
        if 'Facebook' in self.browser.title():
            print(' • Login sucessfull ✓ • ')
            self.wait(0.5)
        elif 'Enter login code to continue' in self.browser.title():
            print(' • 2FA enable in your account • ')
            self.browser.select_form(nr=0)
            msg1 = getpass.getpass('➣Enter 2-step Google code: ')
            self.browser.form['approvals_code'] = msg1
            r = self.browser.submit()
            self.browser.select_form(nr=0)
            self.browser.form['name_action_selected'] = ['save_device']
            r = self.browser.submit()
            print(self.browser.title())
            if 'Facebook' in self.browser.title():
                print(' • 2FA Login sucessfull ✓ • ')
        elif 'Login approval needed' in self.browser.title():
            print('CP GAI TERI ID ACHI ID LGA')
            sys.exit()
        elif 'Epsilon' in self.browser.title():
            print('LOCK GAI TERI ID')
            sys.exit()
        elif 'Review recent login' in self.browser.title():
            print('ID KO FB LITE ME OPEN KR, OR NOTIFICATION DEKH AYA HOGA RECENT LOGIN KA USKO ALLOW KRNE KE BAAD FIRSE LOGIN KR HO JAYEGA')
            sys.exit()
        else:
            print('incorrect username or password×')
            sys.exit()

    def main(self):
        self.clear_screen()
        print('<<<<<First You Have To Login Your account>>>>>>')
        mmm = requests.get('https://pastebin.com/raw/sKhp60ZQ').text
        print('')
        innn = getpass.getpass('[+] PASSWORD :: ')
        if mmm in innn:
            self.login()
            print('<<<<<<---Login successfully--->>>>>> ✓')
            self.wait(0.3)
            print('\x1b[35m', end='')
            self.clear_screen()
            self.display_logo()
            print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            self.browser.open('https://m.facebook.com/')
            print(self.browser.title())
            print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            self.profile()
            print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            num_posts = int(input('Enter the number of posts to comment on: '))
            print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            urls = []
            for i in range(num_posts):
                url = input(f'Enter the URL of post {i + 1}: ')
                urls.append(url)
                print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            speed = int(input('Enter Comment Speed (in seconds): '))
            print('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            while True:
                for i, url in enumerate(urls):
                    try:
                        self.browser.open(url)
                    except Exception as e:
                        print(e)
                    try:
                        self.browser.select_form(nr=0)
                        self.browser.form.find_control('comment_text').attrs['rows'] = '2'
                    except Exception as e:
                        print(e)
                    try:
                        self.browser.submit(name='post')
                        print(f'Comment posted on post {i + 1} ✓')
                    except Exception as e:
                        print(e)
                    self.wait(speed)
        print('[-] <==> Incorrect password! Please get approval from the owner.')
if _name_ == '_main_':
    bot = FacebookBot()
    bot.main()
