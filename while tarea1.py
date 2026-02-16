respesta = ""
while respesta != "no":
    respesta = input ("hola quieres hacer una operacion. " "(si/no)?")
    if respesta == "si":
        print("hola, para realizar una operacion por favor ingrese un numero")
        print("ingrese 1 para suma")
        print("ingrese 2 para resta")
        print("ingrese 3 para multiplicacion")
        print("ingrese 4 para division")
        op=int(input(" "))

        if op>4 or op<1:
            print("no existe esa operacion")
        else:

            print("ingrese hasta donde")
            i=int(input(" "))
            print("ingrese el largo")
            k=int(input(" "))

            if op==1:
                for i in range(0,i+1):
                    print("la operacion suma de",i,"es")
                    for j in range(0,k+1):
                        print(i,"+",j,"=",i+j,) 
            elif op==2:
                for i in range(0,i+1):
                    print("la operacion resta de",i,"es")
                    for j in range(0,k+1):
                        print(i,"-",j,"=",i-j,)
            elif op==3:
                for i in range(0,i+1):
                    print("la operacio multiplicacion de",i,"es")
                    for j in range(0,k+1):
                        print(i,"*",j,"=",i*j,)
            elif op==4:
                if i==0:
                    print("no se puede dividir para 0")
                else:
                    for i in range(0,i+1):
                        print("la operacion division de",i,"es")
                        for j in range(0,k+1):
                            print(i,"/",j,"=",i/j,)
print("okay, ten un buen dia. ")