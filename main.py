import requests
import random
from colorama import Fore
import os
import sys
import string
import threading
from threading import Thread

made = 0
url = "https://spclient.wg.spotify.com/signup/public/v1/account"
headers = {
  'authority': 'spclient.wg.spotify.com',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'content-type': 'application/x-www-form-urlencoded',
  'accept': '*/*',
  'origin': 'https://www.spotify.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.spotify.com/',
  'accept-language': 'en-US,en;q=0.9'
}


def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# Yes i fucked my mind 3 hrs trying to figure out how can i do it and i failed and i raged over my keyboard :D
def mainfunction():
    global made
    while True:
        try:
            Email = random_char(10)+"@protonmail.com"
            password = random_char(20)
            payload = f'birth_day=2&birth_month=02&birth_year=1989&collect_personal_info=undefined&creation_flow=&creation_point=https%3A%2F%2Fwww.spotify.com%2Fus%2F&displayname=DreamyOnTop&gender=male&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&platform=www&referrer=&send-email=0&thirdpartyemail=1&email={Email}&password={password}&password_repeat={password}'
            response = requests.request("POST", url, headers=headers, data=payload)
            print(f"{Email}:{password}")
            save = open("accounts.txt", "a")
            save.write(Email + ":" + password + "\n")
            made+=1
        except Exception as e:
            pass

def title():
    global made
    while True:
        os.system(f"title Accounts: [{made}]")
thread = threading.Thread(target=title)
thread.start()

def start():
    for i in range(100): 
        try:
            threading.Thread(target=mainfunction, args=(), daemon=True).start()
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    start()
