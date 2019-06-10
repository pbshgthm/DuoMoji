from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json,time

access_token = "1130553454164709376-YXFSIWp907KXVP7DvVyr2BxuhR7QZ3"
access_token_secret = "3KzeLHQfk2Rzy37yxUTr4C1vABtbUUJWoRTeRZ0e4LWxR"
consumer_key = "1p7f6bariy5GU4Qj0g8LDWWC1"
consumer_secret = "HxROOrHX2PbQzMYOPwypbf0LO2qWLh5M3oLyX96jrZ99t7Vi3i"

emoji=[
'😂','❤️','♻️','😍','♥️','😭','😊','😒','💕','😘',
'😩','☺️','👌','😔','😁','😏','😉','👍','⬅️','😅',
'🙏','😌','😢','👀','💔','😎','🎶','💙','💜','🙌',
'😳','✨','💖','🙈','💯','🔥','✌️','😴','😄','😑',
'😋','😜','😕','😞','😪','💗','👏','😐','👉','💞',
'💘','📷','😱','💛','🌹','💁','🌸','💋','😡','🙊',
'💀','😆','😈','😀','🎉','💪','😃','✋','😫','▶️',
'😝','💚','😤','💓','🌚','👊','✔️','➡️','😣','😓',
'☀️','😻','😇','😬','😥','✅','👈','😛','😷','😚',
'👑','👋','👇','🎧','🔴','😶','😖','😠','🌟','🎵']



track=['😭😂', '😂😭', '👌😄', '😍❤️', '😂💀', '😭❤️',
 '😂❤️', '💛💙', '😭💖', '😂💔', '😅😂', '😭💔', '😭💜',
 '☺️❤️', '💙💛', '😍😂', '👉👈', '😍🔥', '😭💕', '😍😘',
 '✨🔥', '💚💙', '🔥😈', '😍💕', '❤️😍', '😩😭', '😂😅',
 '😭😍', '😂💜', '😂💕', '💀😂', '😂😍', '😈🔥', '👑💕',
 '😁😂', '💙💚', '😎🔥', '💜✨', '😢💔', '😊😍', '✨💕',
 '✨😍', '😩❤️', '😂♥️', '😆😋', '💔😭', '😭♥️', '😍👌',
 '😳💀', '😔💔', '😏🔥', '💜💛', '😘😍', '😭💛', '😩😂',
 '😘❤️', '😍✨', '😂👍', '💪🔥', '😍♥️', '😍💜', '😊💕',
 '💙✨', '💙💜', '😍💙', '😍😋', '✨💜', '💜😍', '❤️💙',
 '👀😂', '😉😂', '😭💀', '😍😭', '🌟👑', '❤️😘', '🔥😎',
 '😭💙', '🎉🙌', '😍😎', '😉✨', '❤️😭', '❤️🔥', '🎶🎵',
 '😭😩', '😊❤️', '💙👍', '😂💙', '😉😘', '🙏❤️', '😂😩',
 '🙊🙈', '😝😂', '😢😭', '💕✨', '😂💯', '😂😆', '😂😁',
 '💀😭', '💛💚', '❤️✨']




archive={'0500': 2225, '0005': 1722, '1238': 1666,
'0301': 1028, '0060': 967, '0501': 841, '0001': 832,
'5327': 821, '0532': 814, '0024': 802, '1900': 662,
'0524': 660, '0528': 606, '1101': 534, '2753': 524,
'0300': 501, '4886': 464, '0335': 463, '0508': 413,
'0309': 405, '3135': 398, '7127': 338, '3562': 326,
'0308': 313, '0103': 312, '1005': 311, '0019': 295,
'0503': 289, '0028': 280, '0008': 274, '6000': 265,
'0003': 261, '6235': 260, '9008': 260, '1400': 254,
'2771': 242, '2535': 241, '2831': 233, '2224': 231,
'0603': 220, '3108': 212, '3103': 211, '1001': 205,
'0004': 204, '6140': 204, '2405': 203, '0504': 200,
'0312': 199, '3060': 198, '1324': 192, '1535': 191,
'2853': 189, '0903': 189, '0553': 187, '1000': 187,
'0901': 186, '0331': 185, '0017': 179, '6535': 179,
'0304': 178, '0328': 178, '0608': 169, '2731': 167,
'2728': 163, '0327': 162, '0340': 162, '3128': 161,
'2803': 158, '0127': 157, '2300': 156, '1600': 156,
'0560': 156, '0305': 152, '9890': 152, '0109': 151,
'3525': 151, '0527': 149, '6429': 148, '0325': 147,
'1631': 147, '0105': 145, '0135': 143, '2699': 143,
'0510': 142, '0601': 142, '2717': 138, '0027': 137,
'1609': 137, '2001': 137, '0010': 136, '5933': 135,
'7000': 134, '2205': 134, '0831': 134, '0034': 133,
'0061': 131, '0014': 131, '6005': 130, '5371': 129,
'0131': 129}




emEncode={}
for i in emoji:
    for j in emoji:
        emEncode[i+j]=str(emoji.index(i)).zfill(2)+str(emoji.index(j)).zfill(2)


class StdOutListener(StreamListener):

    def __init__(self, track):
        self.track=track

    def on_data(self, data):
        tweet=json.loads(data)
        if tweet['retweeted']:return
        if tweet['is_quote_status']:return
        if "extended_tweet" in tweet:
            txt = tweet['extended_tweet']['full_text']
        else:
            txt=tweet['text']

        found = [e for e in self.track if e in txt]
        if len(found)==0:  return
        pushBuffer(found[0])


    def on_error(self, status):
        print(status)


buffer=[]
def pushBuffer(item):
    global buffer, emEncode, archive
    archive[emEncode[item]]+=1
    buffer.append((emEncode[item],archive[emEncode[item]]))
    

def genMetadata(count):
    trails=[emEncode[i] for i in track[:count]]
    nodes=[i[:2] for i in trails]
    nodes+=[i[2:] for i in trails]
    nodes=list(set(nodes))
    return {'trails':trails,'nodes':nodes}

def trackStream():
    l = StdOutListener(track[:35])
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l,languages=["en"],tweet_mode='extended')
    stream.filter(track=track[:35],is_async=True)
    print('stream started')
