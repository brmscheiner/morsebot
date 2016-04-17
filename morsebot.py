import tweepy,random,api_keys,topusers

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
            
def twitterSetup():
	CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET = api_keys.getKeys()
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api
	
def buildTweets(x,n):
    ''' n is the number of spare characters '''
    all = str2morse(x)+str2morse("you're welcome i love you lol")
    i = 0
    tweets = []
    for c in all:
        if i%n == 0:
            tweets.append('')
        tweets[len(tweets)-1] += c
        i += 1
    return tweets
    
if __name__=='__main__':
    api = twitterSetup()
    # twt = api.search('the')
    twt = api.search('@morsehorse_bot')
    for s in twt:
        try:
            spaceLeft = 140 - len(s.user.screen_name) - 3
            reply = buildTweets(s.text, spaceLeft)
            print(s.text)
            print(s.user.screen_name)
            for each in reply:
                api.update_status(each+' @'+s.user.screen_name)
        except UnicodeEncodeError:
            print('ignoring a tweet')
        #str2morse('hello')



 