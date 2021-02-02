import time
from functools import reduce

"""BU KÜTÜPHANE 'TKİNTER' KÜTÜPHANESİNDE 'RGB' RENK KODLARINI KULLANABİLMEK İÇİN 2020 EYLÜL'DE YAZILMIŞTIR.
KULLANILMASI VE PAYLAŞILMASI ÜCRETSİZDİR.KÜTÜPHANENİN GELİŞTİRME AŞAMALARI DEVAM ETMEKTEDİR.
KÜTÜPHANENİN TEMEL PROBLEMLERİNDEN BİRİ, RGB RENK KODLARININ DÖNÜŞÜMÜNDE BAZI DURUMLARDA YAVAŞ KALMASIDIR.
KÜTÜPHANE DAHA ÇOK WİDGET-HOVER İŞLEMLERİ İÇİN UYGUNDUR.FAKAT HER DURUMDA KULLANILABİLMEKTEDİR.
KÜTÜPHANENİN YAPIMINDA 'TİME' VE 'FUNCTOOLS' KÜTÜPHANELERİNDEN YARDIM ALINMIŞTIR.
KÜTÜPHANEYİ DÜZGÜN VE/VEYA DAHA İYİ BİR ŞEKİLDE KULLANABİLMEK İÇİN EN AZ GİRİŞ SEVİYESİNDE 'RGB' RENK KODU
SİSTEMİ BİLİNMELİDİR.KÜTÜPHANENİN İÇİNDE BULUNAN 'ebob' ve 'ebobb' FONKSİYONLARI İNTERNETTEN ALINMIŞTIR VE
AMAÇLARI 'RGB' RENK KODLARININ DÖNÜŞÜMÜNDE YARDIMCI OLMAK VE DÖNÜŞME SÜRESİNİ KISALTMAK İÇİN KULLANILMIŞTIR.
MUTLAK DEĞER FONKSİYONU KENDİM TARAFINDAN YAZILMIŞTIR.BU KÜTÜPHANEYİ KULLANARAK ÇOK RAHAT BİR ŞEKİLDE
HOVER İŞLEMLERİ YAPILABİLMEKTEDİR.
KÜTÜPHANEYİ HERHANGİ BİR WİDGETA HOVER AMACI İLE KULLANABİLMEK İÇİN:

GİRİŞ: widget.bind(<'Enter'>,lambda x: rgb_to(parametreler...))
ÇIKIŞ: widget.bimd(<'Leave'>,lambda x: rgb_to(parametreler...))

KÜTÜPHANEYİ YAZAN: SAMET ERİLTER
TEST EDEN:         YİĞİT EMİN KOLAN

17/09/2020
"""

def rgb(rgb):
    """
    TKİNTERİN DESTEKLEDİĞİ 'HEX COLOR MODUNU' 'RGB' CİNSİNDEN ALIYORUZ VE HEXE
    ÇEVİRİYORUZ
    FONKSİYONUN İÇİNE DEĞER YAZILIRKEN İKİ TANE PARANTEZ AÇILMALIDIR, ÖRNEK:
    rgb((100,100,100))
    """
    return "#%02x%02x%02x" % rgb



liste_renk = ["red","green","blue"] # KULLANILABİLEN RENKLER #
renk_değer ={
    "red":(255,0,0),"green":(0,255,0),"blue":(0,0,255)
    }

key_r = False
key_g = False
key_b = False

""" EBOB FONKSİYONLARI """

def ebobb(*args):
    return reduce(ebob, args)

def ebob(a,b):
	while b:
		a,b=b,a%b;
	return a;



""" MUTLAK DEĞER FONKSİYONU """

def mutlak(s1):
    if s1 < 0:
        s1 = -s1
    elif s1 == 0:
        s1 = 0
    else:
        s1 = s1

    return s1
 

"""rgb_to fonksiyonu: İki 'rgb' kodunu birbirine çevirir ve (istenirse) widgetlara uygular"""

