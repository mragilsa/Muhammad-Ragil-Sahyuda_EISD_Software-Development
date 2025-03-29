produk = {
    "TV": "elektronik",
    "headphone": "elektronik",
    "baju": "fashion",
    "gitar": "musik",
    "sepatu": "olahraga",
    "kamera": "elektronik"
}

pelanggan = {
    "Rina": {
        "minat": ["elektronik", "musik"],
        "beli": ["TV", "headphone"]
    },

    "Budi": {
        "minat": ["fashion", "musik"],
        "beli": ["baju", "gitar"]
    },

    "Hartono": {
        "minat": ["olahraga", "elektronik"],
        "beli": ["sepatu", "kamera"]
    }
}

def rekomendasi(nama_pelanggan):
    if nama_pelanggan not in pelanggan:
        return []
    
    data_pelanggan = pelanggan[nama_pelanggan]
    minat_pelanggan = data_pelanggan["minat"]
    produk_dibeli = data_pelanggan["beli"]

    rekomendasi_produk = set(produk_dibeli)

    for nama_produk, kategori_produk in produk.items():
        if kategori_produk in minat_pelanggan and nama_produk not in produk_dibeli:
            rekomendasi_produk.add(nama_produk)

    return rekomendasi_produk

print("Rekomendasi untuk Rina:", rekomendasi("Rina"))
print("Rekomendasi untuk Budi:", rekomendasi("Budi"))
print("Rekomendasi untuk Hartono:", rekomendasi("Hartono"))
