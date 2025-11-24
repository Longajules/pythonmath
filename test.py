from pylab import *

for i in range (3,14):
    y=[3]
    x=[2+i]
    plot (x,y,'*g')

xlim(0,20)
ylim(2,4)
show()
