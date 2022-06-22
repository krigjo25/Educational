class ProStaff:
    # Instializer
    '''             Instance variables
                        pName, 
                        pPos, 
                        pSalary

                    Method / function            
                        __init__,
                        __str__,
                    calculateSalary                    
                                            '''
    def __init__(self, pName,pPos, pSalary):

        self.pos = pPos
        self.name = pName
        self.salary = pSalary

        print('Prostaff employe Created')

        # Readable string
    def __str__(self):
        return 'Name = %s,\nPosition = %s\n Salary = %s\n' % (self.name, self.pos, self.salary)

    
    def calculateSalary(self):
        prmpt = '\nEnter number of hours worked for %s:' %(self.name)
        prompt = '\nEnter the hourly rate for %s:' %(self.name)

        hours, rate = input(prmpt), input(prompt)
        self.salary = int(hours)*int(rate)
        
        return self.salary


'''
Calling the Class
'''   

