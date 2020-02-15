print("Welcome to the Git List Retriever Tool")
paths = {'GO': 'start the program', 'SETTINGS': 'change some option', 'QUIT': 'quit the program'}


def help_message():
    print('Please, select one of the following commands:')
    for key in paths:
        print(key, ' -> ', paths[key])


print('This program lets you retrieve a number (of your choice) \
of commits from a selected repo.\n')
help_message()

while True:
    command = input("> ").lower()
    if command == 'go':
        print('starting....')
    elif command == 'settings':
        print('going to settings')
    elif command == 'quit':
        break
    else:
        print(f"Command not found!")
        help_message()