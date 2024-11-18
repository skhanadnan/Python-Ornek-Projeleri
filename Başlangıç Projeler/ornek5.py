#Hesap Makinesi
while True:
    s1=float(input("Birinci Sayıyı Giriniz:"))
    s2=float(input("İkinci Sayıyı Giriniz:"))
    tur=input("Yapmak İstediğniz İşlemi Seçiniz:(+,-,*,/):")
    if(tur=="+"):
        print("İki Sayının Toplamı:",s1+s2)
    elif(tur=="-"):
        print("İki Sayının Farkı:",s1-s2)
    elif(tur=="*"):
        print("İki Sayının çarpımı:",s1*s2)
    elif(tur=="/"):
        print("İki Sayının Bolumu:",s1/s2)
    else:
       print("Geçersiz Bir İşlem Yaptınız")
       break
    
    
     