from z3 import *

periodic_table = [
    "",        # 0
    "H",       # 1
    "He",      # 2
    "Li",      # 3
    "Be",      # 4
    "B",       # 5
    "C",       # 6
    "N",       # 7
    "O",       # 8
    "F",       # 9
    "Ne",      # 10
    "Na",      # 11
    "Mg",      # 12
    "Al",      # 13
    "Si",      # 14
    "P",       # 15
    "S",       # 16
    "Cl",      # 17
    "Ar",      # 18
    "K",       # 19
    "Ca",      # 20
    "Sc",      # 21
    "Ti",      # 22
    "V",       # 23
    "Cr",      # 24
    "Mn",      # 25
    "Fe",      # 26
    "Co",      # 27
    "Ni",      # 28
    "Cu",      # 29
    "Zn",      # 30
    "Ga",      # 31
    "Ge",      # 32
    "As",      # 33
    "Se",      # 34
    "Br",      # 35
    "Kr",      # 36
    "Rb",      # 37
    "Sr",      # 38
    "Y",       # 39
    "Zr",      # 40
    "Nb",      # 41
    "Mo",      # 42
    "Tc",      # 43
    "Ru",      # 44
    "Rh",      # 45
    "Pd",      # 46
    "Ag",      # 47
    "Cd",      # 48
    "In",      # 49
    "Sn",      # 50
    "Sb",      # 51
    "Te",      # 52
    "I",       # 53
    "Xe",      # 54
    "Cs",      # 55
    "Ba",      # 56
    "La",      # 57
    "Ce",      # 58
    "Pr",      # 59
    "Nd",      # 60
    "Pm",      # 61
    "Sm",      # 62
    "Eu",      # 63
    "Gd",      # 64
    "Tb",      # 65
    "Dy",      # 66
    "Ho",      # 67
    "Er",      # 68
    "Tm",      # 69
    "Yb",      # 70
    "Lu",      # 71
    "Hf",      # 72
    "Ta",      # 73
    "W",       # 74
    "Re",      # 75
    "Os",      # 76
    "Ir",      # 77
    "Pt",      # 78
    "Au",      # 79
    "Hg",      # 80
    "Tl",      # 81
    "Pb",      # 82
    "Bi",      # 83
    "Po",      # 84
    "At",      # 85
    "Rn",      # 86
    "Fr",      # 87
    "Ra",      # 88
    "Ac",      # 89
    "Th",      # 90
    "Pa",      # 91
    "U",       # 92
    "Np",      # 93
    "Pu",      # 94
    "Am",      # 95
    "Cm",      # 96
    "Bk",      # 97
    "Cf",      # 98
    "Es",      # 99
    "Fm",      # 100
    "Md",      # 101
    "No",      # 102
    "Lr",      # 103
    "Rf",      # 104
    "Db",      # 105
    "Sg",      # 106
    "Bh",      # 107
    "Hs",      # 108
    "Mt",      # 109
    "Ds",      # 110
    "Rg",      # 111
    "Cn",      # 112
    "Nh",      # 113
    "Fl",      # 114
    "Mc",      # 115
    "Lv",      # 116
    "Ts",      # 117
    "Og"       # 118
]

import random

# one
print("One:")
print(f"a = {periodic_table[80]}")


# two
solver = Solver()
a = Int('a')
b = Int('b')
solver.add(a**2 + b == 12608)
solver.add(a <= 118)
solver.add(a > 0)
solver.add(b <= 118)
solver.add(b > 0)

if solver.check() == sat:
  model = solver.model()
  print("Two:")
  print(f"a = {periodic_table[model[a].as_long()]}")
  print(f"b = {periodic_table[model[b].as_long()]}")
  

# three
solver = Solver()
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r = Ints('a b c d e f g h i j k l m n o p q r')
equations = [
    d**2 + n**3 + r**2 + j == 864110,
    k + p == 172,
    d + f == 122,
    e == 54,
    b + h**2 == 9525,
    q**3 + p == 857430,
    g == 57,
    h + o + q == 300,
    l + a == 141,
    m + c + e**2 == 3074,
    i == 55,
    j**3 + e == 1295083,
    r == 49,
    n == 95,
    e + q == 149,
    m + q == 152,
    k + a == 163,
    o == 108,
    b == 116,
    i + h == 152,
    m + k == 174
]
solver.add(a <= 118)
solver.add(a > 0)
solver.add(b <= 118)
solver.add(b > 0)
solver.add(c <= 118)
solver.add(c > 0)
solver.add(d <= 118)
solver.add(d > 0)
solver.add(e <= 118)
solver.add(e > 0)
solver.add(f <= 118)
solver.add(f > 0)
solver.add(g <= 118)
solver.add(g > 0)
solver.add(h <= 118)
solver.add(h > 0)
solver.add(i <= 118)
solver.add(i > 0)
solver.add(j <= 118)
solver.add(j > 0)
solver.add(k <= 118)
solver.add(k > 0)
solver.add(l <= 118)
solver.add(l > 0)
solver.add(m <= 118)
solver.add(m > 0)
solver.add(n <= 118)
solver.add(n > 0)
solver.add(o <= 118)
solver.add(o > 0)
solver.add(p <= 118)
solver.add(p > 0)
solver.add(q <= 118)
solver.add(q > 0)
solver.add(r <= 118)
solver.add(r > 0)

for equation in equations:
    solver.add(equation)

if solver.check() == sat:
  model = solver.model()
  print("Three:")
  for var in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r]:
    print(f"{var}: {periodic_table[model[var].as_long()]}")