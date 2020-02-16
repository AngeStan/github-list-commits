import urllib.request, urllib.error, json


def process_api(repo, number_commits):
    url_api = 'https://api.github.com/repos/' + repo + '/commits?branch=master'
    remaining_commits = number_commits
    last_sha = starter = 0
    table = []

    def connect(url):
        try:
            json_received = urllib.request.urlopen(url)
        except urllib.error.HTTPError as error:
            # Return code error (e.g. 404, 501, ...)
            print('HTTPError: ', error.code)
        except urllib.error.URLError as error:
            # Not an HTTP-specific error (e.g. connection refused)
            print('URLError: ', error.reason)
        finally:
            print('Connected Successfully!')
            # processing...
            # json_received = urllib.request.urlopen(url)
            json_data = json.loads(json_received.read().decode())
            return json_data

    while remaining_commits > 0:
        if last_sha != 0:
            url_api = url_api.split('&')[0] + '&sha=' + str(last_sha)
            starter = 1
        commits = connect(url_api)

        for i in range(starter, 30):
            last_sha = commits[i]['sha']
            table.append([last_sha, commits[i]['commit']['message'], commits[i]['html_url']])
            remaining_commits -= 1
            print(remaining_commits)
            if remaining_commits == 0:
                break

    for row in range(len(table)):  # remove new lines
        table[row][1] = table[row][1].replace("\n", "")
        table[row][1] = table[row][1].replace("\r", "")

    # print(len(table))
    return table
    # print(table)
