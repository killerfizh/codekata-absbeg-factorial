def SI(p,t,r):
	si = round((p*t*r)/100, 2)
	print(si)
a, b, c = map(float, input().split())
SI(a,b,c)
