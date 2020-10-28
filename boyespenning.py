import numpy as np

def boyespenning (midtmoment, endemoment, nelem, andreArealmoment, z_c):
    sigma = np.zeros((nelem, 3)) #tom liste med plass til spenning i ende 1, midt og ende 2
    for i in range(nelem): #går gjennom alle elementene
        I = andreArealmoment[i] #andre arealmoment
        zc = z_c[i] #arealsenter
        #spenning = Moment/I * zc
        sigma[i][0] += (endemoment[i][0]/I) * zc 
        sigma[i][1] += (midtmoment[i][0]/I)*zc
        sigma[i][2] += (endemoment[i][1]/I)*zc

    return sigma