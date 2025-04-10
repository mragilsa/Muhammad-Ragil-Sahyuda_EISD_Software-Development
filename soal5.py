import math

nama = "Naip Lovyu"

nama = nama.lower()

nama = nama.replace(" ", "")

max_length = 6

def soal5():
    jumlah = 0
    n = len(nama)
    for r in range(1, max_length + 1):
        jumlah = jumlah + math.perm(n, r)
    return jumlah
    
hasil = soal5()
print(hasil)
