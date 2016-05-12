import random

d_comparees = []
id_stat = []
for s in stations_coord:
    id_stat += [s] 

##
continuer= True
count = 0

while continuer and count <= 100:
    i = random.randint(0,N)
    j = random.randint(0,N)
    s1, s2 = id_stat[i], id_stat[j]
    d1 = distance_h(s1,s2)
    d2 = distance_i(s1, s2)
    d_comparees += [[d1,d2]]
    count += 1
##
d2 = []
k = len(d_comparees)
k2 = k//2
for i in range(k2):
    l = [d_comparees[2*i],d_comparees[2*i+1]]
    d2 += [l]

##

import csv
cvsfile = open('comparaison_dist.csv', 'w')
spamwriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
for 
spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])