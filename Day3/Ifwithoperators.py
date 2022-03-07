'''
Created on 04-Mar-2022

@author: ELCOT
'''
print('Enter the numbers')
n1=float(input("Enter 1st number: "))
n2=float(input('Enter 2nd number: '))
if n1!=n2:
    print(f"{n1} is not equal to {n2}")
if n1<n2:
    print(f"{n2} is greater than {n1}")
if n1>n2:
    print(f"{n1} is greater than {n2}")
if n1>=n2:
    print(f"{n1} is greater than or equal to {n2}")
if n1<=n2:
    print(f"{n1} is lesser than or equal to {n2}")