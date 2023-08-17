import math
from tabulate import tabulate
degrees = 37
sine = 0
cosine = 0
deg_min = []
decimal = []
radian = []
sin = []
cos = []
table = []
table_header = ['Angle (degrees and minutes)', 'Angle (degrees as decimal)', 'Angle (Radians)', 'Angle (cosine)', 'Angle (sine)']
table.append(table_header)
# print(tabulate(table_header, headers="firstrow", tablefmt='pretty', numalign="left", floatfmt=".4f"))
for minute in range(0, 60):
    decimals = degrees + minute/60
    radians = math.radians(decimals)
    sine_deg = math.sin(radians)
    cosine_deg = math.cos(radians)
    table.append([str(degrees)+'\u00b0'+str(minute) + "'", decimals, radians, cosine_deg, sine_deg])

# print(table)
print(tabulate(table, headers="firstrow", tablefmt='fancy_grid', numalign="left", floatfmt=".4f"), "Sine, Cosine, Radians, of degrees")
