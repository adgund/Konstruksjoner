import numpy as np


def stivhetsmatrise ( npunkt , nelem , elem , L , EI ) :
    generell = np . array ([[4 , 2] , [2 , 4]]) #lagen en generell stivhetsmatrise
    K = np.zeros (( npunkt , npunkt )) #oppretter tom nxn matrise
    for i in range (nelem): #går gjennom alle elementene
        #Legger elementene på riktig plass i matrisen
        K[elem[i][0] - 1][elem[i][0] - 1] += (generell[0][0] * EI[i]) / L[i] #generell*EI/L
        K[elem[i][0] - 1][elem[i][1] - 1] += (generell[0][1] * EI[i]) / L[i]
        K[elem[i][1] - 1][elem[i][0] - 1] += (generell[1][0] * EI[i]) / L[i]
        K[elem[i][1] - 1][elem[i][1] - 1] += (generell[1][1] * EI[i]) / L[i]
    return K
