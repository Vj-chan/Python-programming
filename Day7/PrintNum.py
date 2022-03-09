#Python program to print range of numbers in desired order

x=int(input('Enter start number : '))
y=int(input('Enter end number : '))

print(' Press 1 for ascending order \n Press 2 for descending order ' )

cho=int(input('Enter your choice :'))

match cho:
    case 1:
        for m in range(x,y+1):
            print(m)
    case 2:
        for n in reversed(range(x,y+1)):
            print(n)