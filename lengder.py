import numpy as np

def lengder(knutepunkt, element, nelem):
 
    elementlengder = np.zeros((nelem, 1))
    # Beregner elementlengder 
    for i in range (0, nelem):
        dx = knutepunkt[element[i][0] - 1] [0] - knutepunkt[element[i][1] - 1] [0] #henter lengde i x-retning
        dy = knutepunkt[element[i][0] - 1] [1] - knutepunkt[element[i][1] - 1] [1] #henter lengde i y-retning
        elementlengder[i] = np.sqrt(dx * dx + dy * dy) #bruker Pytagoras til å beregne elementlengder
    return elementlengder


