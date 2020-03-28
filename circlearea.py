def Area_Circle(r):
    if (r<0):
        print("Error")
    else:
        res = round(3.14159265359*r*r, 2)
        print(res)
a = float(input())
Area_Circle(a)
