from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time, datetime
import json



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
        
        username = all_data["user"]["screen_name"]

        #date = datetime.datetime(all_data["created_at"]).strftime('%Y-%m-%d %H:%M:%S')
        
        c.execute("INSERT INTO tweets_data (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        #print data
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["BHARTIARTL","YESBANK","happy","sad"])
