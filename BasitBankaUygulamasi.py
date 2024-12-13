import random

class Kullanici:
    """
    Kullanıcı bilgilerini tutan sınıf.    
    Özellikler:
    - ad: Kullanıcının adı
    - hesap_no: Kullanıcının hesap numarası
    - bakiye: Kullanıcının hesap bakiyesi
    """
    def __init__(self, ad, hesap_no, bakiye):
        """
        Yeni bir kullanıcı nesnesi oluşturur.        
        :param ad: Kullanıcının adı
        :param hesap_no: Kullanıcının hesap numarası
        :param bakiye: Kullanıcının hesap bakiyesi
        """
        self.ad = ad
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        """
        Hesaba para yatırır.        
        :param miktar: Yatırılacak miktar
        """
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        """
        Hesaptan para çeker.        
        :param miktar: Çekilecek miktar
        """
        if miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")

    def bakiye_sorgula(self):
        """
        Hesap bakiyesini sorgular.        
        :return: Hesap bakiyesi
        """
        print(f"{self.ad} adlı kullanıcının hesap bakiyesi: {self.bakiye} TL")
        return self.bakiye


class Banka:
    """
    Banka işlemlerini yöneten sınıf.    
    Özellikler:
    - kullanicilar: Kayıtlı kullanıcıların listesi
    """
    def __init__(self):
        # Boş bir Banka nesnesi oluşturur.
        
        self.kullanicilar = []

    def hesap_ac(self, ad, bakiye):
        """
        Yeni bir hesap açar.        
        :param ad: Kullanıcının adı
        :param bakiye: Başlangıç bakiyesi
        """
        hesap_no = self.hesap_no_olustur()
        yeni_kullanici = Kullanici(ad, hesap_no, bakiye)
        self.kullanicilar.append(yeni_kullanici)
        print(f"{ad} için yeni hesap açıldı. Hesap No: {hesap_no}, Başlangıç Bakiyesi: {bakiye} TL")

    def hesap_no_olustur(self):
        """
        6 haneli rastgele bir hesap numarası oluşturur.        
        :return: 6 haneli hesap numarası
        """
        while True:
            hesap_no = str(random.randint(100000, 999999))
            if not self.kullanici_bul(hesap_no):
                return hesap_no

    def kullanici_bul(self, hesap_no):
        """
        Hesap numarasına göre kullanıcıyı bulur.        
        :param hesap_no: Kullanıcının hesap numarası
        :return: Bulunan kullanıcı nesnesi veya None
        """
        for kullanici in self.kullanicilar:
            if kullanici.hesap_no == hesap_no:
                return kullanici
        return None

    def para_yatir(self, kullanici, miktar):
        """
        Belirli bir hesaba para yatırır.        
        :param kullanici: Kullanıcı nesnesi
        :param miktar: Yatırılacak miktar
        """
        kullanici.para_yatir(miktar)

    def para_cek(self, kullanici, miktar):
        """
        Belirli bir hesaptan para çeker.        
        :param kullanici: Kullanıcı nesnesi
        :param miktar: Çekilecek miktar
        """
        kullanici.para_cek(miktar)

    def bakiye_sorgula(self, hesap_no):
        """
        Belirli bir hesabın bakiyesini sorgular.        
        :param hesap_no: Kullanıcının hesap numarası
        :return: Kullanıcı nesnesi ve hesap bakiyesi
        """
        kullanici = self.kullanici_bul(hesap_no)
        if kullanici:
            kullanici.bakiye_sorgula()
            return kullanici
        else:
            print("Hesap bulunamadı.")
            return None

    def tum_hesaplari_goster(self):
        # Tüm hesapları listeler.
        
        if not self.kullanicilar:
            print("Herhangi bir hesap bulunmuyor.")
            return
        
        print("\n--- Tüm Hesaplar ---")
        for kullanici in self.kullanicilar:
            print(f"Ad: {kullanici.ad}, Hesap No: {kullanici.hesap_no}, Bakiye: {kullanici.bakiye} TL")


