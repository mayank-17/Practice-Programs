#!/usr/bin/env python3
import urllib.request
from urllib.error import URLError
import json

def get_json(url):
    result_bytes = urllib.request.urlopen(url)
    return json.loads(str(result_bytes.read(),'utf-8'))


MY_FID = "901432406596007"
ACCESS_TOKEN = "EAACEdEose0cBADnbRF5SA26ny88xAHCN0MP9qMdU9M3OOzihDZBV0SZAYwVWuBSTZC7CtjsZCM0PRLu6i3XOWzXkkomcZC1pGEeXSJqWZCYZCAsHXAumvUbHuYaW8ZAY9KsDEnAtaTlERgMO8QESDXr5urgW6ZBZC6zRjh4JDWZCxx4Evfui5CJyZAQpPGNZB6C0GRxG4E9HTRV3hdAZDZD"

FRIENDS_URL = "https://graph.facebook.com/901432406596007/friends?access_token=EAACEdEose0cBADnbRF5SA26ny88xAHCN0MP9qMdU9M3OOzihDZBV0SZAYwVWuBSTZC7CtjsZCM0PRLu6i3XOWzXkkomcZC1pGEeXSJqWZCYZCAsHXAumvUbHuYaW8ZAY9KsDEnAtaTlERgMO8QESDXr5urgW6ZBZC6zRjh4JDWZCxx4Evfui5CJyZAQpPGNZB6C0GRxG4E9HTRV3hdAZDZD"
MUTUAL_FRIENDS_URL= "https://graph.facebook.com/{me}/mutualfriends?user={user}&access_token={access_token}"

next_url = FRIENDS_URL.format(user="me", access_token=ACCESS_TOKEN)

friends = {}


while True:
    results = get_json(next_url)
    friends.update({obj['id']: {"name": obj['name']} for obj in results['data']})
    try: 
        next_url = results['paging']['next']
    except KeyError:
        break
    

for fid in friends.keys():
    print(friends[fid]['name'])
    try:
        url = MUTUAL_FRIENDS_URL.format(me=MY_FID, user=fid, access_token=ACCESS_TOKEN)
        friends_of_fid = get_json(url)
    except URLError:
        print("- failed")
        continue
    
    friends[fid]['friends'] = {obj['id']: obj['name'] 
                               for obj in friends_of_fid['data']}


with open('friends-of-friends.json','w') as f:
    json.dump(friends, f)
