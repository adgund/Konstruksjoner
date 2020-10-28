import numpy as np
def randbetingelser ( npunkt , punkt , K , R ):
    Kn = K.copy () #Oppretter en kopi av stivhetsmatrisen
    Rn = R.copy () #Oppretter en kopi av lastvektoren
    for i in range (npunkt): #går gjennom alle knutepunkter
        if punkt [i][2] == 1: #Hvis fast innspenning
            Rn [i] = 0 # Setter knutepunkt i lastvektoren lik 0
            for j in range (npunkt):
                Kn [j][i] = 0 # Setter tilsvarende rad i lastvektor lik 0
                Kn [i][j] = 0 # Setter tilsvarende kolonne i lastvektor lik 0
            Kn [i][i] = 1 #Setter diagonalelementer som er satt lik 0 lik 1 (ulik 0)
            #Dette gjør at ligningen er mulig å løse
    return Kn , Rn