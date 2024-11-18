#Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük harflere çevirme
metin=input("Bir metin giriniz:")
yenimetin=""
for i in metin:
    if i.islower():
        yenimetin +=i.upper()
    else:
        yenimetin +=i.lower()
        
        print(yenimetin)