import urllib.request, urllib.error, json


def process_api(author_repo, number_commits):
    url_api = 'https://api.github.com/repos/' + author_repo + '/commits?branch=master'
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

    while number_commits > 0:
        if last_sha != 0:
            url_api = url_api.split('&')[0] + '&sha=' + str(last_sha)
            starter = 1
        commits = connect(url_api)

        for i in range(starter, 30):
            last_sha = commits[i]['sha']
            table.append([last_sha, commits[i]['commit']['message'], commits[i]['html_url']])
            number_commits -= 1
            print(number_commits)
            if number_commits == 0:
                break

    # Texts in "Message" column adjustments
    for row in range(len(table)):
        table[row][1] = table[row][1].replace("\n", "")  # removes windows:[newline] chars
        table[row][1] = table[row][1].replace("\r", "")  # removes mac:[newline] chars
        table[row][1] = table[row][1].replace('"', "'")  # swipes " with ' to avoid SQL conflicts

    # print(len(table))
    return table
    # print(table)
