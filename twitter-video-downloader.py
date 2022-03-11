import tweepy
from telegram import Update, ForceReply
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import wget
import os
import random
import string

wheres = [
    "Victorians once used leeches to predict the weather.",
    "Your funny bone is actually a nerve.",
    "The most requested funeral song in England is by Monty Python.",
    "Research shows that all blue-eyed people may be related.",
    "Charles Darwin's personal pet tortoise didn't die until recently.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "President Lyndon B. Johnson owned a water-surfing car.",
    "David Bowie helped topple the Berlin Wall.",
    "Cherophobia is the word for the irrational fear of being happy.",
    "You can hear a blue whale's heartbeat from two miles away.",
    "Nearly 30,000 rubber ducks were lost at sea in 1992 and are still being discovered today.",
    "The inventor of the frisbee was turned into a frisbee after he died.",
    "There's a bridge exclusively for squirrels.",
    "Subway footlongs aren't always a foot long.",
    "Marie Curie's notebooks are still radioactive.",
    "One in three divorce filings include the word 'Facebook.'",
    "Blood banks in Sweden notify donors when blood is used.",
    "Instead of saying 'cheese' before taking a picture, Victorians said 'prunes.'",
    "Roosters have built-in earplugs.",
    "The Netherlands is so safe, it imports criminals to fill jails.",
    "The world's largest pyramid isn't in Egypt.",
    "We may have already had alien contact.",
    "You can smell rain.",
    "Dolphins have actual names.",
    "Cold water is just as cleansing as hot water.",
    "Incan people used knots to keep records.",
    "Water bottle expiration dates are for the bottle, not the water.",
    "South Koreans are four centimeters taller than North Koreans.",
    "The world's most successful pirate was a woman.",
    "Pandas fake pregnancy for better care.",
    "Indians spend 10+ hours a week reading, more than any other country in the world.",
    "Pineapples were named after pine cones.",
    "The IKEA catalog is the most widely printed book in history.",
    "Crocodiles are one of the oldest living species, having survived for more than 200 million years.",
    "Doritos are flammable and can be used as kindling.",
    "It's illegal to own only one guinea pig in Switzerland.",
    "The first written use of 'OMG' was in a 1917 letter to Winston Churchill.",
    "Dead skin cells are a main ingredient in household dust",
    "There’s enough gold inside Earth to coat the planet"
]
token = "Telegram Token"
auth = tweepy.OAuthHandler("API KEY", "API SECRET")
auth.set_access_token("ACCESS KEY", "ACCESS SECRET")
api = tweepy.API(auth)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!'
    )
    update.message.reply_text('Send your Twitter link that has a video and I will send the video to you, right here! Crazy, right?')

def msgg(update: Update, context: CallbackContext) -> None:
    userid = update.message['chat']
    userid = userid['id']
    bott = telegram.Bot(token)
    links = re.findall("http\S+", update.message.text)
    #print(links)
    try:
        link = links[0]
        link = link.split('?')[0]
        tweetid = link.split('/')[-1]
        #print(tweetid)
        try:
            tweet = api.get_status(tweetid, tweet_mode="extended")._json
            try:
                if tweet['extended_entities']:
                    tweet = tweet['extended_entities']
                if tweet['media']:
                    tweet = tweet['media']
                    tweet = tweet[0]
                if tweet['video_info']:
                    tweet = tweet['video_info']
                    tweet = tweet['variants']
                    for i in tweet:
                        print(i)
                        if i['content_type'] == 'video/mp4':
                            video = i['url']
                    url = video.split('?')[0]
                    randomname = ''.join([random.choice(string.ascii_letters) for n in range(6)])
                    randomname = randomname + '.mp4'
                    wget.download(url, randomname)
                    bott.sendVideo(userid, video= open(randomname,"rb"))
                    os.remove(randomname)
            except:
                try:
                    update.message.reply_text('Your link sucks, check it before bothering me!')        
                except:
                    pass
        except:
            try:
                update.message.reply_text('You gotta be fucking kidding me!')
            except:
                pass
    except:
        try:
                
            bott.sendMessage(userid,"Where's the fucking link?")
            bott.sendMessage(userid,"Now that you don't have a link, here's a random fact for you:" + str(random.choice(wheres)))
        except:
            pass
def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, msgg))
    updater.start_polling()
    updater.idle()
while True:
    main()
