"""
# List variables
"""
stooges=["Moe","Larry","Curly"]
print stooges

#mutation 
#affects the values which refer to the same variable
stooges[2]="Shemp"
print stooges
stuge= stooges

stuge[0]="Willy"

print stooges

spy=[0,0,7]
agent=spy

def replace_spy(l):
	l[2]=l[2]+1
	

replace_spy(spy)
print(spy)

#adding an element to a list
stooges.append("Curly")
print stooges
#adding two list (+)

print stooges + spy

#obtaining the length of a list using len
print len(stooges)

p=[1,2]
q=[3,4]

p.append(q)

print len(p)
#loops over lists
i=0
#while loop
while (i<len(stooges)):
	print stooges[i]
	i=i+1

#for loop
for i in stooges:
	print i

numbers=[0,1,2,2,2,2,3,4,5,6,7.0]

def sum_list(l):
	sum=0
	for n in l:
		sum+=n

	return sum
print sum_list(numbers)


def measure_udacity(p):
	measure=0
	for e in p:
		if (e[0])=="U":
			measure+=1
	return measure

names=["Bill","Udacity","Umiko","umikp","Larry"]
print measure_udacity(names)


def find_element(p,n):
	i=0
	while(i<len(p)):
		if p[i]==n:
			return i
		i+=1
	return -1

print find_element(stooges,"Shemp")

def find_element_index(p,t):
	if (t in p):
		return p.index(t)
	else:
		return -1
print find_element_index(stooges,"Curly")


def union(l,t):
	for e in t:
		if  e not in l:
			l.append(t)
	



		
	
print union(stooges,numbers)
