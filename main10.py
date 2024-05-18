import sqlite3

connection = sqlite3.connect(database='ItStepDb.db', timeout=5.0)
pointer = connection.cursor()

# pointer.execute("INSERT INTO crypto (name, rate) VALUES ('Bitcoin', 67291.139)")

# value = ('Etherum', 3138.35)
# pointer.execute("INSERT INTO crypto (name, rate) VALUES (?, ?)", value)

# values = [('Tether', 1.05), ('BNB', 353.12), ('Solana', 174.52)]
# pointer.executemany("INSERT INTO crypto (name, rate) VALUES (?, ?)", values)

rate, = pointer.execute("SELECT rate FROM crypto WHERE name='BNB'").fetchone()
print(rate, type(rate))

# connection.commit()
connection.close()
