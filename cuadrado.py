#cuadrado normalito

# # print("ingrese el simbolo del cuadrado")
# # i=int(input(" "))

# print("ingrese el la renglones")
# j=int(input(" "))
# print("ingrese el columna")
# k=int(input(" "))

# for m in range (1,j+1):
#     for n in range (1,k+1):
#         print("+" ,end=" ")
#     print(" ")



# cuadrado vacio
print("ingrese los renglones")
j=3#altura
print("ingrese las columnas")
k=8#base

for m in range (j):
    for n in range (k):
        if m == 0 or m == j-1 or n == 0 or n == k-1:
            print("*", end=" ")
        else:
            print("*",end=" ")
    print(" ")