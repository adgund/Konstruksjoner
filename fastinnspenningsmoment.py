import numpy as np


    
def fastinnspenning ( nelem , nlast , last , elementlengder ):
    fim = np . zeros (( nelem , 2) ) # Oppretter tom liste for fastinnspenningsmomenter
    for i in range(nlast): #går gjennom alle lastene
        elemnr = int(last[i][0]) #henter ut elementnummer fra last
        lengde = elementlengder[elemnr - 1] # finner elementlengden til elementnr
        if last [i][1] == 1: # Jevnt eller lineært fordelt last
            q1 = last[i][2] #last lokal ende 1
            q2 = last[i][3] #last lokal ende 2
            #finner fastinnspenningsmomentet til lokal ende 1 og lokal ende 2
            #Bruker formler fra tabell 8.3 for fastinnspenningsmomenter fra kompendiet
            #Her brukes formler for to motsatt rettede trekanter
            fim[elemnr-1][0] += ((-1 / 20) * q1 * lengde**2) + ((-1 / 30) * q2 * lengde**2) 
            fim[elemnr-1][1] += ((1 / 30) * q1 * lengde**2) + ((1 / 20) * q2 * lengde**2)

        elif last [i][1] == 2: # Punktlast
            alpha = last[i][4] #henter verdien alfa
            a = alpha * lengde # avstand fra lokal ende 1 til punktlast
            b = lengde - a # avstand fra lokal ende 2 til punktlast
            P = last [i][2] #verdi for punklast
            if last [i][5] == 0: #hvis last står vinkelrett på  
                #finner fastinnspenningsmomentet til lokal ende 1 og lokal ende 2
                #Bruker formler fra tabell 8.3 for fastinnspenningsmomenter fra kompendiet
                #Her brukes formler for punklast
                fim [elemnr - 1][0] += (- P * a * b **2) / lengde **2 
                fim [elemnr - 1][1] += ( P *( a **2) * b) / lengde **2

            else : #hvis punklasten ikke står vinkelrett på
                P_x = P*np.cos(last[i][5]*np.pi /180) #henter ut x-komponenten til lasten
                #finner fastinnspenningsmomentet til lokal ende 1 og lokal ende 2
                #Bruker formler fra tabell 8.3 for fastinnspenningsmomenter fra kompendiet
                #Her brukes formler for punklast
                fim [elemnr - 1][0] += (- P_x * a * b**2) / lengde **2
                fim [elemnr - 1][1] += ( P_x * ( a **2) * b) / lengde **2
    return fim
    
