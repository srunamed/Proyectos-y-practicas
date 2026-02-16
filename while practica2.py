
# i= int(input("cuantas lunas tiene Jupiter?"))
# while  i !=79:
#     i = int(input("respuesta equivocada, responde otra vez"))
# print("felicidades")


# i=int(input("escribe la tabla de multiplicacion"))
# j=0
# while j <= 10:
#     print(i,"*",j,"=",i*j)
#     j+=1


# i=int(input("numero inicial" ))
# j=int(input("numero final" ))
# a=i
# b=j
# while i<=j:
#     if i%2 == 0:
#         print("par",i)
#     i+=1
# else:

#     while a<=b:
#         if a%2 != 0:
#             print("impar",a)
#         a+=1

respuesta="si"
while respuesta != "no":
    print("ingresar nombre")
    i=input()
    print("calificaciones a promediar")
    j=int(input())
    l=0
    for i in range(1,j+1):
        print("ingresar",i,"a. calificacion")
        k=float(input())
        l=l+k
c=l/