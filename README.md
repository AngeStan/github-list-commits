# github-list-commits
(Python) Tool to retreive a list of commits of a chosen Repo.
The current default repo is http://github.com/freeCodeCamp/freeCodeCamp for branch master.

# Methodology
- Parses the HTML page of the master commits to know how many of them are merged in the branch.
- Asks the user to decice how many of them to retrieve.
- Query the GitHub Rest API to get the chosen number of repo, toghther with SHA, Message and URL.
- The results are displayed in an exported CSV file and a SQL DataBase.

# Code
- Invalid Input Handling
- Re-Querying the API after every 30 repos, due to the response type
- Dynamic CSV filename and table name in SQL Db based on current date and time

# Requirements
- beautifulsoup4 4.8.2
- certifi        2019.11.28
- chardet        3.0.4
- idna           2.8
- pip            19.0.3
- requests       2.22.0
- setuptools     40.8.0
- soupsieve      1.9.5
- urllib3        1.25.8
