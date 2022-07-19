import tweepy,time,json
import json,os
import pandas as pd
from pprint import pprint
from pandas import DataFrame as df
import wget
bearer = ""
apikey = ""
apist = ""
accesstk = ""
accessst = ""
client = tweepy.Client(bearer, apikey, apist, accesstk, accessst)
auth = tweepy.OAuth1UserHandler(apikey, apist, accesstk, accessst)
api = tweepy.API(auth)

words = ["Enter the filter words to stream"]

class sth(tweepy.Stream):
    def on_data(self, data):
        now = int(time.time())
        userdata = []
        q = json.loads(data)
        text = q["text"]
        print(text)
        user = q['user']
        handler = user['screen_name']
        tweetid = str(q['id'])
        tweetlink =  f"https://twitter.com/{handler}/{status}/{tweeitd}"
        userid = user['id_str']
        name = user['name']
        screen_name = user['screen_name']
        description = user['description']
        pp = user['profile_image_url']
        pp = pp.replace("_normal.png",".png")
        pp = pp.replace("_normal.jpg",".jpg")
        #print(pp)
        try:
            pb = user['profile_banner_url']
        except:
            pb = ""
        userdataset = {
            'id': userid,
            'screen_name': screen_name,
            'description': description,
            'handler': handler,
            'name': name,
            'pp': pp,
            'pb': pb,
            'logged_at': str(now)
        }
        userdata.append(userdataset)
        user_df = pd.DataFrame(userdata)
        file_exists = os.path.isfile("persiandb.csv")
        exportfile = "persiandb.csv"
        df1 = pd.read_csv("persiandb.csv")
        print(int(userid) in set(df1['id']))
        if not (int(userid) in set(df1['id'])):
            path = './pictures/'
            try:
                wget.download(url = pp,out = path + str(userid) + ".jpg")
            except:
                pass
            try:
                wget.download(url = pb,out = path + str(userid) + "-banner.jpg") 
            except:
                pass
            if not file_exists:
                user_df.to_csv(exportfile,encoding='utf-8',index=False)
            else:
                user_df.to_csv(exportfile,encoding='utf-8',mode='a', index=False, header=False)
while True:
    print("Streaming")
    stream = sth(apikey,apist,accesstk,accessst)
    stream.filter(track=words,languages=["fa"])
