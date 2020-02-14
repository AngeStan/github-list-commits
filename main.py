print("Welcome to the Git List Retriever Tool")
help_message = '''Please, select one of the following commands
GO -> starts the program
SETTINGS -> change some option
QUIT -> quit the program'''
print(help_message)

while True:
    command = input("> ").lower()
    if command == 'help':
        print(help_message)
    elif command == 'go':
        print('starting....')
    elif command == 'settings':
        print('going to settings')
    elif command == 'quit':
        break
    else:
        print(f"Command not found!\n{help_message}")