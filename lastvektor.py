import numpy as np

def lastvektor ( npunkt , nelem , elem , fim , nlast , last ):
   
    lastvektor = np.zeros ((npunkt , 1)) #oppretter tom liste for lastvektor
    
    for i in range (nelem): #går gjennom alle elementer
        knutepunkt1 = elem[i][0] #henter ut lokalt knutepunkt 1 for element i
        knutepunkt2 = elem[i][1] #henter ut lokalt knutepunkt 2 for element i
        lastvektor[knutepunkt1 - 1] -= fim [i][0] #legger til bidraget fra fim i lastvektoren (med motsatt fortegn) 
        lastvektor[knutepunkt2 - 1] -= fim [i][1]
        
    for j in range(nlast): #går gjennom lastene
        if last[j][1] == 3: #hvis moment
            knutepunkt = int(last[j][7]) #henter knutepunktet momentet virker i
            moment = last[j][6] #henter verdien til momentet
            lastvektor[knutepunkt-1] += moment #legger til bidraget fra moment i lastvektoren
    return lastvektor
