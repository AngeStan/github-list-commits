import csv, sqlite3, os, datetime


def export_csv(table):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')  # string "now" is a formatted current time var
    file_name = f"commits {now}.csv"
    csv_file = open(file_name, 'w', newline='')
    csv_write = csv.DictWriter(csv_file, ["SHA", "Message", "URL"])  # define the header of the CSV
    csv_write.writeheader()
    for i in range(len(table)):
        csv_write.writerow({"SHA": table[i][0], "Message": table[i][1], "URL": table[i][2]})
    csv_file.close()
    print(f'CSV file saved: "{os.path.join(os.getcwd(), file_name)}"')


def export_db(table):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')  # string "now" is a formatted current time var
    connection = sqlite3.connect("commits.db")  # establish connection with the database
    cursor = connection.cursor()  # a cursor object must be applied

    # create new table named as up-to-date date & time
    sql_command = f'''
    CREATE TABLE "{now}" (
    SHA VARCHAR(40), 
    Message VARCHAR(1000), 
    URL CHAR(100));'''
    cursor.execute(sql_command)

    for i in range(len(table)):
        sql_command = f'''INSERT INTO "{now}" (SHA, Message, URL)
        VALUES ("{table[i][0]}", "{table[i][1]}", "{table[i][2]}");'''
        cursor.execute(sql_command)

    connection.commit()  # save the changes in the database
    connection.close()
    print('Table "{}" saved in database "{}":\nyou can open/refresh it with a lightweight database manager.' \
          .format(now, os.path.join(os.getcwd(), "commits.db")))
