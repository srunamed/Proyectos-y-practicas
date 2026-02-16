respesta = ""
while respesta != "no":
    respesta = input ("hola quieres crear una nueva lista" " " "(si/no)?")
    if respesta == "si":
        lista=[]
        j=int(input("cuantos datos vas a ingresar?. "))
        i=0
        while i<=j-1:
            g=input("ingrese numero")
            lista.append(g)
            i+=1
        print(lista)
print("ten un buen dia")