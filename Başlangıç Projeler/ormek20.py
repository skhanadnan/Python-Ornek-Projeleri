#Kullanıcıdan Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma

dizi=list()
print("Çıkış için Q harfine basınız. Aksi Halde sayı girmeye devam ediniz.")
while True:
    sayi=(input("Bir Sayı Giriniz:"))
    if sayi.upper()=="Q":
        break
    sayi=int(sayi)
    durum=""
    if sayi%2==0:
        durum="Çift"
    else:
        durum="Tek"
        dizi.append(str(sayi)+" "+durum)
        print(*dizi,sep="\n")