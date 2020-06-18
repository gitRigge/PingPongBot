import twitter
import re

api = twitter.Api(
    consumer_key='xxxxx',
    consumer_secret='xxxxx',
    access_token_key='xxxxx',
    access_token_secret='xxxxx'
)

file = open("last_id","r")
id_str = file.read()
file.close()
try:
    id = int(id_str)
except:
    id=None
print('Ping-Pong-Bot: since_id = {}'.format(str(id)))

mentions = api.GetMentions(count=None, since_id=id, max_id=None, trim_user=False, contributor_details=False, include_entities=True, return_json=True)
print('Ping-Pong-Bot: number of mentions = {}'.format(len(mentions)))

for mention in mentions:
    text = text = mention['text']
    id = mention['id']
    tags = {tag.strip("#") for tag in text.split() if tag.startswith("#")}
    print('Ping-Pong-Bot: current id = {}'.format(str(mention['id'])))
    if 'ping' in tags:
        print('Ping-Pong-Bot: mention contains "ping" hashtag')
        moti = {}
        with open('motivate/motivate/data_unique/unique_quotes.json') as f:
            moti.update(json.load(f))
        fortuneint = random.randint(0, len(moti['data']))
        print('Ping-Pong-Bot: fortune integer = {}'.format(str(fortuneint)))
        fortunestr = moti['data'][fortuneint]['quote']
        screen_name = mention['user']['screen_name']
        if len(moti['data'][fortuneint]['quote']) < 279:
            retweet_text = '@{} {} #pong'.format(screen_name, fortunestr)
        else:
            retweet_text = '@{} Here is your #pong :-)'.format(screen_name)
        print('Ping-Pong-Bot: retweet')
        retweet = api.PostUpdates(retweet_text, in_reply_to_status_id=id)
    else:
        print('Ping-Pong-Bot: mention does not contain "ping" hashtag')

file = open("last_id","w")
file.write(str(id))
file.close()
print('Ping-Pong-Bot: file written and closed')