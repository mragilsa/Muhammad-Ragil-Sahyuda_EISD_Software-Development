tamu = ["Ningguang", "Hutao", "Xiao", "Childe"] # asumsi di soalnya itu dari bawah ke atas, sehingga paling atas adalah orang pertama yang masuk ke ruang tamu

foto_xiao = "kue masih ada"

for i in range(len(tamu)):
    if tamu[i] == "Xiao":
        tersangka = tamu[i + 1] 

print(f"Pelaku yang paling mungkin mengambil kue adalah {tersangka}!")