import csv

table = [['bb06330b639c4a212d9472091ee2cbc16fe9e7ae', 'docs: update link to coc',
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/bb06330b639c4a212d9472091ee2cbc16fe9e7ae'],
         ['3fff454872a3fdfb829510c3a3f77d4db664ccfa',
          "fix(client): localise calendar to user's current timezone (#38217)\n\n* fix: localise Heatmap to user's timezone\r\n\r\nRather than using ISO formatted date strings, this uses Date objects\r\nfor simplicity and to ensure that the heatmap is correct for the\r\ntimezone it is viewed in. It should also match the timeline which is\r\nalso localised to the viewing computer's timezone.\r\n\r\n* test: update snapshot",
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/3fff454872a3fdfb829510c3a3f77d4db664ccfa'],
         ['cc79999a31b46e68a4dca5d536fc2fb4fe3d5199',
          "fix: force timezone to be UTC for tests (#38215)\n\nreact-calendar-heatmap's output depends on the timezone, which means\r\nthat snapshots can fail if the timezone changes.  This sets the timezone\r\nas UTC during client tests to avoid that problem.",
          'https://github.com/freeCodeCamp/freeCodeCamp/commit/cc79999a31b46e68a4dca5d536fc2fb4fe3d5199']]


table.r
csv_file = (open('../commits.csv', 'w'))
csv_write = csv.writer(csv_file)

for i in range(len(table)):
    csv_write.writerow(table[i])

csv_file.close()
