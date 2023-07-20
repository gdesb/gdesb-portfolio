import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            busDict['id'] = bus['id']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['label'] = bus['attributes']['label']
            busDict['updated_at'] = bus['attributes']['updated_at']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  