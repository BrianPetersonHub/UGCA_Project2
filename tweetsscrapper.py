from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


#consumer key, consumer secret, access token, access secret.
ckey="mCbv27Y6SqDq96tDzOj6z5YcN"
csecret="JUogCrlK5f3LooV1bK78SYO0pElaMlrUZA6Pe7N5s0ZOSbcvvY"
atoken="837422129033396224-DzF8IzNNOLqKZfpMyH16QWnwyO0IzWz"
asecret="H3gNryD1U6nIqKyjMmeHVNjOHrgb98THHgT1E0OOFHk2x"

class listener(StreamListener):

    def on_data(self, data):
        try:
            with open('Oct14thTweetMine.json','a') as f:
                f.write(data)
                print(data)
                return(True)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Texas Senate", "Texas Senate Race", "Texas Senate Elections", "TexasSenate2018",
                           "TexasSenate", "SenateRaceTexas", "TexasElection","TexasSenateRace","#betoorourke","#cancruz","#votetexas"])