#!/usr/bin/env python
import os
import sys
import json
import requests
from time import sleep
from pprint import pprint


URL = 'https://api.github.com'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
    'Authorization': 'token {0}'.format(os.getenv('GITHUB_TOKEN_GHQUERY')),
    'User-Agent': 'ghquery'
}


def find_user(user):
    url = '{0}/search/users?q={1}&type=Users'.format(URL, user)
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code in [400, 422, 500, 403, 404, 402]:
        return '{0} not found!'.format(user)
    jresp = json.loads(resp.text)
    if jresp['total_count'] > 0:
        for u in jresp['items']:
            print('Found {0} - {1}'.format(u['login'], u['url']))
    return 'Finished with {0} results for "{1}"\n'.format(jresp['total_count'], user)


def main():
    with open(sys.argv[1], 'r') as users:
        for user in users:
            print find_user(user.strip())
            sleep(3)

    return sys.exit(0)


if __name__ == '__main__':
    main()
