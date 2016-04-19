import random
import tweepy
import api_keys

class MyStreamListener(tweepy.StreamListener):
    ''' http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html '''
    
    def on_status(self,data):
        try:
            text = data.text
            replyid = data.id
            username = data.user.screen_name
            if '@morsehorse_bot' in text:
                reply = buildTweets(text, username)
                for tweet in reply:
                    print(tweet)
                    api.update_status(status=tweet, in_reply_to_status_id=replyid)
        except UnicodeError:
            pass
                    
def str2morse(x):
    morseDict = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
    ans = ''
    for c in x: 
        try:
            ans += morseDict[c.upper()]
        except:
            pass
            #print(c+' was ignored.')
    return ans
            
def morse2longshort(x):
    ans = ''
    for c in x:
        if c=='-':
            ans += 'LONG '
        elif c=='.':
            ans += 'SHORT '
    return ans
    
def apiSetup():
	CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET = api_keys.getKeys()
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api
	
def buildTweets(x, username):
    ''' Convert string x to a list of morse code tweets that tag @username '''
    spaceLeft = 140 - len(username) - 3
    if random.random()>0.5:
        all = str2morse(x)+str2morse("you're welcome i love you lol")
    else:
        all = morse2longshort(str2morse(x))
    i = 0
    tweets = []
    for c in all:
        if i%spaceLeft == 0:
            tweets.append('')
        tweets[-1] += c
        i += 1
    tweets = [tweet+' @'+username for tweet in tweets]
    return tweets
    
if __name__=='__main__':
    api = apiSetup()
    horseListener = MyStreamListener()
    horseStream = tweepy.Stream(auth=api.auth, listener=horseListener)
    horseStream.userstream()
    
    
    
    
 