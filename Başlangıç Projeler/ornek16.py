#Sayı Değerlerin Toplamını Hesaplama
toplam=0
sayi=input("Sayıyı Giriniz:")
if sayi.isnumeric==False:
    print("Lütfen Sadece Sayı Giriniz.")
else:
    for i in sayi:
        toplam +=int(i)
        print(sayi+ " Sayısının Sayı Değerlerinin Toplamı: "+str(toplam))