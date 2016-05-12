import random
import csv

for i in range(8):
    d_comparees = []
    id_stat = []
    for s in stations_coord:
        id_stat += [s] 
    
    continuer= True
    count = 0
    
    while continuer and count <= 100:
        i = random.randint(0,N-1)
        j = random.randint(0,N-1)
        s1, s2 = id_stat[i], id_stat[j]
        d1 = distance_h(s1,s2)
        d2 = distance_i(s1, s2)
        d_comparees += [[d1,d2]]
        count += 1

    
    csvfile = open('comparaison_dist.csv', 'a')
    dwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for l in d_comparees:
        dwriter.writerow(l)
    csvfile.close()
