#METİNDEKİ İLK KELİME İLE SON KELİMEYİ BULMA
metin=input("Bir İfade Giriniz:")
ilkKonum=metin.index(" ")
sonKonum=metin.rindex(" ")
ilkKelime=metin[0:ilkKonum]
sonKelime=metin[sonKonum:len(metin)]
print("İlk Kelime:"+ilkKelime)
print("Son Kelime:"+sonKelime)