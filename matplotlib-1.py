'''
from matplotlib import pyplot as plt

plt.plot([1,2,3],[4,5,1])

plt.show()
'''


#now lets do this with title and axis names
'''
from matplotlib import pyplot as plt

x = [5,6,7]
y = [12,16,7]

plt.plot(x,y)

plt.title("Info")
plt.xlabel("Xaxis")
plt.ylabel("Yaxis")

plt.show()
'''

#lets do a colored graph with legend and grid with color
'''
from matplotlib import pyplot as plt

from matplotlib import style

style.use("ggplot")

x = [5,8,10]
y = [12,16,6]

x1 = [6,9,11]
y1 = [6,15,7]

plt.plot(x,y,'g', label = 'lineone', linewidth = 5)
plt.plot(x1,y1,'c', label = 'linetwo', linewidth = 5)

plt.title("info")
plt.xlabel("Xaxis")
plt.ylabel("Yaxis")

plt.legend()

plt.grid(True, color = 'K')

plt.show()
'''

#lets plot a bar graph
'''
from matplotlib import pyplot as plt

plt.bar([1,2,3,4,5,6,7],[5,8,3,4,9,1,7], label="Example one")

plt.bar([5,6,7,8,9,3,2],[7,4,5,7,6,9,2], label="Example two", color='g')

plt.legend()

plt.title('bar graph')
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.show()
'''

#lets plot a histogram graph
'''
from matplotlib import pyplot as plt

population_ages = [22,45,77,33,54,34,32,21,23,54,57,34,98,124,67,102,45,67,12,87,99,43]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.title('Histogram')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
'''

#lets do a scatter plot
'''
from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [5,7,8,9,2,3,4,5,1]

plt.scatter(x,y, label='this is scatter bro', color='k')

plt.title('scatter plot')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
'''

#lets do a area plot / stack plot
'''
from matplotlib import pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,9]
eating = [2,3,4,3,2]
working = [7,8,9,5,3]
playing = [8,5,7,4,9]

plt.plot([],[], color='m', label='sleeping', linewidth=5)
plt.plot([],[], color='c', label='eating', linewidth=5)
plt.plot([],[], color='r', label='working', linewidth=5)
plt.plot([],[], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.title('Area Plot / Stack Plot')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
'''

#lets do a pie plot
'''
from matplotlib import pyplot as plt

slices = [7,2,5,13]

activities = ["sleeping", "eating", "working", "playing"]
cols = ['c','r','g','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%' #shows the percentage of the pie
        )

plt.title('pie plot')

plt.show()
'''

#lets do a multiple plot
'''
import numpy as np
from matplotlib import pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211) #subplot with 2 plots 1 in horizintal and 1 in vertical
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212) #subplot with 2 plots 1 in horizontal and 2 in vertical
plt.plot(t2, np.cos(2 * np.pi * t2))

plt.show()
'''

