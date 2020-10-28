import numpy as np

def elementstivhetsmatrise ( nelement, element , elementlengder, arealmoment):

    matrise = np.zeros ((nelement, 4)) #tom matrise

    for i in range ( nelement ): # Går gjennom elementer
        E = element [i][2] # elastisitetsmodul for element i
        L = elementlengder[i] #elementlengde for element i
        I = arealmoment[i]
        elementstivhet = ((4 * E * I/ L) * np.array([[1.0 ,0.5, 0.5 ,1]])) #elementstivhet
        matrise[i] = elementstivhet # legger til elementstivheten i matrisen

    return matrise

