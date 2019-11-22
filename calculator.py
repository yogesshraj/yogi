
#calculator


def calculator(num1,num2,operation):
	if operation=="add":
		a=num1+num2
		return a
	elif operation=="subtract":
		a=num1-num2
		return a
	elif operation=="multiply":
		a=num1*num2
		return a
	elif operation =="divide":
		a=num1/num2
		return a
# calculator(20,25,"add")
# calculator(40,3,"subtract")
# calculator(10,4,"multiply")
# calculator(40,4,"divide")
q=int(input("enter the number1:"))
w=int(input("enter the number2:"))
a=input("which operation do u need (add/subtract/multiply/divide):")
if a=="add":
	print (calculator(q,w,"add"))
elif a=="subtract":
	print (calculator(q,w,"subtract"))
elif a=="multiply":
	print (calculator(q,w,"multiply"))
elif a=="divide":
	print (calculator(q,w,"divide"))

