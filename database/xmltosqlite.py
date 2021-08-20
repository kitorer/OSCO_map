import sqlite3
import xml.etree.ElementTree as ET

db = sqlite3.connect('Calls.db')
cursor = db.cursor()

tree = ET.parse('activecalls.xml')
root = tree.getroot()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS calls(
    incidents INTEGER,
    time INTEGER,
    description TEXT,
    location TEXT,
    sector INTEGER,
    zone INTEGER,
    District TEXT)
    ''')
#loops through call
for child in root:

    callbracket =child.attrib
    callbracket = str(callbracket)[14:-2]

    #loops through data inside of <call>
    for calls in child:

        callAttributes = calls.tag
        callinfo = calls.text

        if(callAttributes =='ENTRYTIME'):
            #print("ENTRYTIME")
            global timeAttrib
            timeAttrib = calls.text
        elif(callAttributes =='DESC'):
            #print("DESC")
            global descAttrib
            descAttrib = calls.text
        elif(callAttributes =='LOCATION'):
            #print("LOCATION")
            global locationAttrib
            locationAttrib = calls.text
        elif(callAttributes =='SECTOR'):
            #print("SECTOR")
            global sectorAttrib
            sectorAttrib = calls.text
        elif(callAttributes =='ZONE'):
            #print("ZONE")
            global zoneAttrib
            zoneAttrib = calls.text
        elif(callAttributes =='RD'):
            #print("RD")
            global districtAttrib
            districtAttrib = calls.text

    cursor.execute('''INSERT INTO calls(incidents, time, description, location, sector, zone, District) VALUES(?,?,?,?,?,?,?)''',
    (callbracket, timeAttrib, descAttrib, locationAttrib, sectorAttrib, zoneAttrib, districtAttrib))

db.commit()
