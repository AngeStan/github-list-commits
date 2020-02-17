import urllib.request, urllib.error, json


def connect(url):  # function to test and get the Pythoned JSON data
    try:
        json_received = urllib.request.urlopen(url)
    except urllib.error.HTTPError as error:
        # Return code error (e.g. 404, 501, ...)
        print('HTTPError: ', error.code)
    except urllib.error.URLError as error:
        # Not an HTTP-specific error (e.g. connection refused)
        print('URLError: ', error.reason)
    finally:
        json_data = json.loads(json_received.read().decode())
        return json_data


def process_api(author_repo, number_commits):
    print('Progress', end='')
    url_api = 'https://api.github.com/repos/' + author_repo + '/commits?branch=master'
    last_sha = starter = 0
    table = []

    while number_commits > 0:
        print('...', end='')
        if last_sha != 0:  # if line 33 already executed
            url_api = url_api.split('&')[0] + '&sha=' + str(last_sha)  # add/change the parameter SHA
            starter = 1  # line 32 will skip the first commit (duplicate)
        commits = connect(url_api)

        # code to populate the list "table" with SHA, Message, URL in each row of it
        for i in range(starter, 30):  # max 30 times due to the api of GitHub
            last_sha = commits[i]['sha']  # SHA kept in memory to now if this block runs more then one times
            table.append([last_sha, commits[i]['commit']['message'], commits[i]['html_url']])
            number_commits -= 1  # remaining commits decreases
    print('')
    # Adjustments of the texts in "Message"
    for row in range(len(table)):
        table[row][1] = table[row][1].replace("\n", "")  # removes windows:[newline] chars
        table[row][1] = table[row][1].replace("\r", "")  # removes mac:[newline] chars
        table[row][1] = table[row][1].replace('"', "'")  # swipes " with ' to avoid SQL conflicts

    return table
