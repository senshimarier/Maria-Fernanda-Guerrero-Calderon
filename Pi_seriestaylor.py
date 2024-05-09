import math

def pi():
    contador=0
    acumulador = 0.0
    division_actual=1.0
    suma=True

    while division_actual>0.00052:
        contador+=1
        division_actual=1/contador

        if contador%2 != 0:
            if suma:
                acumulador += division_actual
            else:
                acumulador -= division_actual
            suma = not suma

    return acumulador*4

print("calculate the area of the circle")
x = float(input("Write circle's radius: "))
print("Circle's area is: ", pi()*x**2)