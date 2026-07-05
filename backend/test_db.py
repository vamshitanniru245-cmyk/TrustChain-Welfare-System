from db import get_connection

conn = get_connection()
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM beneficiaries")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()