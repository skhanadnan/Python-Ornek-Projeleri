#Metindeki Sesli Harf Sayısını Hesaplama
metin=input("Metin Giriniz:")
metin=metin.lower()
sesliharfler="aeıioöuü"
sayac=0
for i in metin:
    for j in sesliharfler:
        if i==j:
            sayac +=1
            print("Metindeki sesli harf sayısı:",(metin,sayac))