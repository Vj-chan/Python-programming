'''
Created on 04-Mar-2022

@author: ELCOT
'''
#Python program to find whether the student is passed in all subjects

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
if t>=35 and e>=35 and m>=35 and sc>=35 and soc>=35:
    print("Congratulations, You have passed in all the subjects")
else:
    print('Sorry, You have not passed in all the subjects')

