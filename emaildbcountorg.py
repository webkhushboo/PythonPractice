import sqlite3
from pip._vendor.distlib.compat import raw_input

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''Drop table if exists Counts''')

cur.execute('''Create table counts (org TEXT , count INTEGER)''')

fname = raw_input('Enter file name :')
if(len(fname) < 1) : 
    fname = 'mbox-short.txt'
    
fh = open(fname)
for line in fh:
    if not line.startswith('From:') : continue
    pieces = line.split()
    email = pieces[1]
    emailArray = email.split("@")
    org= emailArray[1]
    cur.execute('Select count from COUNTS where org =?',(org,))
    try :
        count= cur.fetchone()[0]
        cur.execute('Update Counts set count = count +1 where org = ?' ,(org,))
    except :
         cur.execute('''Insert into counts(org,count) values(?,1)''' ,(org,))
         
    conn.commit()

sqlstr = "Select org, count from COUNTS ORDER BY Count desc Limit 10"

for row in cur.execute(sqlstr): 
    print(str(row[0]),row[1])


cur.close()