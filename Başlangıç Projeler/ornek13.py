#1 İLE 100 ARASINDA RASTGELE S10 TAM SAYI ÜRETİP DİZİ İÇİNE EKLEME
import random
dizi=list()
for i in range(10):
    sayi=random.randint(1,100)
    dizi.append(sayi)
    
print(dizi)