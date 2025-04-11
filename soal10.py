pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

total_pembayaran = int(input("Masukkan Total Pembayaran: "))
total_belanja = int(input("Masukkan Total Belanja: "))

kembalian = total_pembayaran - total_belanja
hasil_kembalian = {}

if kembalian == 0:
    print("Tidak ada kembalian (uang sudah pas)")
else:
    for uang in pecahan:
        if kembalian >= uang:
            jumlah = kembalian // uang
            hasil_kembalian[str(uang)] = jumlah
            kembalian = kembalian % uang

print("Kembalian:")
print(hasil_kembalian)
