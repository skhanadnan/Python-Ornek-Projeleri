#fonksiyonlar ile Hesap Makinesi Yapımı
def topla(x,y):
    return x+y
def cikar(x,y):
    return x-y
def carp(x,y):
    return x*y
def bol(x,y):
    return x/y
def modalma(x,y):
    return x%y

print("-----Hesap Makinesi------")

while True:
        num1=int(input("Birinci Sayı Giriniz:"))
        num2=int(input("İkinci Sayı Giriniz:"))
        islem=input("Yapacağınız işlem türünü seçiniz (+,-,*,/,%):")
        if(islem=="+"):
            print("Girilen iki sayının toplamı:",(topla(num1,num2)))
        elif(islem=="-"):
            print("Girilen İki Sayının Farkı:",cikar(num1,num2))
        elif(islem=="*"):
            print("Girilen İki Sayının Carpimi:",carp(num1,num2))
        elif(islem=="/"):
            print("Girilen İki Sayının Bölümü:",bol(num1,num2))
        elif(islem=="%"):
            print("Girilen iki sayının bolumunden kalan:",modalma(num1,num2))
        elif(islem==""):
            print("Çıkış Yapılıyor...")
            break
    
        