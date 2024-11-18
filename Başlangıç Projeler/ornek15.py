#Metindeki Her Harfin Arasına Virgül Koyma
metin=input("Bir Metin Giriniz:")
sonuc=" "
for harf in metin:
    sonuc=sonuc + harf +","
    print(sonuc)