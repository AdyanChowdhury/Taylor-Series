
import math
degree = int(input("Put in a degree to convert: "))
minutes = int(input("Put in a minute to convert: "))
seconds = int(input("Put in a second to convert: "))
# minute = minute/60
angle_convert = degree + minutes/60 + seconds/3600
radian_convert = angle_convert * (math.pi/180)
print(str(degree)+ '\u00b0', str(minutes), "'", float(seconds), '"' "is", + round(radian_convert, 4))
