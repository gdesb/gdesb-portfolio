import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = """insert into mbta_buses 
            (id, latitude, longitude, label, updated_at, occupancy_status,
            direction_id, current_stop_sequence) 
            values (%s,%s,%s,%s,%s,%s,%s,%s)"""
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], 
               mbtaDict['label'], mbtaDict['updated_at'], mbtaDict['occupancy_status'], 
               mbtaDict['direction_id'], mbtaDict['current_stop_sequence'])
        mycursor.execute(sql, val)

    mydb.commit()