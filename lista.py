# lista=[1,2,3,4]
# print("lista numeros")
# lista.append(5)
# lista.extend([6,7,8,9])
# print(lista)

# lista=[2,3,4,5,6,7,8,9]
# print("remover con for")
# lista.remove(3)
# print(lista)

#lista, eliminando numeros repetidos
# lista=[1,3,2,3,4,3,5,3,6,3,7,8,3,9]
# print(len(lista))
# print(lista)
# i=0
# while i<=len(lista):
#     if 3 in lista:
#         lista.remove(3)
#     i+=1
# print(lista)

#lista en reversa
# print("\n")
# lista=[1,4,5,6,7,3,4,5,5]
# lista.reverse()
# print(lista)

#lista de reverse sin reverse
# print("\n")
# lista1=[1,2,3,4,5,6,7]
# print(lista1)
# lista_reversa=[]
# for value in lista1:
#     lista_reversa=[value] + lista_reversa
# print(lista_reversa)

#Ejemplo ciclo while
# b=[9,8,7,6,5,4,3,2,1]
# lista_reversa=[]
# while b:
#     lista_reversa.append(b.pop())
#     print(lista_reversa)
#par que solo se vea el resultado final
# b=[9,8,7,6,5,4,3,2,1]
# lista_reversa=[]
# while b:
#     lista_reversa.append(b.pop())
# print(lista_reversa)

#ejemplo ciclo for lista
# lista=["apple","orange","banana","tiranidos"]
# for index, item in enumerate(lista):
#     print(index,item)

#la suma de numeros pares en la lista
# lista=[1,2,3,4,5,6,7,8,9,10,11,12]
# suma_de_eventos=0
# for item in lista:
#     if item % 2 == 0:
#         suma_de_eventos += item
# print(suma_de_eventos)

#obtener una nueva lista con los elementos de otra lista al cuadrado
# lista=[1,2,3,4,5,6]
# lista2= [item**2 for item in lista]
# print(lista2)

lista=[]
nombre=input("ingresar nombre. ")
for i in nombre:
    lista.append(i)
    if ("a","e","i","o","u") in (lista):
        lista.remove("a","e","i","o","u")
    print(lista)