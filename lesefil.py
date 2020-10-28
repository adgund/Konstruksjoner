import numpy as np


def lesefil():
 
    # Åpner inputfilen
    fid = open("input.txt", "r")
 
    # Leser totalt antall punkt
    npunkt = int(fid.readline()) 
    # Leser knutepunktdata    
    punkt = np.loadtxt(fid, dtype = int, max_rows = npunkt)     
 
    # Leser antall elementer
    nelem = int(fid.readline())
    # Leser elementdata
    elem = np.loadtxt(fid, dtype = np.int64, max_rows = nelem)
 
    # Leser antall laster som virker på rammen
    nlast = int(fid.readline())
    # Leser lastdata
    last = np.loadtxt(fid, dtype = float, max_rows = nlast)     

    # Leser antall tverrsnitt.
    ntvsnitt = int(fid.readline()) 
    # Leser tverrsnittdata
    tvsnitt = np.loadtxt(fid , dtype = float, max_rows = ntvsnitt )

    # Lukker input-filen
    fid.close()
    return npunkt, punkt, nelem, elem, nlast, last, ntvsnitt, tvsnitt

lesefil()




