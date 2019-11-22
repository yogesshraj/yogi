howmanytimes.py

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
unigue=set(char_list)
u=list(unigue)
print(u)
l=len(unigue)
a=0
A=[]
while a<l:
	c=char_list.count(u[a])
	print (u[a]+" is  " + str(c)+" times")
	aa=[u[a],c]
	A.insert(l-1,aa)
	a+=1
print(A)