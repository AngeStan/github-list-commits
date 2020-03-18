from features.html_parser import *
from features.api_processor import *
from features.output import *

author = "freeCodeCamp"
repo = "freeCodeCamp"
main_url = f"https://github.com/{author}/{repo}"

print(f'''Welcome to the Git List Retriever Tool\n\
This program lets you retrieve a number (of your choice) \
of commits from a selected repo.\nThe default repository is "{author}/{repo}" in branch "master"\n''')

text_commits_count, commits_count = parse_count_commits(
    main_url)  # call function in html_parser.py
print(
    f'Please, insert a number of repositories you want to retrieve (max: {text_commits_count})')

while True:
    while True:
        try:
            number = int(input("> "))
        except ValueError as error:
            print('You have NOT inserted an integer!')
            continue
        if number <= 0:
            print("Please choose at least 1 commit to get.")
            continue
        elif number > commits_count:
            print(
                f"'{number}' is too much! Total of available commits to retrieve is '{text_commits_count}'")
            continue
        break

    table = process_api(f'{author}/{repo}', number)
    export_csv(table)
    export_db(table)
    print("\nThank you for using this tool. If you want to run it again, please enter another number.")
    number = 0  # otherwise the cycle won't work again
