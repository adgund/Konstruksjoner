import numpy as np

def arealmoment(ntvsnitt, tvsnitt, nelem, elem):
    andreArealmoment = np.zeros(nelem) #oppretter tom liste til arealmoment
    zc = np.zeros((nelem, 1)) #oppretter tom liste til arealsenter
    
    for i in range(nelem): #går gjennom alle elementer
        for j in range(ntvsnitt): #går gjennom tverrsnitt
            if elem[i][3] == 1: #hvis I-profil
                if tvsnitt[j][0] == 1: #hvis I-profil
                    if elem[i][6] == tvsnitt[j][7]: #hvis elem og tverrnitt i samme gruppe
                        hs = tvsnitt[j][1] #høyde steg
                        ts = tvsnitt[j][2] #tykkelse steg 
                        tft = tvsnitt[j][3] #tykkelse flens topp
                        bft = tvsnitt[j][4] #bredde flens topp
                        tfb = tvsnitt[j][5] #tykkelse flens bunn
                        bfb = tvsnitt[j][6] #bredde flens bunn
                        #finner I-profilets arealsenter
                        zc_I = ((tfb / 2) * tfb * bfb + (tfb + hs / 2) * hs * ts + (tfb + hs + tft / 2) * tft * bft)/ \
                            (tfb * bfb + hs * ts + tft * bft) 
                        #legger arealsenteret i liste
                        zc[elem[i][5]-1] = zc_I
                        
                        #bruker steiners teorem til å finne 2. arealmoment for I-profil
                        I = ((1/12)* (hs**3 * ts)) \
                            + (1/12) * tft**3 * bft + tft * bft * (zc_I - (tfb + hs + (tft / 2)))**2 \
                            + (1/12) * tfb**3 * bfb + tfb * bfb * (zc_I - tfb / 2)**2 
                        #legger arealmoment i liste
                        andreArealmoment[elem[i][5] - 1] = I  
                
            elif elem[i][3] == 2: #hvis rør
                if tvsnitt[j][0] == 2: #hvis rør
                    if elem[i][6] == tvsnitt[j][7]: #hvis element og tverrnitt i samme gruppe
                        d = tvsnitt[j][1] #diameter
                        t = tvsnitt[j][2] #tykkelse
                        #finner 2.arealmoment for rørtverrsnitt
                        I = (np.pi * (d**4 - (d - (2 * t))**4)) / 64 # pi/64 * (Dy^4 - Di^4)
                        #legger arealmoment i liste
                        andreArealmoment[elem[i][5] - 1] = I 
                        #legger arealsenter i liste
                        zc[elem[i][5] - 1] = d / 2
            
    return andreArealmoment, zc #returnerer 2. arealmoment og arealsenter
