'''
Created on 04-Mar-2022

@author: ELCOT
'''
#Python program to get 2 numbers from user and print greatest number 

print('Enter the numbers')
n1=float(input("Enter 1st number: "))
n2=float(input('Enter 2nd number: '))
if n1<n2:
    print(f"{n2} is greater than {n1}")
else:
    print(f'{n1} is greater than {n2}')
