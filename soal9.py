def cari_anak_nakal(laporan):
    jumlah_sebutan = {}

    for nama in laporan:
        if nama in jumlah_sebutan:
            jumlah_sebutan[nama] = jumlah_sebutan[nama] + 1
        else:
            jumlah_sebutan[nama] = 1
        
    maks = 0
    for jumlah in jumlah_sebutan.values():
        if jumlah > maks:
            maks = jumlah
        

    nakal_terbanyak = []
    for nama, jumlah in jumlah_sebutan.items():
        if jumlah == maks:
            nakal_terbanyak.append(nama)
    

    if maks == 1:
        print("Semuanya anak baik")
    elif len(nakal_terbanyak) == 1:
        print(nakal_terbanyak[0], "Nackal")
    else:
        print(" dan ".join(nakal_terbanyak), "Nackal")

laporan1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
laporan2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
laporan3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]

print("Input 1:")
cari_anak_nakal(laporan1)  

print("\nInput 2:")
cari_anak_nakal(laporan2) 

print("\nInput 3:")
cari_anak_nakal(laporan3)  