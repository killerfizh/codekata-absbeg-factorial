def Leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("Y")
            else:
                print("N")
        else:
            print("Y")
    else:
        print("N")
num = int(input())
Leap(num)
