### Correction DS01 - sujet A
print('CORRECTION DS01 - sujet A')
print('-----------------------------')
print('Exercice 2')
x = 3
rep = x**2 == 6
print(rep)

x , y , z = 3 , 4 , 5
rep = x**2 + y**2 == z**2
print(rep)

a , b = 3 , 7
rep = a**2>50 and b**2 < 50
print(rep)

a , b = 3 , 7
rep = (a**2>50 and b**2 < 50) or (a**2 < 10 and b**2 > 10)
print(rep)

print('-----------------------------')
print('Exercice 3')
def f(x,y):
	assert x!=0 , "La première valeur doit être non nulle"
	x = x + y
	y = x - y
	x = x - y
	return x
# print(f(0,3))
print(f(7,3))

def g(a,b):
	''' a et b sont deux entiers naturels '''
	c = (a > b)
	d = (c == False)
	return (c,d)

print(g(5,2))
print(g(2,5))


print('-----------------------------')
print('Exercice 4')

def h(a,b):
	''' a et b sont deux entiers naturels '''
	if a > b:
		return 'a'
	else:
		return b

print(h(4,5))
print(h(6,4))


### Correction DS01 - sujet B
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('CORRECTION DS01 - sujet B')
print('-----------------------------')
print('Exercice 2')
x = 3
rep = x**2 == 9
print(rep)

x , y , z = 3 , 4 , 5
rep = x**2 + y**2 == z**2
print(rep)

a , b = 3 , 7
rep = a**2>50 or b**2 < 50
print(rep)

a , b = 3 , 7
rep = (a**2>50 or b**2 < 50) and (a**2 < 10 or b**2 > 10)
print(rep)

print('-----------------------------')
print('Exercice 3')
def f(x,y):
	assert x!=0 , "La première valeur doit être non nulle"
	x = x + y
	y = x - y
	x = x - y
	return x
# print(f(0,3))
print(f(3,7))

def g(a,b):
	''' a et b sont deux entiers naturels '''
	c = (a > b)
	d = (c == False)
	return (c,d)

print(g(2,6))
print(g(6,2))

print('-----------------------------')
print('Exercice 4')
def h(a,b):
	''' a et b sont deux entiers naturels '''
	if a > b:
		return a
	else:
		return 'b'

print(h(4,5))
print(h(6,4))