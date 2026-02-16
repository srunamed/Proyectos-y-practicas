#una funcion es un bloque de codigo asociado un nombre
# def saludo():
#     print("hola que tal?. ")
# saludo()
# print("\n")

# def hola(nombre):
#     print("estudiando",nombre)
# hola("Mat ")
#print("\n")
#-----------------------------------------------------------------------------------------------------------


def suma():
    i=float(input("primer numero. "))
    j=float(input("segundo numero. "))
    k=i+j
    print(k)
#suma()

def resta():
    i=float(input("primer numero. "))
    j=float(input("segundo numero. "))
    k=i-j
    print(k)
#resta()

def multiplicacion():
    i=float(input("primer numero. "))
    j=float(input("segundo numero. "))
    k=i*j
    print(k)
#multiplicacion()

def divicion():
    i=float(input("primer dato. "))
    j=float(input("segundo dato. "))
    if j==0:
        print("no se puede divir para 0. ")
    else:
        k=i/j
        print(k)
#divicion()
respuesta=""
while resta != "no":
    respuesta=input("quieres realizar una operacion?" "(si/no?)")
    if respuesta =="si":
        op=int(input("introduzca 1(suma),2(resta),3(multiplicacion),4(division)"))
        if op>=1 and op<=5:
            if op==1:
                suma()
            elif op==2:
                resta()
            elif op==3:
                multiplicacion()
            elif op==4:
                divicion()
        else:
            print("no se puede")
print("ten un buen dia. ")