import math

print('WELCOME TO MY JOIN PROGRAM')
print('STARTING POINT \n\n Input Y-Coordinate')

coord_a_y = float(input())
print('Input X-Coordinate')
coord_a_x = float(input())
print('Moving on to the second point\n\nInput Y-Coordinate')
coord_b_y = float(input())
print('Input X-Coordinate')
coord_b_x = float(input())

dif_y = coord_b_y - coord_a_y
dif_x = coord_b_x - coord_a_x

distance = math.sqrt((pow(dif_x, 2) + pow(dif_y, 2)))
print("***********RESULT**************\n\nDistance => " + str(distance))

# finding the angle now
rad_theta = math.atan(dif_y / dif_x)

# declaring a constant rad value to convert from radians to degrees
rad_constant = 180 / math.pi

# conditions to find quadrants

# second quadrant
if dif_x < 0 < dif_y:
    quadrant = 180

# third quadrant
elif dif_x < 0 and dif_y < 0:
    quadrant = 180

# fourth quadrant
elif dif_x > 0 > dif_y:
    quadrant = 360

# when neither condition is met and its first quadrant
else:
    quadrant = 0

# calculating the angle
angle = (rad_theta * rad_constant) + quadrant
degree = int(angle)
minutes_float = (angle - degree) * 60
minutes = int(minutes_float)
seconds = math.floor((minutes_float - minutes) * 60)

# the angle in DMS format
print("Angle => " + str(degree) + "°" + str(minutes) + "`" + str(seconds) + "``")
