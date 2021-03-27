# Membuat Program menghitung luas lingkaran di Python

# Rumus Keliling Dan Lingkaran
# Luas = phi x r x r

# Keliling = 2 x r x r

import math

r = float(input("Masukkan Jari-Jari : "))

luas = math.pi*(r*r)
keliling = 2*math.pi*r

# fungsi format, bisa membuat format menjadi 2 desimal atau 3 desimal
# tergantung kebutuhan

print("Luas Lingkaran =  ", format(luas, '.4f'))
print("Keliling Lingkaran =", format(keliling,'.4f'))