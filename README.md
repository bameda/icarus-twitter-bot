# icarus-twitter-bot

Bot to publish alerts from http://icarus.live/ in Twitter ([@icarusalerts](https://twitter.com/icarusalerts)).


## Setup

```
mkvirtualenv -p /usr/bin/python3 icarus-twitter-bot
workon icarus-twitter-bot
pip install -r requirements.txt
```

## Usage

```bash
$ ./icarus-twitter-bot --help

```

You can configure the bot with:

- command options.
- environment variables.
- using ```settings/local.py``` (example at ```settings/local.py.example```).