def admin_girisi(banka):
    """
    Banka yetkilisi girişi ve tüm hesapları gösterme fonksiyonu.    
    :param banka: Banka sınıfı nesnesi
    """
    kullanici_adi = input("Yetkili kullanıcı adını girin: ")
    sifre = input("Yetkili şifresini girin: ")

    if kullanici_adi == "admin" and sifre == "admin":
        banka.tum_hesaplari_goster()
    else:
        print("Geçersiz kullanıcı adı veya şifre.")


def ana_menu(banka):
    """
    Kullanıcı için ana menü ve etkileşim fonksiyonu.    
    :param banka: Banka sınıfı nesnesi
    """
    while True:
        print("\n--- BANKA SİSTEMİ ---")
        print("1. Hesap Aç")
        print("2. Bakiye Sorgula ve İşlemler")
        print("3. Para Yatır")
        print("4. Para Çek")
        print("5. Yetkili Girişi")
        print("6. Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ")
        
        if secim == '1':
            ad = input("Adınızı girin: ")
            while True:
                try:
                    bakiye = float(input("Başlangıç bakiyesini girin: "))
                    break
                except ValueError:
                    print("Lütfen geçerli bir bakiye değeri girin.")
            banka.hesap_ac(ad, bakiye)
        
        elif secim == '2':
            hesap_no = input("Hesap numaranızı girin: ")
            kullanici = banka.bakiye_sorgula(hesap_no)
            if kullanici:
                while True:
                    print("\n--- İşlemler ---")
                    print("1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Ana Menüye Dön")
                    
                    islem_secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-3): ")
                    
                    if islem_secim == '1':
                        while True:
                            try:
                                miktar = float(input("Yatırılacak miktarı girin: "))
                                break
                            except ValueError:
                                print("Lütfen geçerli bir miktar girin.")
                        banka.para_yatir(kullanici, miktar)
                    
                    elif islem_secim == '2':
                        while True:
                            try:
                                miktar = float(input("Çekilecek miktarı girin: "))
                                break
                            except ValueError:
                                print("Lütfen geçerli bir miktar girin.")
                        banka.para_cek(kullanici, miktar)
                    
                    elif islem_secim == '3':
                        break
                    
                    else:
                        print("Geçersiz seçenek. Lütfen 1-3 arasında bir numara seçin.")
        
        elif secim == '3':
            hesap_no = input("Hesap numaranızı girin: ")
            kullanici = banka.kullanici_bul(hesap_no)
            if kullanici:
                while True:
                    try:
                        miktar = float(input("Yatırılacak miktarı girin: "))
                        break
                    except ValueError:
                        print("Lütfen geçerli bir miktar girin.")
                banka.para_yatir(kullanici, miktar)
            else:
                print("Hesap bulunamadı.")
        
        elif secim == '4':
            hesap_no = input("Hesap numaranızı girin: ")
            kullanici = banka.kullanici_bul(hesap_no)
            if kullanici:
                while True:
                    try:
                        miktar = float(input("Çekilecek miktarı girin: "))
                        break
                    except ValueError:
                        print("Lütfen geçerli bir miktar girin.")
                banka.para_cek(kullanici, miktar)
            else:
                print("Hesap bulunamadı.")
        
        elif secim == '5':
            admin_girisi(banka)
        
        elif secim == '6':
            print("Banka sisteminden çıkılıyor. İyi günler!")
            break
        
        else:
            print("Geçersiz seçenek. Lütfen 1-6 arasında bir numara seçin")

def main():
    # Banka nesnesini oluştur
    banka = Banka()

    # Örnek banka hesapları ekle
    banka.hesap_ac("Ali Veli", 5000)
    banka.hesap_ac("Ayşe Yılmaz", 3000)
    banka.hesap_ac("Mehmet Demir", 7000)

    # Ana menüyü başlat
    ana_menu(banka)

# Uygulamayı çalıştır
if __name__ == "__main__":
    main()
