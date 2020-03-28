def Mon_Day(n):
  if (0<n<13):
  	dict = {1:"31", 2:"28", 3:"31", 4:"30", 5:"31", 6:"30", 7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"}
  	print(dict[n])
  else:
    print("Error")
day = int(input())
Mon_Day(day)
