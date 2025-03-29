input_angka = input("Masukkan angka (pisahkan dengan koma): ")

data = []
for x in input_angka.split(","):
    data.append(int(x)) 

angka_cek = []

for angka in data:
    if angka in angka_cek:  
        print("True")
        break  
    else:
        angka_cek.append(angka) 

else:
    print("False")