#Sınav Notu Hesaplama
vize=float(input("Vize Notunu Giriniz"))
final=float(input("Final Notunu Giriniz"))
average= vize*0.4 + final*0.6
durum=""
if average>=70:
    durum="Sınavdan Geçtiniz"
else:
    durum="Sınavdan Kaldınız"
    
print("Geçme Notu:{0} ".format(average))
print("Geçme Durumunuz{0}: ".format(durum))