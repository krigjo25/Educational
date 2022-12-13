#   Importing libraries
import pandas as pd

class Norway():

    def __init__(self): pass

    def main(self):

        return

    def AnmeldteLovBrudd(self):
        df = pd.read_csv('../resources/csv/anmeldteLovbruddsgruppe.csv')

        print(df)

if __name__ == '__main__':
    cls = Norway()
    cls.main()
