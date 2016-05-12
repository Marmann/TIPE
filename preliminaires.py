import requests
import os

os.chdir('/home/hichem/TIPE 2')

stations_coord = dict()
stations_bornes = dict()
stations_velos = dict()
N = 1129

##
def recuperer_etat_stations():
    with open('bornes','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        stations_bornes = mon_depickler.load()
    
    with open('coord','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        stations_coord = mon_depickler.load()
    
    with open('velos','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        stations_velos = mon_depickler.load()


##
def maj_coord():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Paris&apiKey=08d9a2281bfac62f9b1ec531426ee7de8a7abfc0'
    r = requests.get(url)
    s = r.json()
    for station in s:
        stations_coord[str(station['number'])] = [station['position']['lat'],station['position']['lng']]

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

##
def maj_tout():
    maj_bornes()
    maj_coord()
    maj_N()
    maj_velos()

##

import pickle

def enregister_etat_stations():
    with open('bornes','wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(stations_bornes)
    
    with open('coord','wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(stations_coord)
    

    with open('velos','wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(stations_velos)

    
    
    

##

maj_tout()
enregister_etat_stations()






