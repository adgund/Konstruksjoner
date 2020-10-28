import numpy as np

def midtmoment(nelem, elem, nlast, last, elementlengde, endemoment):
    midtmoment = np.zeros((nelem , 1)) #opretter et tomt array for aa lagre midtmomentene
    for i in range(nelem): #går gjennom alle elementene
        elnr = elem[i][5] #henter ut elementnr fra elementene
        if elem[i][4] == 1: #hvis element har ytre last
            for j in range(nlast): #går gjennom lastene
                elemnr = int(last[j][0]) #henter ut elementnr fra lastene
                lengde = elementlengde[elemnr - 1] #finner lengden til element
                if last[j][1] == 2:#punktlast, beregnes rett under punktlasten
                    alpha = last[j][4] #finner alfa
                    a = alpha * lengde #finner avstand fra lokal ende 1
                    b = lengde - a #finner avstand fra lokal ende 2
                    M1 = endemoment[elemnr - 1][0] #henter endemoment lokal ende 1
                    M2 = endemoment[elemnr - 1][1] #henter endemoment lokal ende 2
                    if last[j][5] != 0: #hvis ikke vinkelrett
                        P = last[j][2] * np.cos(last[j][5] * np.pi / 180) #dekomponerer og finner komponent vinkelrett på
                        M_punkt = (P * a * b) / lengde #Finner moment under last
                        #Finner bidaget til moment under punklast fra endemoment
                        M1 = endemoment[elemnr - 1][0] #moment fra ende 1
                        M2 = endemoment[elemnr - 1][1] #moment fra ende 2
                        if abs (M2) >= abs (M1) : #Hvis M2 >= M1
                            M_ende = M1 - (M1 + M2) * alpha #M1 - (M1 + M2) * alfa
                            midtmoment[elemnr - 1] = M_punkt + M_ende #legget til begge bidragene
                        else : 
                            M_ende = -M2 + ( M1 + M2) * (1 - alpha) #-M2 + (M1 + M2) * (1 - alfa)
                            midtmoment[elemnr - 1] = M_punkt + M_ende #legger til begge bidragen
                            midtmoment[elemnr - 1] = M_punkt + M_ende #legger til begge bidragene
                    else: #hvis vinkelrett på element
                        P = last[j][2] #størrelse på last
                        M_punkt = (P * a * b) / lengde #moment under last
                        M1 = endemoment[elemnr - 1][0] #moment fra ende 1
                        M2 = endemoment[elemnr - 1][1] #moment fra ende 2
                        if abs (M2) >= abs (M1) : #Hvis M2 >= M1
                            M_ende = M1 - (M1 + M2) * alpha #M1 - (M1 + M2) * alfa
                            midtmoment[elemnr - 1] = M_punkt + M_ende #legget til begge bidragene
                        else : 
                            M_ende = -M2 + ( M1 + M2) * (1 - alpha) #-M2 + (M1 + M2) * (1 - alfa)
                            midtmoment[elemnr - 1] = M_punkt + M_ende #legger til begge bidragene
                        
                elif last[j][1] == 1: #jevnt eller lineært fordelt last
                    q1 = last[j][2] #verdi last ende 1
                    q2 = last[j][3] #verdi last ende 2
                    M1 = endemoment[elemnr - 1][0] #moment fra ende 1
                    M2 = endemoment[elemnr - 1][1] #moment fra ende 2
                    M_ende = (M1 - M2) / 2 #(M1 - M2) / 2 #midtmoment fra endemoment
                    #momentbidrag fra jevnt/lineært fordelt last
                    #den jevnt fordelte lasten deles opp i to trekantbidrag
                    M_jevnt = (lengde**2 / 16) * (q1 + q2) 
                    midtmoment[elemnr - 1] = M_jevnt + M_ende #legger til begge bidragene
        else: #hvis ikke ytre last
            M1 = endemoment[elnr - 1][0] #moment ende 1
            M2 = endemoment[elnr - 1][1] #moment ende 2
            M_ende = (M1 - M2) / 2 #bidraget fra endemoment
            midtmoment[i] += M_ende #legger til bidraget
    return midtmoment
