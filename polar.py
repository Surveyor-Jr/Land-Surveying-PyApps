import math
import re

def dms2dd(bearing):
    dd = float(bearing[0]) + float(bearing[1])/60 + float(bearing[2])/(60*60);
    return dd; 

print('*************POLAR***************')
print('Enter Coordinates of occupation Station \n\n Y-coordinate :')

# Y-coordinate of the station
y_initial = float(input())

# X-coordinate of the station
print('X-coordinate :')
x_initial = float(input())

# Distance to the target
print('Distance to target :')
distance = float(input())

# -->Bearing to target
print('Bearing to Target (use (*) as your separator in DMS format :')
# -->take input in DMS format while separated with an asterik (*)
bearing = tuple(int(x.strip()) for x in input().split('*'))
# -->call the dms2dd function
direction = dms2dd(bearing)

# -->calculating coordinates of target
rad_constant = 180 / math.pi
dir_deg = rad_constant * direction
y_target = y_initial + distance * math.sin(dir_deg)

# testing
print('Y-Coordinate of Target :')
print(y_target)
print('Bearing of')
print(direction)



