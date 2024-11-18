#Üç Adet Sayıyı Karşılaştırıp Sıralama
num1=int(input("Lütfen birinci sayıyı giriniz:")) 
num2=int(input("Lütfen ikinci sayıyı giriniz:"))
num3=int(input("Lütfen üçüncü sayıyı giriniz:"))
if(num1>num2 and num1>num3):
    print("En büyük sayı birinci sayı")
elif(num2>num1 and num2>num3):
    print("En Büyük ikinci sayı")
else:
    print("En Büyük Sayı üçüncü")