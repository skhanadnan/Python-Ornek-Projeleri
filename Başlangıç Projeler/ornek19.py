#İDEAL KİLO HESAPLAMA
import datetime

def idealkilohesaplama(boy,dogumYili,kilo,cinsiyet):
    yas=datetime.datetime.today().year-dogumYili
    if(cinsiyet=="Erkek"):
        k=0.9
    else:
        k=0.8
        idealkilo=(boy-100+yas/10)*k
        fark=idealkilo-kilo
    if  idealkilo==kilo:
            mesaj="İdeal Kilodasınız."
    elif idealkilo>kilo:
            mesaj="Zayıfsınız, kilo almanız gerekir."
    elif idealkilo<kilo:
            mesaj="Kilolusunuz, kilo vermeniz gerekir."
            sonuc={"ideal kilo":idealkilo, "Fark":fark, "Mesaj":mesaj}
            return sonuc
boy=input("Boy Değerini giriniz:")
boy=float(boy)
dogumYili=input("Doğum yılınızı giriniz:")
dogumYili=int(dogumYili)
kilo=input("Kilo Değerini giriniz:")
kilo=int(kilo)
cinsiyet=input("Cinsiyet Değerini Giriniz: (1:Erkek,0:Kadın):")
cinsiyetTurleri={"1":"Erkek","0":"Kadın"}
sonuc=idealkilohesaplama(boy,dogumYili,kilo,cinsiyetTurleri["1"])
print(sonuc)