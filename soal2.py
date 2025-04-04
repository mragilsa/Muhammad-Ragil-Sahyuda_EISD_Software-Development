def soal2():
    teks = input("Masukkan kata atau kalimat: ")

    teks = teks.lower()

    teks = teks.replace(" ", "")

    reverse = teks[::-1]

    if (teks == reverse):
        return "eureeka!"
    else:
        return "suka blyat"


hasil = soal2()
print(hasil)
