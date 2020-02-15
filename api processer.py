import urllib.request, urllib.error, json

api = 'https://api.github.com/repos/' + repo + '/commits'
try:
    url = urllib.request.urlopen("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?branch=master")
    print('Connected')
    # process
    data = json.loads(url.read().decode())
    # this loads the pythondata value "data" back to json string
    with open("C:\\Users\\Angelo\\Desktop\\Studio\\Python\\data.json", 'w') as f:
        json.dump(data, f)

    first_commit = data[0]

    # output some object attributes
    with open("C:\\Users\\Angelo\\Desktop\\Studio\\Python\\file.txt", 'w') as file:
        file.write(str(first_commit))
    file2 = open("C:\\Users\\Angelo\\Desktop\\Studio\\Python\\file2.txt", 'a')
    for comma in first_commit:
        file2.write(f"{comma}: {first_commit[comma]}\n")
    sha = first_commit['sha']
    url = first_commit['html_url']
    camp_commit = first_commit['commit']
    message = camp_commit['message']

    print(f"{sha}\n{url}")
    file3 = open("C:\\Users\\Angelo\\Desktop\\Studio\\Python\\file3.txt", 'w')
    file3.write(str(camp_commit))
    file4 = open("C:\\Users\\Angelo\\Desktop\\Studio\\Python\\file4.txt", 'w')
    file4.write(message)
    file.close()
    file2.close()
    file3.close()
    file4.close()
    #print(data{sha})
    #print('$ ' + data['volume'])
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    # ...
    print('HTTPError: ', e.code)
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    # ...
    print('URLError: ', e.reason)
#else:
    # 200
    # ...
    #print('Connected')