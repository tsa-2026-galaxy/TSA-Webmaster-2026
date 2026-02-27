import sqlite3
import json
import bcrypt

'''
TODO: integrate bcrypt or some other password thingamajig
'''
def createSampleData():
    con = sqlite3.connect("tsa2026.db")

    cur = con.cursor()

    cur.execute("CREATE TABLE events(id, title, password, description, color, location, start)")
    cur.execute("CREATE TABLE resources(id, title, password, description, color, location, type)")

    events = (
        (0, "Art display", bcrypt.hashpw(bytes("apricot", encoding='utf8'), bcrypt.gensalt(14)), "see awesome fricken art", "blue", "level 2", "August 5th"),
        (1, "Film competition", bcrypt.hashpw(bytes("anvil", encoding='utf8'), bcrypt.gensalt(14)), "show off your cool indie films", "red", "level 3", "August 6th"),
        (2, "Gnosh's pizza opening", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place is opening", "yellow", "level 4", "August 7th")
    )
    resources = [
        (0, "Universal Library", bcrypt.hashpw(bytes("rat", encoding='utf8'), bcrypt.gensalt(14)), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur mauris nunc, mollis in risus vitae, vestibulum pulvinar libero. Quisque id metus varius, rhoncus ligula vel, aliquet dolor. Ut convallis vel ipsum at ornare. Nam tristique eleifend neque eu suscipit. Proin tincidunt purus sit amet massa faucibus facilisis. Quisque sit amet sem velit. Aliquam facilisis quam felis, sit amet porta lacus placerat id. Suspendisse blandit, massa id bibendum fringilla, diam leo aliquet enim, id sodales enim nulla id eros. Suspendisse tempor feugiat mi sed hendrerit. Nunc vehicula ex sit amet felis blandit vulputate. ", "green", "level 7", "library"),
        (1, "Universal Library 2", bcrypt.hashpw(bytes("egg", encoding='utf8'), bcrypt.gensalt(14)), "not enough history though, this has more", "green", "level 23", "library"),
        (2, "Gnosh's pizza", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place that is opened probably", "yellow", "level 4", "food"),
        (3, "Sample 2", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place that is opened probably", "red", "level 4", "food"),
        (5, "Sample 3", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place that is opened probably", "blue", "level 4", "food"),
        (4, "Sample 4", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place that is opened probably", "purple", "level 4", "food"),
        (6, "Sample 5", bcrypt.hashpw(bytes("pizzatastic", encoding='utf8'), bcrypt.gensalt(14)), "awesome evil pizza place that is opened probably", "orange", "level 4", "food")
    ]
    cur.executemany("INSERT INTO events VALUES(?, ?, ?, ?, ?, ?, ?)", events)
    cur.executemany("INSERT INTO resources VALUES(?, ?, ?, ?, ?, ?, ?)", resources)
    con.commit()
    con.close()

    con2 = sqlite3.connect("tsa2026_pending.db")

    cur2 = con2.cursor()
    cur2.execute("CREATE TABLE events(id, title, password, description, color, location, start)")
    cur2.execute("CREATE TABLE resources(id, title, password, description, color, location, type)")
    con2.commit()
    con2.close()

def testBcrypt():
    con = sqlite3.connect("tsa2026.db")
    cur = con.cursor()
    cur.execute("SELECT id, password FROM events")

    passw ="apricot"

    print(bcrypt.checkpw(bytes(passw, encoding='utf8'), cur.fetchone()[1]))
    con.close()

if __name__ == "__main__":
    createSampleData()
    # testBcrypt()