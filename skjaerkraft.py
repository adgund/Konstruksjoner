import numpy as np

def skjaerkrefter( nelem ,elem, endemoment, nlast, last, elementlengde ):
    skjaer = np.zeros((nelem, 2)) #tom liste for skjærkrefter
    
    for i in range(nelem):
        M1 = endemoment[i][0] #henter ut endemoment ende 1
        M2 = endemoment[i][1] #endemoment ende 2
        Q1 = -(M1 + M2) / elementlengde[i] #finner skjærkraft pga endemoment
        skjaer[i][0] = Q1 #legger til i liste for skjærkrefter
        skjaer[i][1] = Q1 
        
    #legger til for punktlast og jevnt fordelt
    for i in range(nlast): #går gjennom lastene
        elemnr = int( last[i][0] ) #henter elementnr
        lengde = elementlengde[elemnr - 1] #henter lengden på elementet
        alpha = last[i][4] #henter alfa
        
        if last[i][1] == 2: #hvis punktlast
            if last[i][4] != 0: #hvis ikke normalt på
                Pq = ( last[i][2]) * (np.cos(last[i][4] * np.pi / 180)) #finner last normalt på 
                skjaer[elemnr - 1][0] += Pq * (1 - alpha) #legger til bidrag til skjær ende 1
                skjaer[elemnr - 1][1] -= Pq * alpha #legger til bidrag til skjær ende 2
            else: #normalt på 
                Pq = last[i][2]  #last verdi
                skjaer[elemnr - 1][0] += Pq * ( 1 - alpha) #legger til bidrag til skjær ende 1
                skjaer[elemnr - 1][1] -= Pq * alpha #legger til bidrag til skjær ende 2
                


        elif last[i][1] == 1: #hvis jevnt/lineært fordelt 
            q1 = last[i][2] #henter ut jevnt/lineært fordelt last ende 1
            q2 = last[i][3] #henter ut jevnt/lineørt fordelt last ende 2
            if q1 == q2: #hvis jevnt fordelt
                Q = (q1 * lengde) / 2 #skjær lik (motsatt fortegn) i begge ender
                skjaer[elemnr - 1][0] += Q #legger til bidraget fra last i ende 1
                skjaer[elemnr - 1][1] -= Q #legger til bidraget fra last i ende 2
            else: 
                #deler lineært fordelt last i to trekantbidrag
                P_q1 = (q1 * lengde) / 2 #resulterende kraft fra trekant 1 
                P_q2 = (q2 * lengde) / 2 #resulterende kraft fra trekant 2
                
                #angrepslinjen til en 'trekantlast' vil ligge 1/3 fra enden med størst last
                #trekant 1
                avstand_kpkt1_P_q1 = 1 / 3 #avstand til angrepslinje fra ende 1 
                avstand_kpkt2_P_q1 = 2 / 3 #avstand til angrepslinje fra ende 1 
                #trekant 2
                avstand_kpkt1_P_q2 = 2 / 3 #avstand til angrepslinje fra ende 1
                avstand_kpkt2_P_q2 = 1 / 3 #avstand til angrepslinje fra ende 2
                
                #legger sammen bidragene til skjærkrefter
                Q1 = P_q1 * (1 - avstand_kpkt1_P_q1) + P_q2 * (1 - avstand_kpkt1_P_q2) 
                Q2 = P_q1 * (1 - avstand_kpkt2_P_q1) + P_q2 * (1 - avstand_kpkt2_P_q2)
                skjaer[elemnr - 1][0] += Q1 #legget til bidragene 
                skjaer[elemnr - 1][1] -= Q2
    return skjaer