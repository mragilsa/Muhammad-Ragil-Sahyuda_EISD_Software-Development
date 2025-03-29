teks = input("Masukkan kata atau kalimat: ")

teks = teks.lower()

teks = teks.replace(" ", "")

reverse = teks[::-1]

if (teks == reverse):
    print("eureeka!")
else:
    print("suka blyat")