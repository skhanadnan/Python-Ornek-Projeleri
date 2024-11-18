#Python ile TC kimlik kontrolü
def tckontrol(tc):
    sonuc=True
    if 11!=len(tc) or tc[0:1]=="0" or tc.isnumeric()==False:
        return False
    else:
        s1=int(tc[0])
        s2=int(tc[1])
        s3=int(tc[2])
        s4=int(tc[3])
        s5=int(tc[4])
        s6=int(tc[5])
        s7=int(tc[6])
        s8=int(tc[7])
        s9=int(tc[8])
        s10=int(tc[9])
        s11=int(tc[10])
        
        toplamTekler=s1+s3+s5+s7+s9
        toplamCiftler=s2+s4+s6+s8
    if(7*toplamTekler-toplamCiftler) %10!=s10:
        return False
    toplam10=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10
    
    if toplam10%10!=s11:
        return False
    
    return sonuc

tc=input("TC giriniz")
sonuc=tckontrol(tc)
print(sonuc)