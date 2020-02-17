import requests, bs4
from features.api_processor import *
from features.output import *
author = "freeCodeCamp"
repo = "freeCodeCamp"
main_url = f"https://github.com/{author}/{repo}"

print(f'''Welcome to the Git List Retriever Tool\n\
This program lets you retrieve a number (of your choice) \
of commits from a selected repo.\nThe default repository is "{author}/{repo}" in branch "master"\n''')

# the following block of code is to count the total number of up-to-date commits in "master"
master_url = f"{main_url}/tree/master"  # generation of the "master" branch
html_page = requests.get(master_url)
soup = bs4.BeautifulSoup(html_page.text, features="html.parser")
box = soup.select('.commits > a:nth-child(1) > span:nth-child(2)')  # interested CSS selection
text_commits_count = box[0].getText()
text_commits_count = text_commits_count.replace(" ", "")
text_commits_count = text_commits_count.replace("\n", "")
commits_count = int(text_commits_count.replace(",", ""))

print(f'Please, insert a number of repositories you want to retrieve (max: {text_commits_count})')

while True:
    try:
        number = int(input("> "))
    except ValueError as error:
        print('You have NOT inserted a number! Please try again')
        continue
    finally:
        if number <= 0:
            print("Please choose at least 1 commit to get.")
            continue
        elif number > commits_count:
            print(f"'{number}' is too much! Total of available commits to retrieve is '{text_commits_count}'")
            continue
        break


table = process_api(f'{author}/{repo}', number)
export_csv(table)
export_db(table)