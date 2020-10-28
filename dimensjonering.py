import numpy as np
def dimensjonering(elem, nelem, boyespenninger, flytespenning):
    #lager inndeling av grupper:
    antgrupper = 10 #antall grupper
    prosent = np . zeros (( antgrupper , 3) ) #lager tom liste med plass til prosenter
    #gruppeinndeling:
    g1 = [1,3,5,7]
    g2 = [9, 11, 13, 19]
    g3 = [14, 16]
    g4 = [21, 22]
    g5 = [2, 12 ,15]
    g6 = [4, 10, 17]
    g7 = [6]
    g8 = [8]
    g9 = [20]
    g10 = [18]

    #legger bøyespenningnene for hver gruppe i ny liste
    boyeG1 = [abs(boyespenninger[g1[0]-1]) , abs(boyespenninger [g1[1]-1]) , abs(boyespenninger [g1[2]-1]) , abs(boyespenninger [g1[3]-1])]
    boyeG2 = [abs(boyespenninger[g2[0]-1]) , abs(boyespenninger [g2[1]-1]) , abs(boyespenninger [g2[2]-1]) , abs(boyespenninger [g2[3]-1])]
    boyeG3 = [abs(boyespenninger [g3[0]-1]) , abs(boyespenninger [g3[1]-1])]
    boyeG4 = [abs(boyespenninger [g4[0]-1]) , abs(boyespenninger [g4[1]-1])]
    boyeG5 = [abs(boyespenninger [g5[0]-1]) , abs(boyespenninger [g5[1]-1]), abs(boyespenninger [g5[2]-1])]
    boyeG6 = [abs(boyespenninger [g6[0]-1]) , abs(boyespenninger[g6[1]-1]) , abs(boyespenninger [g6[2]-1])]
    boyeG7 = [abs(boyespenninger [g7[0]-1])]
    boyeG8 = [abs(boyespenninger [g8[0]-1])]
    boyeG9 = [abs(boyespenninger [g9[0]-1])]
    boyeG10 = [abs(boyespenninger [g10[0]-1])]

    #finner største bøyespenning i hver gruppe
    storsteBoyespG1 = np.amax( boyeG1 )
    storsteBoyespG2 = np.amax( boyeG2 )
    storsteBoyespG3 = np.amax( boyeG3 )
    storsteBoyespG4 = np.amax( boyeG4 )
    storsteBoyespG5 = np.amax( boyeG5 )
    storsteBoyespG6 = np.amax( boyeG6 )
    storsteBoyespG7 = np.amax( boyeG7 )
    storsteBoyespG8 = np.amax( boyeG8 )
    storsteBoyespG9 = np.amax( boyeG9 )
    storsteBoyespG10 = np.amax( boyeG10 )
    print(storsteBoyespG1)

    #finner plassen i gruppa til elementet med størst bøyespenning
    ind1 = np.where(boyeG1 == storsteBoyespG1)[0][0]
    ind2 = np.where(boyeG2 == storsteBoyespG2)[0][0]
    ind3 = np.where(boyeG3 == storsteBoyespG3)[0][0]
    ind4 = np.where(boyeG4 == storsteBoyespG4)[0][0]
    ind5 = np.where(boyeG5 == storsteBoyespG5)[0][0]
    ind6 = np.where(boyeG6 == storsteBoyespG6)[0][0]
    ind7 = np.where(boyeG7 == storsteBoyespG7)[0][0]
    ind8 = np.where(boyeG8 == storsteBoyespG8)[0][0]
    ind9 = np.where(boyeG9 == storsteBoyespG9)[0][0]
    ind10 = np.where(boyeG10 == storsteBoyespG10)[0][0]

    #finner elementnummertet
    index1 = g1[ind1]
    index2 = g2[ind2]
    index3 = g3[ind3]
    index4 = g4[ind4]
    index5 = g5[ind5]
    index6 = g6[ind6]
    index7 = g7[ind7]
    index8 = g8[ind8]
    index9 = g9[ind9]
    index10 = g10[ind10]

    #henter ut bøyespenning i ende1, midt/under last og ende 2
    #deler på flytspenningen og multipliserer med 100 for å finne prosent
    #legger dette til i listen med prosenter
    prosent [0] = ( abs(boyespenninger[index1-1]) / flytespenning ) *100
    prosent [1] = ( abs(boyespenninger[index2-1]) / flytespenning ) *100  
    prosent [2] = ( abs(boyespenninger[index3-1]) / flytespenning ) *100
    prosent [3] = ( abs(boyespenninger[index4-1]) / flytespenning ) *100
    prosent [4] = ( abs(boyespenninger[index5-1]) / flytespenning ) *100
    prosent [5] = ( abs(boyespenninger[index6-1]) / flytespenning ) *100
    prosent [6] = ( abs(boyespenninger[index7-1]) / flytespenning ) *100
    prosent [7] = ( abs(boyespenninger[index8-1]) / flytespenning ) *100
    prosent [8] = ( abs(boyespenninger[index9-1]) / flytespenning ) *100
    prosent [9] = ( abs(boyespenninger[index10-1]) / flytespenning ) *100
    
    return prosent
    