def rgb_to(renk1,renk2,hız=0.0001,widget=None,root=None,text=None,fg=False,bg=False):
    global key_r
    global key_g
    global key_b
    global p
    if renk1 == renk2:
        return renk2
    
    try:
        hız/1
    
    except TypeError:
        return hız,"onluk tabanda bir veri değil"
        
    if renk1 in liste_renk and renk2 in liste_renk:
        değer1 = renk_değer[renk1]
        değer2 = renk_değer[renk2]
        r1 = int(değer1[0])
        g1 = int(değer1[1])
        b1 = int(değer1[2])

        r2 = int(değer2[0])
        g2 = int(değer2[1])
        b2 = int(değer2[2])

        r_fark = r1 - r2
        g_fark = g1 - g2
        b_fark = b1 - b2
        

        if r_fark < 0:
            key_r = True
                
        elif r_fark == 0:
            r1 = 0
        else:
            key_r = False
            
        if g_fark < 0:
            key_g = True
        elif g_fark == 0:
            g1 = 0
        else:
            key_g = False
            
        if b_fark < 0:
            key_b = True
        elif b_fark == 0:
            b1 = 0
        else:
            key_b = False
    elif renk1 not in liste_renk and renk2 not in liste_renk:
        r1 = int(renk1[0])
        g1 = int(renk1[1])
        b1 = int(renk1[2])

        r2 = int(renk2[0])
        g2 = int(renk2[1])
        b2 = int(renk2[2])
        # print(g1,g2)

        r_fark = r1 - r2
        g_fark = g1 - g2
        b_fark = b1 - b2

        if r_fark < 0:
            key_r = True
        else:
            key_r = False
            
        if g_fark < 0:
            key_g = True
        else:
            key_g = False
            
        if b_fark < 0:
            key_b = True
        else:
            key_b = False

    ebob_bul = ebobb(mutlak(r_fark),mutlak(g_fark),mutlak(b_fark))
    katsayı = ebob_bul
    katsayı_eski = ebob_bul
    # print("eski katsayı:",katsayı_eski)
    if katsayı == 50:
        katsayı = 10
        # print("yeni katsayı:",katsayı)
    else:
        if katsayı > 10:
            for j in range(2,10):
                if katsayı % j == 0:
                    if katsayı % 3 == 0:
                        katsayı = int(katsayı / 3)
                    if katsayı % 4 == 0:
                        katsayı = int(katsayı / 4)
                    if katsayı % 5 == 0:
                        katsayı = int(katsayı / 5)
                    if katsayı % 6 == 0:
                        katsayı = int(katsayı / 6)
                    if katsayı % 7 == 0:
                        katsayı = int(katsayı / 7)
                    if katsayı % 8 == 0:
                        katsayı = int(katsayı / 8)
                    if katsayı % 9 == 0:
                        katsayı = int(katsayı / 9)
                            
        
            # print("yeni katsayı:",katsayı)
        
    for i in range(255):
        # print(r1,g1,b1)
        if (r1,g1,b1) != (r2,g2,b2):
            if r1 != r2:
                if r_fark == 0:
                    pass
                else:
                    if key_r == True:
                        r1 += katsayı
                    else:
                        r1 -= katsayı
            if g1 != g2:
                if g_fark == 0:
                    pass
                else:
                    if key_g == True:
                        g1 += katsayı
                    else:
                        g1 -= katsayı

            if b1 != b2:
                if b_fark == 0:
                    pass
                else:
                    if key_b == True:
                        b1 += katsayı
                    else:
                        b1 -= katsayı

            if not widget:
                pass
            else:
                if not root:
                    if fg == True and bg == False:
                        widget["fg"] = rgb((r1,g1,b1))
                    if bg == True and fg == False:
                        widget["bg"] = rgb((r1,g1,b1))
                    if bg == True and fg == True:
                        return "'bg' ve 'fg' parametreleri aynı anda girilemez"
                    
                    time.sleep(hız)
                    if text:
                        widget["text"] = text
                    else:
                        if fg == True and bg == False:
                            widget["fg"] = rgb((r1,g1,b1))
                        if bg == True and fg == False:
                            widget["bg"] = rgb((r1,g1,b1))
                        if bg == True and fg == True:
                            return "'bg' ve 'fg' parametreleri aynı anda girilemez"


                else:
                    if fg == True and bg == False:
                        widget["fg"] = rgb((r1,g1,b1))
                    if bg == True and fg == False:
                        widget["bg"] = rgb((r1,g1,b1))
                    if fg == True and bg == True:
                        return "'bg' ve 'fg' parametreleri aynı anda girilemez"
                    time.sleep(hız)
                    root.update()
                    if text:
                        widget["text"] = text
                    else:
                        pass
        else:
            break
        
    
    return (r1,g1,b1)


if __name__ == "__main__":
    print("bruh")