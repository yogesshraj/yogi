reverseing


def reverse(a):
	b=[]
	c=len(a)-1
	while c>=0:
		b.append(a[c])
		c-=1
	print (b)
reverse([2,3,4,5,6,6])