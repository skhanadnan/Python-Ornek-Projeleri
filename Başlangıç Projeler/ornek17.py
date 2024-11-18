#Fonksiyonlar ile Hesap Makinesi yapımı

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

while True:
    num1=int(input("Lütfen birinci sayıyı giriniz:"))
    num2=int(input("Lütfen ikinci sayıyı giriniz:"))
    islem=input("Lütfen yapacağınız islemi seciniz (+,-,*,/,%)")
    if(islem=="+"):
        print("Girilen iki sayının toplamı:",topla(num1,num2))
    elif(islem=="-"):
        print("Girilen İki Sayını farkı:",cikar(num1,num2))
    elif(islem=="*"):
        print("Girilen iki sayının çarpımı:",carp(x,y))
    elif(islem=="/"):
        print("Girilen İki Sayını bolumu:",bol(num1,num2))
    elif(islem=="%"):
        print("Girilen iki sayının modu:",modalma(num1,num2))
    else:
        ("Geçersiz bir islem yaptınız")
        break