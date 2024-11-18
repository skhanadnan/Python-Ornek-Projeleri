#String Metotları

#len:Bir String dizinin uzunluğunu almak için kullanılır

metinverisi="Pycharm ile Python"
uzunluk=len(metinverisi)
print(uzunluk)

#strip:Bir string verisinin başındaki ve sonundaki boşluk karakterini siler

metin="Pycharm ile Python"
yeniMetin=metin.strip()
print(yeniMetin)

#lower:Bir string verisinin tüm karakterlerini küçük harflere dönüştürür.
a="Pycharm ile Python"
b=a.lower()
print(b)

#upper:Bir String verisinin tüm karakterlerini büyük harflere dönüştürür.
a="Pycharm İle PYTHON"
b=a.upper()
print(b)

#replace: Bir String değeri bir başka stirng değer ile yer değiştirir.
a="Pycharm ile Python"
b=a.replace("Pycharm","Editör")
print(b)

#split:Bir string değeri istenen ayraç metni kullanarak alt parçalara böler.
a="Pycharm İle Python"
dizi=a.split("")
print(dizi)

#capitalize:Yalnızca ilk karakteri büyük harfe çevirir.
a="Pycharm ile Python"
b=a.capitalize()
print(b)

a="pycharm ile PYTHON"
b=a.count("")
print(b)

#endswith:String değer belirli bir değerle bitiyorsa true değer döndürür.
a="pycharm ile PYTHON"
b=a.endswith("N")
print(b)

#find:String değerde belirli bir değeri soldan başlayarak arar ve bulduğu indis(indis 0'dan başlar) döndürür. Aranan değer bulunmaza
#-1 değeri döner. Bunun dışında indeks metodu ile aynı işi yapar.
a="pycharm ile PYTHON"
b=a.find("")
print(b)

#index:String değerde belirli bir değeri soldan başlayarak arar ve bulduğu indisi (indis 0'dan başlar) ve döndürür.
#Eğer aradığı karakteri bulmazsa ValueError Hatası verir. Bunun dışında find metodu ile aynı işi yapar.
a="pycharm ile PYTHON"
b=a.index("")
print(b)

#join:Metni string elemanların sonuna ekler.
a=('A','B','C')
c=','
b=c.join(a)
print(b)

#isnumeric:String değerdeki tüm karakterler numeric değerse True Döndürür.
a="123"
b=a.isnumeric()
print(b)

#islower:String değerdeki tüm karaketerler küçük harf ise True döndürür.
a="123"
b=a.islower()
print(b)

#isupper:String değerdeki tüm karakterler büyük harf ise True döndürür.
a="A123"
b=a.isupper()
print(b)

#swapcase:Büyük harfleri küçük harfe,küçük harfleri büyük harfe çevirir.
a="Pycharm ile Python"
b=a.swapcase()
print(b)

#startswith:String belirli bir değerle başlıyorsa True döndürür.
a="Pycharm ile Python"
b=a.startswith("P")
print(b)