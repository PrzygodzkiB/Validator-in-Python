# Bartłomiej Przygodzki 299214
# Projekt 1 JFK

from scanner import *
from parser2 import *

# input_string = """
# begin
# v = voltagesource(1.0)
# u = voltagesource()
# r = resistor(1400)
# c = capacitor(5e-12)
# l = inductor(0.000001)
# j_in = voltagesource()
# r1 = resistor(1e3)
# c1 = capacitor(47e-9)
# d1 = diode(is=1e-15)
# d2 = diode(is=1.8e-15, eta=2)
# j_out = voltageprobe()
# R1 = resistor(13.2)
# C1 = capacitor(100e-9)
# VIN = voltagesource()
# AM1 = currentprobe()
#
# u[2] -- r[1]
# r[2] -- l[1]
# l[2] -- c[1]
# c[2] -- v[1]
# v[2] -- u[1] -- gnd
# j_in[2] -- r1[1]
# j_in[1] -- gnd
# r1[2] -- c1[1] -- d1[2] -- d2[1] -- j_out[2]
# gnd -- c1[2] -- d1[1] -- d2[2] -- j_out[1]
# VIN[2] -- R1[1]
# R1[2] -- C1[1]
# C1[2] -- AM1[1]
# AM1[2] -- VIN[1]
# VIN[1] -- gnd
# end
# """

input_string = """

begin
v = voltagesource(1.0)
u = voltagesource()
r = resistor(1400)
c = capacitor(5e-12)
l = inductor(0.000001)
j_in = voltagesource()
r1 = resistor(1e3)
c1 = capacitor(47e-9)
d1 = diode(is=1e-15)
d2 = diode(is=1.8e-15, eta=2)
j_out = voltageprobe()
R1 = resistor(13.2)
C1 = capacitor(100e-9)
VIN = voltagesource()
AM1 = currentprobe()

u[2] -- r[1]
r[2] -- l[1]
l[2] -- c[1]
c[2] -- v[1]
v[2] -- u[1] -- gnd
j_in[2] -- r1[1]
j_in[1] -- gnd
r1[2] -- c1[1] -- d1[2] -- d2[1] -- j_out[2]
gnd -- c1[2] -- d1[1] -- d2[2] -- j_out[1]
VIN[2] -- R1[1]
R1[2] -- C1[1]
C1[2] -- AM1[1]
AM1[2] -- VIN[1]
VIN[1] -- gnd
end

"""

print(input_string)
scanner = Scanner(input_string)
print(scanner.tokens)

parser = Parser2(scanner)
parser.program()
  
