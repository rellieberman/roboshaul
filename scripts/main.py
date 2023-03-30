import os
import urllib
import csv

import readData
import urllib
import requests
import json


token = r"38583232097341dce437b4a897e96cc12da7cf8845cf401a09133b79fefb89fa"


def getPhon(urlText):
    global token
    address = r"https://alittlehebrew.com/transliterate/get.php?token=" + token +"&style=140_ipa&syllable=auto&accent=auto&hebrew_text="

    headers = {
     #   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie":  "PHPSESSID=56aff47d7063d7e31829691f7f993d9f",
    "Host": "alittlehebrew.com",
    "Referer" : "https://alittlehebrew.com/transliterate/",
    "Sec-Fetch-Dest" : "empty",
    "Sec-Fetch-Mode" : "cors",
    "Sec-Fetch-Site": "same-origin",

    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "X-Requested-With" : "XMLHttpRequest"
    }

    r = requests.get(address+urlText, headers=headers)
    string = r.content.decode('utf-8')
    json_obj = json.loads(string)
    pass
    while not json_obj['success']:
        print('enter fresh token')
        token = input()
        address = r"https://alittlehebrew.com/transliterate/get.php?token=" + token + "&style=140_ipa&syllable=auto&accent=auto&hebrew_text="
        r = requests.get(address + urlText, headers=headers)
        string = r.content.decode('utf-8')
        json_obj = json.loads(string)
    ans = json_obj['result'].replace("</strong>", "")[:-1]
    return ans




root_path = r"/home/nerya/Downloads/Roboshaul/saspeech_gold_standard"
meta_file = r"metadata.csv"
items = readData.ljspeech(root_path, meta_file)

if os.path.isfile("name.csv"):
    lines = 0
    # iterating through the whole file
    for row in open("name.csv"):
        lines += 1
    pass
else:
    lines = 0

with open(r'name.csv', 'a') as f:

    writer = csv.writer(f, quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')
    for i in range(lines+2, len(items)):
        text = items[i]['text']
        #print("text: ", text)
        urlText = urllib.parse.quote(text)
        phon = getPhon(urlText)
        #print('phonem: ', phon)
        csvText = items[i]['wav']+"|"+phon+"|"+phon
        writer.writerow([csvText])
        print(i)


