'''
Created on 03-Mar-2022

@author: ELCOT
'''
#Python code to get marks and print total and percentage

print("Hi student, Enter your subject wise marks")
t=float(input(' Tamil = '))
e=float(input(' English = '))
m=float(input(' Mathematics = '))
sc=float(input(' Science = '))
soc=float(input(' Social = '))
total=t+e+m+sc+soc
perc=total/5
print('Your total mark is ',total)
print(f'Your percentage is {perc} %')
