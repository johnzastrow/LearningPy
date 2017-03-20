# LSI = pH - pHs

# Where:
# pH is the measured water pH
# pHs is the pH at saturation in calcite or calcium carbonate and is defined as:

# pHs = (9.3 + A + B) - (C + D)

# Where:
# A = (Log10 [TDS] - 1) / 10
# B = -13.12 x Log10 (deg C + 273) + 34.55
# C = Log10 [Ca2+ as CaCO3] - 0.4
# D = Log10 [alkalinity as CaCO3]

# The indications for the LSI and the improved LSI by Carrier are based on the following values:

# LSI	Indication
# LSI<0	Water is undersaturated with respect to calcium carbonate. Undersaturated water has a tendency to remove existing calcium carbonate protective coatings in pipelines and equipment.
# LSI=0	Water is considered to be neutral. Neither scale-forming nor scale removing.
# LSI>0	Water is supersaturated with respect to calcium carbonate (CaCO3) and scale forming may occur.


# LSI (Carrier)	Indication
# -2,0<-0,5	Serious corrosion
# -0,5<0	Slightly corrosion but non-scale forming
# LSI = 0,0	Balanced but pitting corrosion possible
# 0,0<0,5	Sligthly scale forming and corrosive
# 0,5<2	Scale forming but non corrosive

# Read more: http://www.lenntech.com/calculators/langelier/index/langelier.htm#ixzz4bbswoh9P


import math  # This will import math module
import platform
import os

# clear the terminal either in windows or *nix
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

myos = platform.system()

print('Hey, you appear to be running: ', myos)
print()

# Simple F to C converter. It works!
Celsius = input("Enter a temperature in Celsius: ")
Fahrenheit = 9.0 / 5.0 * float(Celsius) + 32
print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
# the reverse calc
revc = (Fahrenheit - 32) * 5.0 / 9.0
print('and the check. here is Deg C back: ', revc)

print(
    'The following program developed from \n http://www.corrosion-doctors.org/Cooling-Water-Towers/Index-Lang-calcul'
    '.htm ')
print('Enter values for the following inputs')
print('------------------')
# easy space
print()
# command line input with a default value. Must convert input to number, here a float
temp = float(input('Enter Temperature in Deg F [77]: ') or 77)
tds = float(input('Enter TDS in mg/l [320]: ') or 320)
ca = float(input('Enter Ca2+ in mg/l [150]: ') or 150)
pH = float(input('Enter pH [7.5]: ') or 7.5)
alk = float(input('Enter Alkalinity as CaCO3 [34]: ') or 34)

# convert F to C
degc = ((temp) - 32) * 5.0 / 9.0
# compute the TDS index
A = (math.log10(tds) - 1) / 10
print('TDS = ', tds, ' --> The TDS index is: ', A)

# compute the temperature index
B = -13.12 * (math.log10(degc + 273)) + 34.55
print('Deg C = ', degc, ' --> The temp index is: ', B)

# compute the hardness index
C = math.log10(ca) - 0.4
print('Calcium Hardness = ', ca, ' --> The hardness index is: ', C)

# compute the alkalinity index
D = math.log10(alk)
print('Alklinity = ', alk, ' --> The alkalinity index is: ', D)

# compute the pHs
pHs = (9.3 + A + B) - (C + D)
print('pHs = ', pHs)

# compute the LSI
LSI = pH - pHs
print('LSI = ', LSI)

# Now we interpret the results for the user

print()

if LSI <= -0.5:
    print(
        'Serious corrosion. Water is undersaturated with respect to calcium carbonate. Undersaturated water has a '
        'tendency to remove existing calcium carbonate protective coatings in pipelines and equipment.')
elif -0.499 <= LSI < 0:
    print(
        'Slightly corrosive, but non-scale forming. Water is undersaturated with respect to calcium carbonate. '
        'Undersaturated water has a tendency to remove existing calcium carbonate protective coatings in pipelines '
        'and equipment.')
elif LSI == 0:
    print(
        'Balanced but pitting corrosion possible. Water is considered to be neutral. Neither scale-forming nor scale removing.')
elif -.0001 <= LSI < 0.5:
    print(
        'Slightly scale forming. Water is supersaturated with respect to calcium carbonate (CaCO3) and scale forming may occur.')
else:
    print(
        'Scale forming, but non-corrosive. Water is supersaturated with respect to calcium carbonate (CaCO3) and scale forming may occur.')
print()
print('Done!')

