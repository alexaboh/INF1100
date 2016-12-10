from math import pi
g = 9.81 #m/s2, acceleration of gravity
rho = 1.2 #kg/m3, density of air
a = 0.11 #m, radius of ball, here football(11cm)
A = pi*a**2 #m2, area of ball
m = 0.43 #kg, mass of ball
Cd = 0.2 #drag coefficient
V = [120.0*1/3.6, 10.0*1/3.6]#m/s, list with the two velocities

Fg = m*g #kg m/s2, gravity force on object
Fd = []  #kg m/s2, drag force

print "The gravity force is: %.1f N" % Fg

#Calculating drag force in loop going through both velocities. 
for i in range(0, len(V)):
    Fd.insert(i,(1/2.0)*Cd*rho*A*V[i]**2)
    print "\nThe drag force, when velocity is %.1f m/s, is: %.1f N, and the ratio of the drag force and the gravity force is %.1f" % (V[i], Fd[i], Fd[i]/Fg)

    
"""-----------------------------------
Terminal:

The gravity force is: 4.2 N

The drag force, when velocity is 33.3 m/s, is: 5.1 N, and the ratio of the drag force and the gravity force is 1.2

The drag force, when velocity is 2.8 m/s, is: 0.0 N, and the ratio of the drag force and the gravity force is 0.0
"""
