averagesum.py

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
a=0
l=len(elements)
c=0
C=0
d=0
D=0
while a<l:
	if elements[a]%2 is 0:
		c+=elements[a]
		C+=1
	else:
		d+=elements[a]
		D+=1
	a+=1
print(c," even numbers")
print(d," odd numbers")
print(C," EVEN")
print(D," odd")
print(c/C ," IS AVERAGE OF EVEN numbers")
print(d/D," IS AVERAGE OF odd numbers")                                                       
print((c+d)/(l-1)," is overall average")
