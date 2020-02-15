import urllib.request, urllib.error, json
'''
with open('settings.json', 'r') as settings_file:
    json_file = json.loads(settings_file)
repo = json_file['repo']'''
# debug
repo = 'freeCodeCamp/freeCodeCamp'
url_api = 'https://api.github.com/repos/' + repo + '/commits?branch=master'

try:
    json_received = urllib.request.urlopen(url_api)
except urllib.error.HTTPError as error:
    # Return code error (e.g. 404, 501, ...)
    print('HTTPError: ', error.code)
except urllib.error.URLError as error:
    # Not an HTTP-specific error (e.g. connection refused)
    print('URLError: ', error.reason)
finally:
    print('Connected Successfully!')
    # processing...
    thirty_commits = json.loads(json_received.read().decode())
    table = []
    for commit in thirty_commits:
        sha = commit['sha']
        message = commit['commit']['message']
        url = commit['html_url']
        table.append({'sha': sha, 'message': message, 'url': url})
print(table)