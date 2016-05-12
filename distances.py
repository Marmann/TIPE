import requests
import numpy as np
import os

os.chdir('/home/hichem/TIPE 2')

cleAPI = 'AIzaSyDX5Je-aHHsW3iI_o8D0VlCLFM2kC8H1rE' #API Google Maps

champ_distances_h = dict() #h pour hors-ligne, distances obtenues uniquement à partir des coordonnées GPS avec un calcul simple prenant en compte la courbure de la Terre

#champ_distances_i = dict() #i pour internet, champ des distances obtenu à partir des données en ligne de Google Maps
#champ_distances_i_plus = dict()

def distance_i(s1, s2):
    c1 = stations_coord[s1]
    c2 = stations_coord[s2]
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + str(c1[0]) + ',' + str(c1[1]) +'&destinations=' +  str(c2[0]) + ',' + str(c2[1]) + '&key=' + cleAPI
    print(url)
    r = requests.get(url)
    s = r.json()
    return s['rows'][0]['elements'][0]['distance']['value']

def distance_h(s1,s2):
    c1 = stations_coord[s1]
    c2 = stations_coord[s2]
    lat1 = (c1[0]/180) * np.pi
    lat2 = (c2[0]/180) * np.pi
    lng1 = (c1[1]/180) * np.pi
    lng2 = (c2[1]/180) * np.pi
    a= np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(lng2-lng1)
    if abs(a)<= 1:
        return 1.5*60*(180/np.pi)*np.arccos(a)*1852
    if s1 ==s2:
        return 0

def maj_distances_h():
    for s1 in stations_coord:
        champ_distances_h[s1] = dict()
        for s2 in stations_coord:
            champ_distances_h[s1][s2] = distance_h(s1,s2)

def enregistrer_champ_distances_h():
    with open('champ_dist_h','wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(champ_distances_h)

def recuperer_champ_distances_h():
    with open('champ_dist_h','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        champ_distances_h = mon_depickler.load()

# 
# def maj_distances_i_prim():
#     for s1 in stations_coord: #on remplit la matrice champ_distances
#         champ_distances_i[s1] = dict()
#         for s2 in stations_coord:
#             champ_distances_i[s1][s2] = distance(s1, s2)
#             
# def distances_i_ameliore_aux():
#     id_stat = []
#     
#     for s in stations_coord:
#         id_stat += [s] 
#     
#     n = len(id_stat)
#     champ_distances_i_am = np.zeros((n,n))
#     
#     idep = 0
#     jdep = 0
#     
#     while (idep,jdep) <= (n-1,n-1):
#         idep,jdep = remplir_suite(idep, jdep, id_stat, champ_distances_i_am,n)
#     
#     return champ_distances_i_am, id_stat, n
#     
# def distances_i_ameliore():
#     c, l, n = distances_i_ameliore_aux()
#     
#     for i in range(n):
#         s1 = id_stat[i]
#         champ_distances_i_plus[s1] = dict{}
#         for j in range(n):
#             s2 = id_stat[j]
#             champ_distances_i_plus[s1][s2] = c[i,j]
#                     
#                 
# def remplir_suite(idep, jdep, id_stat, champ_distances_i_am,n):
#     s1 = id_stat[idep]
#     s2 = id_stat[jdep]
#     
#     c1 = stations_coord[s1]
#     c2 = stations_coord[s2]
#     
#     cle = '&key=AIzaSyB4cDDHXTGwNcojOQwdGxh7QofIjmCBYV8'
#     urlor ='https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + str(c1[0])[0:7] + ',' + str(c1[1])[0:6]
#     urldes =  '&destinations=' + str(c2[0])[0:7] + ',' + str(c2[1])[0:6]
#     url = urlor + urldes + cle
#     
#     jarr = idep
#     iarr = jdep
#     
#     i = idep+ (jdep + 1)//n
#     j = (jdep+1) % n
# 
#     while len(url) < 1800 and i < n:
#         s1 = id_stat[i]
#         s2 = id_stat[j]
#         c1 = stations_coord[s1]
#         c2 = stations_coord[s2]
#         urlor += '|' + str(c1[0])[0:7] + ',' + str(c1[1])[0:6]
#         urldes += '|' + str(c2[0])[0:7] + ',' + str(c2[1])[0:6]
#         url = urlor + urldes + cle
#         i = i+ (j + 1)//n
#         j = (j+1) % n
#         iarr = i
#         jarr = j
#     r = requests.get(url)
#     s = r.json()
#     i = idep
#     j = jdep
#     while (i,j) < (iarr, jarr):
#         print(i,j)
#         print(idep, jdep)
#         
#         champ_distances_i_am[i][j] = s['rows'][j-jdep]['elements'][i-idep]['distance']['value']
#         i = i + (j + 1)//n
#         j = (j + 1) % n
#     return iarr, jarr
    
    

            