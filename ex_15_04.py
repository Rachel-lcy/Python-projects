import sqlite3

#connect to (or create) the SQLite database file
conn = sqlite3.connect('counts.sqlite')
cur = conn.cursor()

# Drop the table if it already exists (to start fresh)
cur.execute('DROP TABLE IF EXISTS Counts')

# create a new table for storing organization counts
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#Ask for the file name; default to 'mbox.txt' if none provided

fname = input('Enter file name: ')

if len(fname) < 1:
  fname = 'mbox.txt'
fh = open(fname)

# Loop through each line in the file
for line in fh:
  if not line.startswith('From: '):
    continue
  pieces = line.split()
  email = pieces[1]
  org = email.split('@')[1]

  #check if this organization already exists in the table
  cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
  row = cur.fetchone()
  if row is None:
    # Insert new organization with count = 1
    cur.execute('INSERT INTO Counts (org, count)  VALUES (?, 1)', (org,))
  else:
    # update the count for existing organization
    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
  conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('\nTop organizations:')
for row in cur.execute(sqlstr):
  print(row[0], row[1])

cur.close()
