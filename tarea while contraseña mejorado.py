# usuario=""
# while usuario != "no":
#     usuario=input("ingresar usuario. ")
#     if usuario == "mat":
#         contraseña=""
#         while contraseña != "no":
#             contraseña=input("ingrese contraseña. ")
#             if contraseña == "123":
#                 print ("bien venido")
#                 i=int(input("ingrese el valor maximo"))
#                 j=0
#                 while i>=j:
#                     print(i+j)
#                     i-=1

usuario=""
contraseña=""
while usuario != "no" and contraseña != "no":
    usuario= input("ingrese usuario. ")
    contraseña= input("ingrese contraseña. ")
    if usuario == "mat" and contraseña == "123":
        print("bien venido")
        i= int(input("ingrese el valor maximo"))
        j=0
        while i>=j:
            print(i+j)
            i-=1
    else:
        print("vuelva a verificar su usuario o contraseña")