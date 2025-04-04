def cek_duplikat(input_angka):
    data = list(map(float, input_angka.split(",")))  
    angka_cek = []  

    for angka in data:
        if angka in angka_cek:
            return True  
        angka_cek.append(angka)  

    return False 

input_angka = input("Masukkan angka (pisahkan dengan koma): ")
hasil = cek_duplikat(input_angka)
print(hasil)
