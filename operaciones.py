print("presiones 1 si quiere sumar")
print("presiones 2 siquiere restar")
print("presiones 3 para multiplicar")
print("presiones 4 para divicion")
print("presiones 5 para sacarl el resto")
print("presiones 6 para potencia")

op= float(input("ingrese la operacion: "))
numb1= float(input("ingrese el primer numero"))
numb2= float(input("ingrese el segundo numero"))

if op==1:
    suma=(numb1+numb2)
    print("la suma de",numb1,"y",numb2,"es",suma,)
else:
    if op==2:
        resta=(numb1-numb2)
        print("la resta de",numb1,"y",numb2,"es",resta)
    else:
        if op==3:
            multi=(numb1*numb2)
            print("la multiplicacion de",numb1,"y",numb2,"es",multi)
        else:
            if op==4:
                if numb2==0:
                    print("no se puede dividir entre 0")
                else:
                    div=(numb1/numb2)
                    print("la divicion de",numb1,"y",numb2,"es",div)
            if op==5:
                if numb2==0:
                    print("nu se puede dividir entre 0")
                else:
                    resto=(numb1%numb2)
                    print("el resto de",numb1,"y",numb2,"es",resto)
                    if resto==0:
                        print("el resto es par")
                    else:
                        resto==1
                        print("el resto es impar")
            else:
                if op==5:
                    pontencia=(numb1**numb2)
                    print("la potencia de",numb1,"y",numb2,"es",pontencia)