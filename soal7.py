def dekripsi(teks):
    hasil = ""

    for huruf in teks:
        if huruf.isalpha():
            kode_ascii = ord(huruf)
            kode_ascii_baru = kode_ascii - 5
            huruf_baru = chr(kode_ascii_baru)
            hasil += huruf_baru
        else:
            hasil += huruf
    return hasil

chat1 = "xfqfr bfmdz"
chat2 = "gjxtp lzj rfz ifkyfw jxi snm"
chat3 = "gwt, gjxtp qz rfz rfpfs in bfwlty lfp?"
chat4 = "fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz"
chat5 = "ddfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"

print(dekripsi(chat1))
print(dekripsi(chat2))
print(dekripsi(chat3))
print(dekripsi(chat4))
print(dekripsi(chat5))