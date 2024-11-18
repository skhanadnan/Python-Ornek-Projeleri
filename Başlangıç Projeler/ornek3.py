#Girilen Sayının tek veya çift olduğunu belirleme
sayi=int(input("Bir Sayı Giriniz:"))
sonuc=""

if(sayi&2==0):
    sonuc="Girilen Sayı Çift"
else:
    sonuc="Girilen Sayı Tek"

print(sonuc)