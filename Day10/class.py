# Python program using class

class marks:
    def __init__(self,eng: float,tam: float,mat: float,sci: float,ss: float):
        self.eng = eng
        self.tam = tam
        self.mat = mat
        self.sci = sci
        self.ss = ss
        
        

vijay = marks(90,93,94,83,85)
ajith = marks(87,98,92,95,100)
rajinikanth = marks(100,100,100,100,100)

print('''1 - vijay
2 - ajith
3 - rajinikanth''')
rollnum = int(input('Enter roll number : '))

if rollnum==1:
    name=vijay
elif rollnum==2:
    name=ajith
elif rollnum==3:
    name=rajinikanth
else:
    print('Invalid roll number ')


print(f'The marks are :')
print('Tamil = ', name.tam)
print('English = ', name.eng)
print('Mathematics = ', name.mat)
print('Science = ', name.sci)
print('Social science = ', name.ss)