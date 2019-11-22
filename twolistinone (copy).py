twolistinone.py


a=[23,[23,45,76,[46],34,56]]
b=[]
for i in range(len(a)):
	if type(a[i])==int:
		b.append(a[i])
	else:
		for j in range(len(a[i])):
			if type(a[i][j])==int:
				b.append(a[i][j])
			else:
				for k in range(len(a[i][j])):
					if type(a[i][j][k])==int:
						b.append(a[i][j][k])

print(sum(b))