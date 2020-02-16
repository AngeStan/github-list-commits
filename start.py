from features.api_processor import *
repo = 'freeCodeCamp/freeCodeCamp'

print(f'''Welcome to the Git List Retriever Tool\n\
This program lets you retrieve a number (of your choice) \
of commits from a selected repo.\nThe default repository is "{repo} in branch "master"''')
print('Please, insert a number of repositories you want to retrieve')

while True:
    try:
        number = abs(int(input("> ")))
        break
    except ValueError as error:
        print('You have NOT inserted a number! Please try again')

print(process_api(repo, number))