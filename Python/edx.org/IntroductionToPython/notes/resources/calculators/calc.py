class Geometry():

    def __init__(self):
        pass

    def main(self):

        x = int(input('What is x?: '))

        return print (f'x squared is {self.Square(x)}')

    def Square(self, x):

        return x * x

if __name__=='__main__':
    cls = Geometry()
    cls.main()