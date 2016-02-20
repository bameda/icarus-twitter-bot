import sys

try:
    from . import local
except ImportError:
    local = {}
    print('No "settings/local.py" file found.', file=sys.stderr)


ACCESS_TOKEN = getattr(local, 'ACCESS_TOKEN', 'undefined')
ACCESS_SECRET = getattr(local, 'ACCESS_SECRET', 'undefined')
CONSUMER_KEY = getattr(local, 'CONSUMER_KEY', 'undefined')
CONSUMER_SECRET = getattr(local, 'CONSUMER_SECRET', 'undefined')
