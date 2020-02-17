import csv, sqlite3, os

'''table = [['bb06330b639c4a212d9472091ee2cbc16fe9e7ae', 'docs: update link to coc',
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/bb06330b639c4a212d9472091ee2cbc16fe9e7ae'],
         ['3fff454872a3fdfb829510c3a3f77d4db664ccfa',
          "fix(client): localise calendar to user's current timezone (#38217)* fix: localise Heatmap to user's timezoneRather than using ISO formatted date strings, this uses Date objectsfor simplicity and to ensure that the heatmap is correct for thetimezone it is viewed in. It should also match the timeline which isalso localised to the viewing computer's timezone.* test: update snapshot",
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/3fff454872a3fdfb829510c3a3f77d4db664ccfa'],
         ['cc79999a31b46e68a4dca5d536fc2fb4fe3d5199',
          "fix: force timezone to be UTC for tests (#38215)react-calendar-heatmap's output depends on the timezone, which meansthat snapshots can fail if the timezone changes.  This sets the timezoneas UTC during client tests to avoid that problem.",
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/cc79999a31b46e68a4dca5d536fc2fb4fe3d5199']]'''


def export_csv(table):
    csv_file = open('commits.csv', 'w', newline='')
    csv_write = csv.DictWriter(csv_file, ["SHA", "Message", "URL"])
    csv_write.writeheader()
    for i in range(len(table)):
        csv_write.writerow({"SHA": table[i][0], "Message": table[i][1], "URL": table[i][2]})
    csv_file.close()


def export_db(table):
    # if the database exists already, it will make sure to clean the table, before recreating it
    database_exists = False
    if os.path.exists("commits.db"):
        database_exists = True

    connection = sqlite3.connect("commits.db")
    cursor = connection.cursor()

    if database_exists:
        cursor.execute("""DROP TABLE commits;""")

    sql_command = """
    CREATE TABLE commits ( 
    commit_num INTEGER PRIMARY KEY, 
    Sha VARCHAR(40), 
    Message VARCHAR(1000), 
    Url CHAR(100));"""
    cursor.execute(sql_command)

    for i in range(len(table)):
        sql_command = f'''INSERT INTO commits (commit_num, Sha, Message, Url)
        VALUES (NULL, "{table[i][0]}", "{table[i][1]}", "{table[i][2]}");'''
        cursor.execute(sql_command)

    connection.commit()  # save the changes in the database
    connection.close()
    print(f'Database saved in "{os.getcwd()}"\nYou can open it as a lightweight database file.')