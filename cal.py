#!/usr/bin/python3

#  *********SUMA***********

def Suma ():
    
    Number_one = int(input("Digite el 1st no. de la Suma: "))
    Number_two = int(input("Digite el 2nd no. de la Suma: "))
    result = Number_one + Number_two
    
    print("El resutado es: "+ str(result)+'\n')


#  *********RESTAS***********


def Resta ():
    
    Number_one = int(input("Digite el 1st no. de la Resta: "))
    Number_two = int(input("Digite el 2nd no. de la Resta: "))
    result = Number_one - Number_two 
    
    print("El resutado es: "+ str(result) + '\n')

#  *********DIVISION***********

def Division ():
    
    Number_one = int(input("Digite el 1st no. de la Division: "))
    Number_two = int(input("Digite el 2nd no. de la Division: "))
    result = Number_one / Number_two
    
    print("El resutado es: "+ str(result)+ '\n' )


#  *********Multiplication***********

def Multi ():
    Number_one = int(input("Digite el 1st no. de la Multiplicacion: "))
    Number_two = int(input("Digite el 2nd no. de la Multiplicacion: "))
    result = Number_one * Number_two

    print("El resutado es: "+ str(result) + '\n' )


def SetUp():

    print('************Calculadora********************\n')
    print('Seleccione su operacion con un Digito: \n')
    print('No. 1: Suma')
    print('No. 2: Resta')
    print('No. 3: Division')
    print('No. 4: Multiplicacion\n')

    selector = int(input('Digite su Operacion #> '))

    if  selector == 1:
        print('*****Suma***** \n')
        return Suma()

    elif selector == 2:
        print('*****Resta***** \n')
        return Resta()

    elif selector == 3:
        print('*****Division***** \n')
        Division()
    else:
        print('*****Multiplicacion***** \n')
        Multi()

SetUp()


