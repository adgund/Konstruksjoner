import numpy as np


def endeM ( nelem , elem , elementlengder , rot , fim , boyestivheter):
    endemom = np.zeros(( nelem , 2) ) #oppretter tom matrise for endemomenter
    rotasjoner = np.zeros(( nelem , 2) ) #oppretter tom liste for rotajsoner
    generell = np.array ([[4 , 2] , [2 , 4]]) #lager en basis stivhetsmatrise
    for i in range ( nelem ):
        ESM = generell * ( boyestivheter [i]/ elementlengder [i]) #elementstivhetsmatrise
        knutepkt1 = elem[i][0] #finner knutepunkt lokal ende 1
        knutepkt2 = elem[i][1] #finner knutepunkt lokal ende 2
        rotasjoner[i][0] = rot [knutepkt1 - 1] #henter ut rotasjoner i lokal ende 1
        rotasjoner[i][1] = rot [knutepkt2 - 1] #henter ut rotasjoner i lokal ende 2
        
        #Finner momentbidraget fra enderotasjonene
        #Bruker matrisemultiplikasjon for å finne momentbidrag fra rotasjoner
        #Legger til bidraget i matrisen med endemomenter
        endemom[i] = np.matmul(ESM, rotasjoner[i]) 
        #Finner momentbidrager fra fastinnspenningsmomentene
        m1 = fim[i][0] #henter ut fastinnspenningsmoment fra lokal ende 1
        m2 = fim[i][1] #henter ut fastinnspenningsmoment fra lokal ende 2

        #Legger til bidragene fra fastinnspenningsmomentene i matrisen med endemomenter
        endemom[i][0] += m1 
        endemom[i][1] += m2 
    return endemom

