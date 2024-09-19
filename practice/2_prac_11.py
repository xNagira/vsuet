import math
x=6.251
y=0.827
z=25.001

s=y**((abs(x))**1/3)+(math.cos(y)**3)*((abs(x-y)*(1+((math.sin(z)**2)/((x+y)**0.5))))/(math.exp(abs(x-y))+(x/2)))
print(s)