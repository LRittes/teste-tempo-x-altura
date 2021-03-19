from funcao import*
import matplotlib.pylab as mpl
import numpy as np

n1 = np.array(li[1::3])
y1 = np.array(li[2::3])
x = np.linspace(0.9,2.5,100)
y = np.zeros(100)

for c in range(100):
    y[c] = quedaL(x[c])
    
mpl.plot(x,y)
p = 1
for c in range(5):
    mpl.plot(p,n1[c],"o")
    mpl.errorbar(p,n1[c], yerr = y1[c], fmt = 'o', capsize = 5)
    p += 0.3
mpl.ylabel('Tempo (s)', fontsize = 18)
mpl.xlabel('Altura (m)', fontsize = 18)
mpl.show()