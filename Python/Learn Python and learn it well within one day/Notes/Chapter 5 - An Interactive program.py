'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                           Chapter 5 - An Interactive program

5.1 Input()

5.2  Print()
    - can have multiple agruments,
    - using triple quotes, will span the message over multiple lines.

5.3 Triple quotes



5.4 Escape characters
    - Tab \t(ab), \\, \", \', \n(ew line) (r not\tab)

'''
uName = input(' Please insert a name : ')
uAge = input('What about insert a age, %s? :' % (uName))
print ('''
        5.0 An interactive program:\n 
        Inserted name : %s, inserdet age %s
    '''%(uName, uAge))