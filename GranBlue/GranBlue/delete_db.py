import sqlite3

conn = sqlite3.connect('/home/ubuntu/project/GranBlue/boss')
#print("Linked to SQLite database !")

cursor = conn.cursor()
cursor.execute('delete from GranBlueModel_granblue where id in (select id from GranBlueModel_granblue order by id limit 0,30000)')
conn.commit()
conn.close()

