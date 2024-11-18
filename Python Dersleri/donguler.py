#Belirlenen bir başlangıç ve bitiş aralığında for döngüsü oluşturmak için range metodu kullanılır.

for i in range(1,10):
    print(i)
    
#Bir döngünün belirlenen bir şartın gerçekleşmesi durumunda sonlanması isteniyorsa bunun için break komutu kullanılır.
for i in range(20):
    if(i==10):
        break
    print(i)
    
#dongulerde kullanılan başka bir ifade ise while değeridir. while true deyimi ile kod uygulama sonsuz döngüye girer.

while True:
    sayi=int(input("1-10 arası sayı giriniz:"))
    if(sayi!=10):
        continue
    else:
        print("tebrikler")
        break
