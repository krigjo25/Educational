'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                                    Chapter 4 - Data types in python

 


'''

num = 46652938
print("4.1  integers %s" % (num))

pi = 3.14
print("4.2 float %4.2f" % (pi))


num = 'Hello Python !'
ok = num.upper()
lol = ok.lower()
brand, exr = 'Android', 1.2345
msg = "4.3 Strings\n %s \n %s \n %s \n %s, %4.2f" % (num, ok, lol, brand, exr)
print(msg)

uAlias = ['jhon', 'Jake', 'Timmb']
uAge = [21,23,24,51,53]

print("4.4 Printing the lists : \n", uAlias, uAge)
print("4.4 Printing an index of th list : \n", uAlias[2], ", ", uAge[0])

uAlias.append('Japalano')
print("4.4 Printing a sliced list : \n", uAlias[0:1], ", ", uAge[2:4])
print("4.4 Printing a sliced list with stepper : \n", uAlias[0:3:2], ", ", uAge[0:3:2])

del uAlias[2]
print("4.4 Printing a sliced list : \n", uAlias[0:1], ", ", uAge[2:4])
print("4.4 Printing a sliced list with stepper : \n", uAlias[0:3:2], ", ", uAge[0:3:2])

uAlias = {  0:23,
            1:24,
            2:25,
            3:26,
            4:21,
            5:12}


