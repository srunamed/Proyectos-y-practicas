respesta = ""
l=0
while respesta != "no":
    respesta = input ("quiere continuar" "(si/no)?")
    if respesta == "si":
        i= int(input("numero inicual"))
        j= int(input("numero final"))
        # se pone la vatiable para que marque solo un resultado
        # l=0
        while i<=j:
            if i%2 !=0:
                l=l+i
                print(i,"+",i,"=",l)
            i+=1
print("buen dia")