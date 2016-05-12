stations_coord = dict()
stations_bornes = dict()
stations_velos = dict()
N = 0

##
def maj_coord():
    stations = open('Paris.csv', 'r')
    stationreader = csv.reader(stations, delimiter = ',')
    for row in stationreader:
        l=[]
        for item in row:
            l = l + [item]
        stations_coord[str(l[0])] = [l[3],l[4]]
    stations.close()

##
def maj_bornes():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=08d9a2281bfac62f9b1ec531426ee7de8a7abfc0'
    r = requests.get(url)
    s = r.json()
    for station in s:
        stations_bornes[str(station['number'])] = station['bike_stands']
    
##
def maj_velos():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=08d9a2281bfac62f9b1ec531426ee7de8a7abfc0'
    r = requests.get(url)
    s = r.json()
    for station in s:
        stations_velos[str(station['number'])] = station['available_bikes']

##
def maj_N():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=08d9a2281bfac62f9b1ec531426ee7de8a7abfc0'
    r = requests.get(url)
    s = r.json()
    global N
    N = len(s)













