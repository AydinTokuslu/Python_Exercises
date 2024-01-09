sahip_olunan_para = 2000

secim = input("işlem yapmak için 's', çıkmak için 'a' yazınız : ")

if secim == "s":
    while True:
        islem = int(input("""
        İşlemler
        ------------
        1-Para Çekme
        2-Para Yatırma
        3-Hesap Bakiyesi Gösterme
        4-Kart İadesi
        
        Yapmak istediğiniz işlemin numarasını giriniz : 
        """))
        if islem == 1:
            cekilmek_istenen_tutar = int(input("Çekmek istediğiniz para tutarını giriniz : "))
            if sahip_olunan_para < cekilmek_istenen_tutar:
                print("Bu işle  geçersizdir. Yeterli bakiyeniz bulunmamaktadır.")
            else:
                sahip_olunan_para-=cekilmek_istenen_tutar
        elif islem == 2:
            yatirilmek_istenen_tutar = int(input("Yatırmak istediğiniz para tutarını giriniz : "))
            sahip_olunan_para+=yatirilmek_istenen_tutar

else:
    print("ATM'den ayrıldınız")