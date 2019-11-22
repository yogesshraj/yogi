

Number = int(input(" Please Enter any Number: "))
count = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and Number != 1):
    #print(" %d is a Prime Number" %Number)
    print (Number,"is a prime number")
else:
    print("%s is not a Prime Number" %Number)
