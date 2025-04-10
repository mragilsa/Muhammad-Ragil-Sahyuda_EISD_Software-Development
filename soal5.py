nama = "Naip Lovyu"

nama = nama.lower()

nama = nama.replace(" ", "")

max_length = 6

def hitung_kombinasi(nama, max_length):
    jumlah = 0
    n = len(nama)
    for r in range(1, max_length + 1):
        jumlah += math.perm(n, r)
    return jumlah

hasil = hitung_kombinasi(nama, max_length)
print(hasil)
