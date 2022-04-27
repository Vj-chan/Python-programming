print("*~*~*Hi 90's kid, Welcome to the real FLAMES Calculator by Vj chan*~*~*")


#Get the names in lower case and remove the spaces

name1=input('Enter your name : ').lower().replace(' ','')
name2=input('Enter your partner name : ').lower().replace(' ','')


#Convert the names into separate iterable list

ln1=list(name1)
ln2=list(name2)


#Find the longest name and store its length in a variable

if len(ln1)>len(ln2):
	cchk=len(ln1)
else:
	cchk=len(ln2)


#Find and remove the common characters from the names

count=0
while count!=cchk:
	count+=1
	for i in ln1:
		for j in ln2:
			if i==j:
				ln1.remove(i)
				ln2.remove(j)
				break			
#print(ln1)
#print(ln2)


#Calculate the total number of remaining letters

length=len(ln1)+len(ln2)
#print(length)


#Strike out the characters of flames according to the calculated length till last one

f='flames'
count=0
while count!=5:
	count+=1
	lstf=list(f)*length
	strike=lstf.pop(length-1)
	f1,f2=f.split(strike)
	f=f2+f1


#Create a dictionary to get the abbreviation from the remained character in flames

fdict={'f':'Friends', 'l':'Love', 'a':'Affection', 'm':'Marriage', 'e':'Enemy', 's':'Sister'}

result=fdict.get(f)


#Print the relationship from the dictionary

print(f'The relationship between you and your partner is {result}')
