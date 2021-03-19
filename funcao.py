import numpy as np 

def med(n):
	s = i = 0
	for c in range(len(n)):
		s += n[c]
		i += 1
	return s/float(i)

def desP(n):
	from math import sqrt as raiz
	s = i = 0
	for c in range(len(n)):
		s += ((n[c]-med(n))**2)
		i += 1
	return raiz(s/i)

def quedaL(n):
	from math import sqrt as raiz
	return raiz((2*n)/9.81)

def abra(a):
    with open(a,'r') as arq1:
        ler = arq1.read()
        sepa = ler.split('\n')
        l1 = []
        for c in sepa:
            l1.append(float(c))

    m = np.array(l1)
    mm = med(m)
    dm = desP(m)
    return mm, dm

def addd(a,b,c):
	with open('arq_f.txt','a') as arqf:
		arqf.write(f'\n{a[0:3]} {b:.4f} {c:.4f}')

def adt(a,b,c):
	b = abra(a)
	c = addd(a[0:3],b[0],b[1])

a = "1.0m.txt"
r1 = abra(a)
with open('arq_f.txt','w') as arqf:
	arqf.write(f'1.00 {r1[0]:.4f} {r1[1]:.4f}')

b = "1.3m.txt"
b1 = b2 = 0
r2 = adt(b,b1,b2)

c = "1.6m.txt"
c1 = c2 = 0
r3 = adt(c,c1,c2)

d = "1.9m.txt"
d1 = d2 = 0
r4 = adt(d,d1,d2)

e = "2.2m.txt"
e1 = e2 = 0
r5 = adt(e,e1,e2)

with open("arq_f.txt") as arquivo:
    ler = arquivo.read()
    sepa = ler.split('\n')
    li2 = []
    for c in range(len(sepa)):
        sepa2 = sepa[c].split(' ')
        li2.append(sepa2)
    li = []
    for c in range(len(li2)):
        for j in range(3):
            li.append(float(li2[c][j]))