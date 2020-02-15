import urllib.request, urllib.error, json

'''
with open('settings.json', 'r') as settings_file:
    json_file = json.loads(settings_file)
repo = json_file['repo']'''
# debug-----------
repo = 'freeCodeCamp/freeCodeCamp'
url_api = 'https://api.github.com/repos/' + repo + '/commits?branch=master'
number_commits = remaining_commits = 69
if remaining_commits > 30:
    page_commits = 30
else:
    page_commits = remaining_commits
sha = starter = 0
table = []

while remaining_commits > 0:
    if remaining_commits > 30:
        page_commits = 29
    else:
        page_commits = remaining_commits

    if sha != 0:
        url_api = url_api.split('&')[0] + '&sha=' + str(sha)
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

    print(page_commits)
    for i in range(starter, page_commits + 1):
        sha = commits[i]['sha']
        message = commits[i]['commit']['message']
        url = commits[i]['html_url']
        table.append({'sha': sha, 'message': message, 'url': url})
        remaining_commits -= 1
        print(remaining_commits)

print(table)
print(len(table))
