# RedactedMastodonStatus
Toot the server status and latency of several Redacted services.
# Install 

Clone this repo and cd into it:

```
git clone https://github.com/NeuroWinter/RedactedMastodonStatus.git
cd RedactedMastodonStatus
```

Install Mastodon API wrapper:

```
pip3 install Mastodon.py
```

Edit  config.json with the correct info for your bot

Now simply run the following to toot the current status of Redacted:

```
python3 ./RedactedStatus.py SourceUsername@instance.social
```

# Run it regularly

You can use cron to run the bot regularly.

Run the command:

```
crontab -e
```

And at the end of the file add the line:

```
0,30 * * * * cd /path/to/RedactedMastodonStatus/ && python3 RedactedStatus.py SourceUsername@instance.social
```

(this will execute every 30 minutes)
