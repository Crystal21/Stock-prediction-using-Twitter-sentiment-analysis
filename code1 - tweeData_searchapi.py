from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import MySQLdb
import time



conn = MySQLdb.connect("localhost","root","root","tweet")

conn.set_character_set('utf8')

c = conn.cursor()

c.execute('SET NAMES utf8mb4;')
c.execute('SET CHARACTER SET utf8mb4;')
c.execute('SET character_set_connection=utf8mb4;')


ckey =""
csecret = ""
atoken = ""
asecret =""

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

#change company and timeline, and truncate table
#10 days data available, including current date; exluding date in "until"

company = "Reliance"

#for tweet in tweepy.Cursor(api.search,q='BAJAJ-AUTO OR BAJFINANCE OR "BAJAJ AUTO LIMITED" OR "BAJAJ FINANCE LIMITED" OR BAJAJCORP OR BAJAJELEC OR BAJAJFINSV OR BAJAJHIND OR BAJAJHLDNG', lang="en", since='2017-03-13',until='2017-03-19').items():
#for tweet in tweepy.Cursor(api.search,q='TATACHEM OR TATACOMM OR TATAELXSI OR TATAGLOBAL OR TATAMOTORS OR TATAMTRDVR OR TATAPOWER OR TATASTEEL OR TCS OR TATACOFFEE OR TATAINVEST OR TATAMETALI OR TATASPONGE OR TTML', lang="en", since='2017-01-30',until='2017-02-05').items():
#for tweet in tweepy.Cursor(api.search,q='HEROMOTOCO OR "Hero Motocorp" OR HEROHONDA OR "Brijmohan Lall Munjal" OR "Pawan Munjal" OR "Hero Cycles"', lang="en", since='2017-03-13',until='2017-03-19').items():
for tweet in tweepy.Cursor(api.search,q='RCOM OR RELCAPITAL OR "RELIANCE JIO" OR "Reliance Industries" OR RELINFRA OR RPOWER OR RELBANK OR RDEL OR RELGOLD OR RELMEDIA', lang="en", since='2017-04-05',until='2017-04-06').items():
#for tweet in tweepy.Cursor(api.search,q='@TCS OR "Tata Consultancy Services" OR "Natarajan Chandrasekaran"', lang="en", since='2017-03-10',until='2017-03-11').items():
    print tweet.created_at, tweet.text
    c.execute("INSERT INTO tweets_data (time, username, tweet, company, date) VALUES (%s,%s,%s,%s,%s)",
            (time.time(), tweet.user.screen_name, tweet.text, company, tweet.created_at))
        
    conn.commit()
