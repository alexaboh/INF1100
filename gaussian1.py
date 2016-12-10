#Importing the necessary math function. 
from math import pi, exp, sqrt

#Variables as defined in exercise.
m = 0.0
s = 2.0
x = 1.0

#The gaussian function as defined in exercise. 
f = 1/(sqrt(2*pi)*s)*exp(-(1/2.0)*((x-m)/s)**2) 
print f

"""Terminal: 0.176032663382"""

