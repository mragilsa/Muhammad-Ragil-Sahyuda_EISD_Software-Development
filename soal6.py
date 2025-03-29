menu = {
    "ayam_goreng_krispi": 15000,
    "ayam_puk_puk": 13000,
    "ayam_bakar": 20000,
    "es_teh": 5000,
    "es_jeruk": 7000
}

makanan = {"ayam_goreng_krispi", "ayam_puk_puk", "ayam_bakar"}
minuman = {"es_teh", "es_jeruk"}

pajak_makanan = 0.05  
pajak_minuman = 0.03  
pajak_transaksi = 0.15  

pesanan_rehan = {"ayam_bakar": 2, "es_teh": 1}
pesanan_amba = {"ayam_puk_puk": 1, "es_teh": 3}
pesanan_faiz = {
    "ayam_goreng_krispi": 1,
    "ayam_puk_puk": 1,
    "ayam_bakar": 1,
    "es_teh": 1,
    "es_jeruk": 1
}

def hitung_total(pesanan):
    total_harga = 0

    for item, jumlah in pesanan.items():
        harga = menu[item]

        if item in makanan:
            harga += harga * pajak_makanan
        elif item in minuman:
            harga += harga * pajak_minuman

        total_harga += harga * jumlah

    total_harga += total_harga * pajak_transaksi
        
    return round(total_harga)

total_rehan = hitung_total(pesanan_rehan)
total_amba = hitung_total(pesanan_amba)
total_faiz = hitung_total(pesanan_faiz)

print(f"Total yang harus dibayar Rehan Whangsap: Rp.{total_rehan}")
print(f"Total yang harus dibayar Amba roni: Rp.{total_amba}")
print(f"Total yang harus dibayar Faiz: Rp.{total_faiz}")