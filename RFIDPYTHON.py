import sqlite3
import datetime
import serial
con = sqlite3.connect("veritabanırfıd123.db")
cursor = con.cursor()
def Tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Denemee(Name TEXT,Zaman timestamp)")

def InsertValue(bil, simdi ):
    cursor.execute("INSERT INTO Denemee VALUES('{}','{}')".format(bil, simdi))

Tabloolustur()
arduino = serial.Serial("com5",9600)
i = 0
while i<10:
    x = arduino.readline()
    bil = x.decode()
    simdi = datetime.datetime.now()
    InsertValue(bil, simdi)
    con.commit()
    i += 1
con.close()
