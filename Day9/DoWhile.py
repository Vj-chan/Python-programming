#Python program for emulating do while concept of printing numbers upto 5


x=int(input('Enter a number '))

print(x)

while x<=5:
    x=x+1
    if x>5:
        break
    print(x)