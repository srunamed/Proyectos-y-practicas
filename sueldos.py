sueldo= float(input("ingrese la cantidad de su sueldo actual: "))

if sueldo<=1000: 
    des1=(sueldo*0.10)
    print("tu sueldo de"" ",sueldo," ""se le ha restado el 10%, por lo cual ahora es",des1)
else:
    if sueldo>1000 and sueldo<=2000:
        des2=(sueldo*0.15)
        print("tu sueldo de"" ",sueldo," ""se le ha restado el 15%, por lo cual ahora es",des2)
    else:
        if sueldo>2000:
            des3=(sueldo*0.18)
            print("tu sueldo de"" ",sueldo," ""se le ha restado el 18%, por lo cual ahora es",des3)