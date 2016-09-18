import sqlite3


def fetchQuestion():
    conn = sqlite3.connect('dataBase.db')
    result = []
    c = conn.cursor()
    c.execute('SELECT * FROM questions')
    for row in c:
        result.append(row)
    return result
