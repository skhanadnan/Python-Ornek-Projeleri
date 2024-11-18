#Program içerisnde istenen bir şartın gerçekleşmesi durumunda yerine getirilecek kod blokları if bloklarıdır.
sayi=int(input("Bir Sayi Girin"))
if sayi<1:
    print("Sayı 1'den küçük")
    
num=int(input("Bir sayı giriniz"))
if num<0:
    print("Negatif Sayı")
elif num>0:
    print("Pozitif Sayı")
else:
    print("Sıfır")
    
num1=int(input("Birinci Sayı Giriniz:"))
num2=int(input("İkinci Sayı Giriniz:"))
if num1<0 and num2<0:
    print("İkiside Negatif Sayı")
elif num1>0 and num2>0:
    print("İkiside Pozitif Sayı")
else:
    print("Diğer durumlar var")