import sqlite3
import xml.etree.ElementTree as ET

db = sqlite3.connect('Calls.db')
cursor = db.cursor()

tree = ET.parse('activecalls.xml')
root = tree.getroot()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS calls(call number INTEGER PRIMARY KEY, time INTEGER, description TEXT, location TEXT, sector INTEGER, zone INTEGER
    , District TEXT)
    ''')

for child in root:

    #cursor.execute(''' INSERT INTO CALLS(call number INTEGER PRIMARY KEY, time INTEGER, description TEXT, location TEXT)(?,?,?,?)''',())
    print(child.tag, child.attrib)

    for calls in child:
        print(calls.tag, calls.text)


db.commit()
