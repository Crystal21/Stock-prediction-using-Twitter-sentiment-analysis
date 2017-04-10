from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time, datetime
import json
#import sentiment_mod as s



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","root","tweet")

conn.set_character_set('utf8')

c = conn.cursor()

c.execute('SET NAMES utf8mb4;')
c.execute('SET CHARACTER SET utf8mb4;')
c.execute('SET character_set_connection=utf8mb4;')

#consumer key, consumer secret, access token, access secret.
ckey="kXcUvaiGIos4q7F2c6RnBDZsy"
csecret="tMlaXBesvtZOyMAmiz9ZAPnM7yq771CJERsG8wy2NucPWCG5ni"
atoken="135456971-MUmWpofCJgMjhLa1lXcC3Kn5GPB1Ons9RAqUVozt"
asecret="BDzJl29MVuL8m7rVjcZFjTMHuVEFIxJaqR99M7gUjxh3X"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        #sentiment_value, confidence = s.sentiment(tweet)
        
        username = all_data["user"]["screen_name"]

        custom_date = all_data["created_at"]
        
        #c.execute("INSERT INTO tweets_data (time, username, tweet, sentiment_of_tweet, confidence_of_sentiment, date) VALUES (%s, %s, %s, %s,%s,%s)",
            #(time.time(), username, tweet, sentiment_value, confidence, custom_date))

        c.execute("INSERT INTO tweets_data (time, username, tweet, date) VALUES (%s,%s,%s,%s)",
            (time.time(), username, tweet, custom_date))
        
        conn.commit()

        print((username,tweet, custom_date))
        #print data
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["TATACHEM","TATACOMM","TATAELXSI","TATAGLOBAL","TATAMOTORS","TATAMTRDVR","TATAPOWER","TATASTEEL","TCS","TATACOFFEE","TATAINVEST","TATAMETALI","TATASPONGE","TTML"])
twitterStream.filter(track=["BAJAJ-AUTO","BAJFINANCE","BAJAJ AUTO LIMITED","BAJAJ FINANCE LIMITED","BAJAJCORP","BAJAJELEC","BAJAJFINSV","BAJAJHIND","BAJAJHLDNG"])
