# Checking wheter an Integer is a odd number or a even number
check = int(input( "Type a number, to check if it's even or an odd : "))
mod = int(input("Type another to divide with : "))

if check % 2 == 0:
    print("2. I guess the number is even.")
else:
    print("2  I guess the number is odd.")
    
    ## Dividing two numbers and check if its odd or even

result = check % mod

if check % mod == 0:
    print("2. 1 The numbers which were divided : %d, / %d = %d which is an even number" % (check, mod, result))
elif check % mod == 1:
    print("2.1 The numbers which were divided : %d / %d = %d which is an odd number" % (check, mod, result))
else:
    print("number is below zero")
