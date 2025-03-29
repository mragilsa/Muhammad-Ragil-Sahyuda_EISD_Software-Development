pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

total_pembayaran = int(input("Masukkan total pembayaran: "))
total_belanja = int(input("Masukkan total belanja: "))

kembalian = total_pembayaran - total_belanja

if kembalian == 0:
    print("Tidak ada kembalian")
else:
    print("Kembalian:")

for uang in pecahan:
    if kembalian >= uang:
        jumlah = kembalian // uang  
        print(f"{uang}: {jumlah}")  
        kembalian = kembalian % uang  