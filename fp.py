# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# 1 Опоределить корни

from sympy import * 
from scipy.optimize import fsolve

x = Symbol('x')
func= '-8*x**2+3*x+17'
y=solve(func)
x1=float(y[0])
x2=float(y[1])
print(f'корни: {x1},{x2}')

# 2 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))

# 3 Найти интервалы, на которых функция убывает

print(solve(fd<0))

# 4 Построить график

import matplotlib.pyplot as plt

list_y=[]
for i in range(-5,7):
    x=i
    y=-8*x**2+3*x+17
    list_y.append(y)
print(list_y)
plt.plot(range(-5,7),[0,0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-5,7),list_y)

# 5 Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=-8*x**2+3*x+17
print(top,y)

# 6 Определить промежутки, на котором f > 0

solve(0<func)


# 7 Определить промежутки, на котором f < 0

fsolve(func<0)

