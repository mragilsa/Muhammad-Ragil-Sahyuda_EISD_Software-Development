nama = "Naip Lovyu"

nama = nama.lower()

nama = nama.replace(" ", "")

max_length = 6

def hitung_kombinasi(nama, max_length):
    jumlah = 0
    panjang_nama = len(nama)

    for panjang in range(1, max_length + 1):
        kombinasi = 1
        for i in range(panjang):
            kombinasi = kombinasi * (panjang_nama - i)
        jumlah += kombinasi
    return jumlah

hasil = hitung_kombinasi(nama, max_length)
print(hasil)