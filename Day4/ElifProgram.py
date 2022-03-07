'''
Created on 05-Mar-2022

@author: ELCOT
'''
year=int(input("Enter your year of birth :"))
if 1980<=year<1990:
    print("You are a 80's kid")
elif 1990<=year<2000:
    print("You are a 90's kid")
elif year>2000:
    print("You are a 2k kid")
else: print("Sorry old man")