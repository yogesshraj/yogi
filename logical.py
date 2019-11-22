

# queston 
# taken_list = list(input("enter anything to make a string: "))
# new_list = []

# while taken_list:
#     minimum = taken_list[0]  
#     for x in taken_list: 
#          if x < minimum:
#              minimum = x
#     new_list.append(minimum)
#     taken_list.remove(minimum)   
# print (new_list)

# ___________________________________________________________________________________________________________________________________________-



# a=[23,2,[23,45,76,[46],34,56]]
# b=[]
# for i in range(len(a)):
# 	if type(a[i])==int:
# 		b.append(a[i])
# 	else:
# 		for j in range(len(a[i])):
# 			if type(a[i][j])==int:
# 				b.append(a[i][j])
# 			else:
# 				for k in range(len(a[i][j])):
# 					if type(a[i][j][k])==int:
# 						b.append(a[i][j][k])
# print (b)


# _________________________________-______________________________________________________________________________________________--


# matrx_list= [[12,7,7],
#     [4 ,5,5],
#     [3 ,8,6]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# s=[]

# for i in range(len(matrx_list)):
#    for j in range(len(matrx_list[0])):
#        result[j][i] = matrx_list[i][j]

# for r in result:
# 	print (r)

# _____________________________________________________________________________________________________________________________________________


# for i in range(32,128):
# 	print (chr(i),end='')
# 	if (i-1)%10==0:
# 		print ()
# print ()

# a=33
# b=chr(a)
# print (b)

# a=int(input("Enter a number: "))
# for i in range(1,a+1):
# 	for j in range(1,a-i+1):
# 		print (end=" ")
# 	for j in range(i,0,-1):
# 		print (j,end="")
# 	for j in range(2,i+1):
# 		print (j,end="")
# 	print ()


# a=input("enter the input: ")
# length=len(a)
# for i in range(length):
# 	for j in range(len(a)-i-1):
# 		print (end=" ")
# 	for j in range(i+1):
# 		print (a[j],end=' ')
# 	print ()



# a=input("Enter the string:")
# i=0
# s={}
# print ("{",end="")
# while i<len(a):
# 	if i%2!=0:
# 		print (s[i]=s[i+1],end=" ")
# 	if i%2==0:
# 		print (s[i]=s[i+1],end=':')
# 	i+=1
# print ("}",end="")
# print ()


# a=input("enter the string: ")
# s={}
# i=0
# if len(a)%2!=0:
# 	while i < len(a)-1:
# 		s[a[i]]=a[i+1]
# 		i+=2
# else:
# 	while i < len(a):
# 		s[a[i]]=a[i+1]
# 		i+=2
# print (s)

