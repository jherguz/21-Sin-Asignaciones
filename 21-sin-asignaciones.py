import random
import math
          
def baraja(mazo,mazoBase,rnd,t):
    if(len(mazo)<=40):
        if(len(mazoBase)>=1 and t>1):
            mazo.append(mazoBase[rnd])
            mazoBase.pop(rnd)
            baraja(mazo,mazoBase,math.floor(random.randrange(0,t-1)),t-1)
    return mazo
 
def jugador(baraja, manoJugador,manoBanca):
    print("Mano del Jugador: ", manoJugador)    
    if(len(manoJugador)<2 and len(manoBanca)<2):
        jugador(baraja[2:],manoJugador+[baraja[0]]+[baraja[1]],manoBanca+[baraja[0]]+[baraja[1]])
    else:
        if(comprobar_mano(manoJugador)<=21):            
            if(comprobar_mano(manoJugador)==21):
                print("Ganaste")
            elif(input("Quiere una carta?  ")==('s' or 'S')):
                print(len(manoJugador))
                jugador(baraja[1:],manoJugador+[baraja[0]],manoBanca+[baraja[math.floor(random.randrange(0,40))]])                
            else:
                print("Mano del Jugador: ", manoJugador)
                print(comprobar_mano(manoJugador))
                print("Mano de la Banca : ", manoBanca)
                print(comprobar_mano_AI(manoBanca))
                if(comprobar_mano_AI(manoBanca)> comprobar_mano(manoJugador) and comprobar_mano_AI(manoBanca)<=21):
                     print("perdiste")
                elif(comprobar_mano(manoJugador)>comprobar_mano_AI(manoBanca) and comprobar_mano(manoJugador)<=21) or comprobar_mano_AI(manoBanca)>21:     
                     print("Ganaste")
        else:
            print(comprobar_mano(manoJugador))
            print("perdiste")

def comprobar_mano(mazo):    
    if(mazo==[]):
        return 0
    else:
        return mazo[0] + comprobar_mano(mazo[1:])
    
def comprobar_mano_AI(mazo):    
    if(mazo==[]):
        return 0
    else:
        return mazo[0] + comprobar_mano_AI(mazo[1:])
        
jugador(baraja([],[1,1,1,1,2,2,2,2,
                   3,3,3,3,4,4,4,4,
                   5,5,5,5,6,6,6,6,
                   7,7,7,7,8,8,8,8,
                   9,9,9,9,10,10,10,10],
        math.floor(random.randrange(0,40)),40),[math.floor(random.randrange(1,10)),math.floor(random.randrange(1,10))],[math.floor(random.randrange(1,10)),math.floor(random.randrange(1,10))])

