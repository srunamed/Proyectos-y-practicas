# print("primer valor")
# i=int(input(" "))
# print("segundo valor")
# j=int(input(" "))
# while i<j+1:
#     print(("el valor de i es"),i)
#     i+=1

ini=int(input("ingrese el valor de inicio"))
fin=int(input("ingrese el valor de fin"))
a=ini
b=fin
while ini<=fin:
    par=ini%2
    if par==0:
        print(end=(" "))
        if (ini>=0):
            print(ini,"positivo")
        else:
            print(ini,"negativo")
    ini+=1
else:
    print("\n")
    while a<=b:
        par=a%2
        if par!=0:
            print(end=(" "))
            if (a>=0):
                print(a,"positivo")
            else:
                print(a,"negativo")
        a+=1    
