import sys
import time
import requests
import json
import telepot
import re
import tweepy
import subprocess
import os
import string
import random
from datetime import datetime
from telepot.loop import MessageLoop
import wget 

# IMGUR CREDENTIALS 
client_id = "PUT YOUR IMGUR CLIENT ID HERE" # put your client ID here
headers = {'Authorization': 'Client-ID ' + client_id}
# TELEGRAM CREDENTIALS
TOKEN2 = "" #PUT YOUR TELEGGRAM BOT CREDS HERE 

# TWITTER CREDENTIALS 
auth = tweepy.OAuthHandler("TWITTER API KEY"  , "TWITTER API SECRET ")
auth.set_access_token("TWITTER ACCESS TOKEN", "TWITTER ACCESS SECRET")
import tweepy 
api = tweepy.API(auth)
#SEARCH ENGINES
baseurl = "GOOGLE: https://images.google.com/searchbyimage?image_url="
yandex = "YANDEX: https://yandex.com/images/search?rpt=imageview&url="
tineye0 = "TINEYE: https://tineye.com/search/?url="

#CODE BEGINS 

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'photo' and  "channel" not in chat_type:
        photoz= msg['photo']
        letters = string.ascii_letters
        name = ''.join(random.choice(letters) for i in range(10))        
        for i in photoz:
            fileid = i['file_id']
            qqq = bot.getFile(fileid)
            path = qqq['file_path']
            url = "https://api.telegram.org/file/bot" + TOKEN2 + "/" + path    
            if os.path.exists(str(name) + ".jpg"):
                os.remove(str(name) + ".jpg")
            wget.download(url, str(name) + ".jpg")
        with open(str(name) + ".jpg", "rb") as imagefile:
                filetoupload = imagefile.read()
                qq = requests.post("https://api.imgur.com/3/upload.json", data= {"image": filetoupload} ,headers=headers)
                pp = qq.json()
                imgurdata = pp['data']
                imgurlink =  imgurdata['link']     
                bot.sendMessage(chat_id, str(baseurl) + str(imgurlink) + "\n\n" + str(yandex) + str(imgurlink) + "\n\n" + str(tineye0) + imgurlink  ,disable_web_page_preview=True)
                imagefile.close()
                if os.path.exists(str(name) + ".jpg"):
                    os.remove(str(name) + ".jpg")                
    elif content_type == 'text':
        try:
            a = msg['text']
            a = re.findall(r'[0-9]{10,25}',a)[-1]
            tweet = api.get_status(a, tweet_mode="extended")._json
            tweet = tweet['entities']
            tweet = tweet['media'][0]
            tweet = tweet['media_url_https']
            yandex1 = "YANDEX: https://yandex.com/images/search?rpt=imageview&url=" + tweet
            tieye = "TINEYE: https://tineye.com/search/?url=" + tweet
            tweet = "GOOGLE: https://images.google.com/searchbyimage?image_url=" + tweet
            bot.sendMessage(chat_id,str(tweet) + "\n\n" + str(tieye) + "\n\n" + str(yandex1),disable_web_page_preview=True)
        except:
            pass
bot = telepot.Bot(TOKEN2)
MessageLoop(bot, handle).run_as_thread()
print('\n' + 'Listening..')
while 1:
    time.sleep(10)
