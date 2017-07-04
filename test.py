
from mastodon import Mastodon
import os, datetime, sys
import requests
import json


def mastodon_bot(botname, email, password, instance_url='https://octodon.social'):
    # This will be used to generate unique names for files containing your credentials
    # So that you could run several bots with different accounts
    account_name = email+"_"+instance_url.replace("https://","")+"_"

    # Create app if doesn't exist
    if not os.path.isfile(account_name + "clientcred.txt"):
        print("Creating app")
        mastodon = Mastodon.create_app(
            botname,
            to_file = account_name + 'clientcred.txt',
            api_base_url=instance_url
        )
    
    # Fetch access token if I didn't already
    if not os.path.isfile(account_name + "usercred.txt"):
        print("Logging in")
        mastodon = Mastodon(
            client_id = account_name + 'clientcred.txt',
            api_base_url=instance_url        
        )
        mastodon.log_in(email, password, to_file = account_name + 'usercred.txt')
    
    # Login using generated auth
    mastodon = Mastodon(
        client_id = account_name + 'clientcred.txt',
        access_token = account_name + 'usercred.txt',
        api_base_url=instance_url    
    )
    print(botname + " logged in as " + email + " at " + instance_url)

    return mastodon


with open('config.json', 'r') as f:
    config = json.load(f)

try:
    # Can also pass the rebooster account credentials as arguments
    botname = "AutoboosterBot"
    email =  sys.argv[2]
    password =  sys.argv[3]
    instance_url =  sys.argv[4]
except:
    botname = config["botname"]
    email = config["email"]
    password = config["password"]
    instance_url = config["instance_url"]

# Log into mastodon
mastodon = mastodon_bot(botname, email, password, instance_url)

# GET POST DATA
r = requests.get('https://red.trackerstatus.info/api/all/')
data = r.json()

tests = "Website","TrackerHTTP","TrackerHTTPS","IRC","IRCTorrentAnnouncer","IRCUserIdentifier",

postData = "Redacted status: \n \n"

for test in tests:
    if data[test]['Status']:
        latency = data[test]['Latency']
        postData += (str(test + " Is Up and has a latency of " + latency + '\n'))


mastodon.toot(postData)