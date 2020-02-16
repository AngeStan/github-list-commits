import urllib.request, urllib.error, json

'''
with open('settings.json', 'r') as settings_file:
    json_file = json.loads(settings_file)
repo = json_file['repo']'''
# debug-----------
repo = 'freeCodeCamp/freeCodeCamp'
url_api = 'https://api.github.com/repos/' + repo + '/commits?branch=master'
number_commits = remaining_commits = 69

last_sha = starter = last_index_commit = 0
table = []

while remaining_commits > 0:
    if remaining_commits > 30:
        last_index_commit = 29
    else:
        last_index_commit = remaining_commits

    if last_sha != 0:
        url_api = url_api.split('&')[0] + '&sha=' + str(last_sha)
        starter = 1
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
        commits = json.loads(json_received.read().decode())

    print(last_index_commit)
    for i in range(starter, last_index_commit + 1):
        last_sha = commits[i]['sha']
        table.append([last_sha, commits[i]['commit']['message'], commits[i]['html_url']])
        remaining_commits -= 1
        print(remaining_commits)

print(table)
print(len(table))
