#İki Sayı İle İslem Yapan Hesap Makinesi
num1=float(input("Birinci Sayıyı Giriniz:"))
num2=float(input("İkinci Sayıyı Giriniz:"))
calculate=input("Yapacağınız İşlemin Türünü Seçiniz(+,-,*,/):")
if(calculate=="+"):
    print("Girilen İki Sayının Toplamı:",num1+num2)
elif(calculate=="-"):
    print("Girilen İki ayının Farkı:",num1-num2)
elif(calculate=="*"):
    print("Girilen İki Sayının Çarpımı:",num1*num2)
elif(calculate=="/"):
    print("Girilen Sayının Bolumu:",num1/num2)
else:
    print("Bilinmeyen bir veri girişi yaptınız")