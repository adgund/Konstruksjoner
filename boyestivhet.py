import numpy as np

def boyestivhet(nelem, elem, arealmoment):
    boyestivhet = np.zeros((nelem, 1)) #oppretter tom liste for bøyestivhet

    for i in range(nelem): #går gjennom alle elementer
        boyestivhet[i] = arealmoment[i]*elem[i][2] #bøyestivhet = arealmoment * e-modul
    return boyestivhet