from classList import ListaZ

def Menu():
 while True:   
    #Function to present the user menu and get their choice

    #local variables
    UserChoice = int()

    #Display menu and get choice
    print()
    print("Select one of the options listed below:  ")
    print("\t1\t==\tMostrar Lista")
    print("\t2\t==\tEsvaziar Lista")
    print("\t3\t==\tRemover")
    print("\t4\t==\tExibir Elemento")
    print("\t5\t==\tExibir Posição")
    print("\t6\t==\tEsvaziar")
    print("\t0\t==\tSair")
    print()
    UserChoice = input("Enter choice:  ")
    print()
    

    return UserChoice

def Mostrar_Lista():
    print("test, test, test")

def Esvaziar_Lista():
    print("test, test, test")

def Remover():
    print("test, test, test")

def Exibir_Elementos():
    print("test, test, test")

def BelowLevels():
    print("test, test, test")

def main():
    Choice = int()

    #call GetChoice function


    Choice = Menu()

    #Loop until user quits

    if Choice == 1:
        Mostrar_Lista()


    elif Choice == 2 :
        AverageLevels()
    elif Choice == 3:
        AveragePerZone()
    elif Choice ==  4 :
        AboveLevels()
    elif Choice == 6:
        BelowLevels()


main()
