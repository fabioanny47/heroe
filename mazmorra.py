derrotMostruos = 0
monstruovenc = 0
derrota = 0
nivelHeroe = 0
print("vas a entrar  ala mazmorra")
numMonstruos = int (input("ingrese el numero de mosntruos en la mazmorra "))
while numMonstruos > 0  :
    if nivelHeroe == 0 : 
        print ("te vas a enfrentar a un monstruo")
        nivelMonstruo = int (input("ingrese nivel del monstruo "))
        nivelHeroe = int (input("ingrese el nivel del heroe "))
        derrotMonstruos = numMonstruos - monstruovenc
        derrota

    
    else :
        print ("te vas a  enfrentar a otro monstruo")
        nivelMonstruo = int (input("ingrese nivel del monstruo "))
        derrotMonstruos = numMonstruos - monstruovenc
        
    if nivelMonstruo <= nivelHeroe :
        print ("mosntruo derrotado")
        nivelHeroe = nivelHeroe +1
        nivelH2 = nivelHeroe
        numMonstruos = numMonstruos -1
        print("nivel del heroe",nivelHeroe)
    else :
        print("el heroe ha sido derrotado")   
        break 
