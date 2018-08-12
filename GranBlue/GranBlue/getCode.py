# encoding = 'utf-8'

import sys
sys.path.append('/home/ubuntu/project/GranBlue/GranBlue/')
import tweepy
import re
import sqlite3
from twitterAPIKey import access

api = access()


# database
conn = sqlite3.connect('/home/ubuntu/project/GranBlue/boss')
print("Linked to SQLite database !")
cursor = conn.cursor()


def divide(boss, level, code):
    level = int(level)
    cursor.execute('insert into GranBlueModel_granblue (name, level, code) values (?, ?, ?)', (boss, level, code,))

    print("Insert!")
    conn.commit()

# streaming
class GranBlueStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        pattern = r'^.*(\w{8}) :(Battle ID|参戦ID)\n(I need backup!|参加者募集！)\n(Lvl |Lv)(\d{2,3}) (.+)(https:.+){0,1}'
        matching = re.match(pattern, status.text)
        try:
            print(matching.group(6), matching.group(5), matching.group(1))
            divide(matching.group(6), matching.group(5), matching.group(1))
        except:
            print("Error")

streamer_listener = GranBlueStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamer_listener)
stream.filter(track=['Battle ID\nI need backup!\nLvl', u'参加者募集！'])
