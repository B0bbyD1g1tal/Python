# Metric Converter

MILLIMETER = 1000
CENTIMETER = 100
METER = 1
KILOMETER = 0.001

INCH = 39.3700787
FEET = 3.2808399
YARD = 1.0936133
MILE = 0.000621371192

value = float(input())
input_units = input()
output_units = input()

# Calculate value in meters
metric_units = value
if input_units == 'mm':
    metric_units /= MILLIMETER
elif input_units == 'cm':
    metric_units /= CENTIMETER
elif input_units == 'm':
    metric_units /= METER
elif input_units == 'km':
    metric_units /= KILOMETER
elif input_units == 'in':
    metric_units /= INCH
elif input_units == 'ft':
    metric_units /= FEET
elif input_units == 'yd':
    metric_units /= YARD
elif input_units == 'mi':
    metric_units /= MILE

# Calculate from meters to the given units
if output_units == 'mm':
    metric_units *= MILLIMETER
elif output_units == 'cm':
    metric_units *= CENTIMETER
elif output_units == 'm':
    metric_units *= METER
elif output_units == 'km':
    metric_units *= KILOMETER
elif output_units == 'in':
    metric_units *= INCH
elif output_units == 'ft':
    metric_units *= FEET
elif output_units == 'yd':
    metric_units *= YARD
elif output_units == 'mi':
    metric_units *= MILE

result = f'{metric_units:.3f}'

print(result)
