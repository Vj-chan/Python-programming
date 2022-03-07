'''
Created on 05-Mar-2022

@author: ELCOT
'''
mark=float(input("Hi student, Enter your mark :"))
if 0<=mark<35:
    print("Sorry, you failed in the  exam")
elif 35<=mark<=100:
    print("Congratulations, you passed in the exam")
else:
    print("Sorry, Mark out of range")
