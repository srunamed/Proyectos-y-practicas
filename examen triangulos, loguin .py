respesta = ""
while respesta != "no":
    respesta = input ("hola quieres crear un figura" "(si/no)?")
    if respesta == "si":
        print("triangulo nomal" "(1)")
        print("triangulo apuntando a la derecha" "(2)")
        print("piramide" "(3)")
        print("diamante" "(4)")
        print("cuadrado" "(5)")
        op=int(input("escribe que quieres hacer. "))
        if op>5 or op<1:
            print("no")
        else:
            if op==1:
                print("TRIANGULO")
                i=int(input("pon la altura. "))
                for j in range (0,i,1):
                    for k in range(0,j+1,1):
                        print("*",end="")
                    print("")
            elif op==2:
                    print("TRIANGULO A LA IZQUIERDA")
                    i=int(input("pon la altura. "))
                    for j in range (i,-1,-1):
                        for k in range(j):
                            print(" ",end="")
                        for l in range(j,i):
                            print("*",end="")
                        print("")
            elif op==3:
                    print("PIRAMIDE")
                    i=int(input("pon la altura. "))
                    for j in range (0,i,1):
                        for k in range(0,j+1,1):
                            print("*",end="")
                        print("")
                    for j in range (i-1,0,-1):
                        for k in range(0,j,1):
                            print("*",end="")
                        print("")
            elif op==4:
                    print("DIAMANTE")
                    i=int(input("pon la altura. "))
                    for j in range(i+1):
                        for k in range(i-j):
                            print(" ",end="")
                        for l in range(2*j-1):
                            print("*",end="")
                        print("")
                    for j in range(i-1,0,-1):
                        for k in range(i-j):
                            print(" ",end="")
                        for l in range(2*j-1):
                            print("*",end="")
                        print("")
            elif op==5:
                print("CUADRADO")
                j=int(input("pon la altura. "))
                k=int(input("pon las columnas. "))

                for m in range (j):
                    for n in range (k):
                        if m == 0 or m == j-1 or n == 0 or n == k-1:
                            print("*", end="")
                        else:
                            print("#",end="")
                    print(" ")
print("Ten un buen dia, no olvides beber agua.")