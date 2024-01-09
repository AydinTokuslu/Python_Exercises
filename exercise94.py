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
        
        
        """))

else:
    print("ATM'den ayrıldınız")