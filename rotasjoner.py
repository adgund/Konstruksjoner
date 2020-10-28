import numpy as np

def rotasjon (Kn , Rn ):
    rot = np.linalg.solve( Kn, Rn ) # Løser ligningssystemet for rotasjon
    #Bruker np.linalg.solve for å løse matrisene, og finner derfor rotasjon
    #Kr = R der r er rotasjoner
    return rot
