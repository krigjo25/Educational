#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 6 - Data exploration and Analysis
Created on Thu Apr 22 23:38:44 2021

@author: krigjo25

We will cover how we workik with data files and data frames. 
Pandas and Numpy function will be introduced.

We'll use a sample fictional dataset which contain house sale prices, based on the house features. Such as
    Year built
    Square Footage
    House Type
    Garage Size
    Fireplaces
    Pool
    Sale Price
    
    Exlpore and Clean data with Pandas
    Pandas 
    
    Pandas 
     allow us to work with data as organized data frames.

     # Importing a function which is called pandas
     import pandas as pd # Keyword for function usage
"""
import pandas as pd 
df = pd.read_csv('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Educational\\Programming\\Python\\Machine learning\\Notes\\csv\\HouseSalesValues.csv')
 # 10 first rows of our ds
print("Prints 10 first rows of ds")
print(df.head(10))
