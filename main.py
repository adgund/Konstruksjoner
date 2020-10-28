import numpy as np
from lesefil import lesefil
from lengder import lengder
from arealmoment import arealmoment
from boyestivhet import boyestivhet
from fastinnspenningsmoment import fastinnspenning
from lastvektor import lastvektor
from stivhetsmatrise import stivhetsmatrise
from randbet import randbetingelser
from rotasjoner import rotasjon
from endemoment import endeM
from skjaerkraft import skjaerkrefter
from midtmoment import midtmoment
from boyespenning import boyespenning
from dimensjonering import dimensjonering
from structure_visualization import *


def main():
    #-----Konstanter---
    flytspenning = 355000000 #[Pa]

    #-----Verider fra funksjoner----
    npunkt, punkt, nelem, elem, nlast, last, ntvsnitt, tvsnitt = lesefil()
    elementlengder = lengder(punkt, elem, nelem)
    I, zc = arealmoment(ntvsnitt, tvsnitt, nelem, elem)
    EI = boyestivhet(nelem, elem, I)
    fim = fastinnspenning( nelem , nlast , last , elementlengder )
    R = lastvektor(npunkt, nelem, elem, fim, nlast, last)
    K = stivhetsmatrise(npunkt, nelem, elem, elementlengder, EI)
    Kn, Rn = randbetingelser ( npunkt , punkt , K , R )
    rot = rotasjon(Kn, Rn) 
    endemoment = endeM ( nelem , elem , elementlengder , rot , fim , EI )
    midtmom = midtmoment(nelem, elem, nlast, last, elementlengder, endemoment)
    skjaer = skjaerkrefter( nelem ,elem, endemoment, nlast ,last, elementlengder)
    spenning = boyespenning (midtmom, endemoment, nelem, I, zc) 
    dim = dimensjonering(elem, nelem, spenning, flytspenning) #OBS! for å kjøre oppgave c) må denne kommenteres ut
    #dette fordi den er laget spesifikt for vår oppgave, og virker ikke som en generell funksjon
    for i in range (nelem):
        print(i+1, I[i])
    fig_init, ax_init, fig_def, ax_def = setup_plots()

    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    # Endre gjerne selv
    first_index = 1
 
    # -----Plott initalramme-----
    plot_structure(ax_init, punkt, elem, 1, first_index)
 
    #-----Skriver ut rotasjoner-----
    print("Rotasjoner i de ulike punktene:")
    for i in range(npunkt):
        print(i+1, round(rot[i][0]*180/np.pi, 4))
 
    #-----Skriver ut endemomentene------
    print("Elementvis endemoment [kNm]:")
    print('Moment lokal ende 1', '\t\t', 'Moment lokal ende 2')
    print('----------------------------------')
    for i in range (nelem):  
        print(i+1, '|' '\t', round(endemoment[i][0] * 10**-3, 4), '\t\t\t', round(endemoment[i][1]*10**-3,4) )
    
    #-----Skriver midtmomentene--------
    print('Elementvis midtmoment [kNm]:')
    print('Midtmoment')
    print('------------')
    for i in range (nelem):
        print(i+1, '|', '\t', np.round(midtmom[i][0]* 10**-3, 4))

    #------Skriver skjærkreftene-----
    print('Elementvis skjærkraft')
    print('Skjær lokal ende 1', '\t\t', 'Skjær lokal ende 2')
    print('------------------------------------------------')
    for i in range (nelem):  
        print(i+1, '|' '\t', round(skjaer[i][0] * 10**-3, 2), '\t\t\t', round(skjaer[i][1]*10**-3,2) )

    #--------Skriver bøyespenning---------
    print('Elementvis bøyespenning:')
    print('Spenning lokal ende 1', '\t\t\t', 'Spenning midt/under last', '\t\t\t', 'Spenning lokal ende 2')
    print('----------------------------------------------------------------------------------------------')
    for i in range(nelem):
        print(i+1, '|' '\t', round(spenning[i][0] * 10**-6, 2), '\t\t\t', round(spenning[i][1]*10**-6,2), '\t\t\t', round(spenning[i][2]*10**-6,2))


    #-----Plott deformert ramme-----
    skalering = 50     # Du kan endre denne konstanten for å skalere de synlige deformasjonene til rammen
    plot_structure_def(ax_def, punkt, elem, 1, first_index, skalering*rot)
    plt.show()

main()    