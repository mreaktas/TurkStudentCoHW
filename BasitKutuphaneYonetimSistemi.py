class Kitap:
    """
    Kitap bilgilerini tutan sınıf.    
    Özellikler:
    - ad: Kitabın adı
    - yazar: Kitabın yazarı
    - odunc_alindi: Kitabın ödünç alınma durumu (True/False)
    """
    def __init__(self, ad, yazar):
        """
        Yeni bir kitap nesnesi oluşturur.        
        :param ad: Kitabın adı
        :param yazar: Kitabın yazarı
        """
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi = False

    def __str__(self):
        # Kitap bilgilerini string olarak döndürür.
        
        return f"{self.ad} - {self.yazar} {'(Ödünç Alındı)' if self.odunc_alindi else ''}"


class Kutuphane:
    """
    Kütüphane işlemlerini yöneten sınıf.    
    Özellikler:
    - kitaplar: Kayıtlı kitapların listesi
    - odunc_alinan_kitaplar: Ödünç alınan kitapların listesi
    """
    def __init__(self):
        # Boş bir Kütüphane nesnesi oluşturur.
        
        self.kitaplar = []
        self.odunc_alinan_kitaplar = []

    def kitap_ekle(self, kitap):
        """
        Yeni bir kitap ekler.        
        :param kitap: Eklenecek Kitap nesnesi
        """
        self.kitaplar.append(kitap)
        print(f"{kitap.ad} kütüphaneye eklendi.")

    def kitaplari_listele(self):
        # Kütüphanedeki tüm kitapları listeler.
        
        if not self.kitaplar:
            print("Kütüphanede hiç kitap bulunmuyor.")
            return
        
        print("\n--- Kütüphanedeki Kitaplar ---")
        for kitap in self.kitaplar:
            print(kitap)

    def kitap_odunc_ver(self, kitap_adi):
        """
        Belirli bir kitabı ödünç verir.        
        :param kitap_adi: Ödünç verilecek kitabın adı
        """
        for kitap in self.kitaplar:
            if kitap.ad.lower() == kitap_adi.lower() and not kitap.odunc_alindi:
                kitap.odunc_alindi = True
                self.odunc_alinan_kitaplar.append(kitap)
                print(f"{kitap.ad} ödünç verildi.")
                return
        print(f"{kitap_adi} adlı kitap bulunamadı veya zaten ödünç alınmış.")

    def kitap_iade_et(self, kitap_adi):
        """
        Belirli bir kitabı iade alır.        
        :param kitap_adi: İade edilecek kitabın adı
        """
        for kitap in self.odunc_alinan_kitaplar:
            if kitap.ad.lower() == kitap_adi.lower():
                kitap.odunc_alindi = False
                self.odunc_alinan_kitaplar.remove(kitap)
                print(f"{kitap.ad} iade edildi.")
                return
        print(f"{kitap_adi} adlı kitap ödünç alınmamış.")

    def odunc_alinan_kitaplari_listele(self):
        # Ödünç alınan kitapları listeler.
        
        if not self.odunc_alinan_kitaplar:
            print("Ödünç alınan kitap bulunmuyor.")
            return
        
        print("\n--- Ödünç Alınan Kitaplar ---")
        for kitap in self.odunc_alinan_kitaplar:
            print(kitap)


def ana_menu(kutuphane):
    """
    Kullanıcı için ana menü ve etkileşim fonksiyonu.    
    :param kutuphane: Kutuphane sınıfı nesnesi
    """
    while True:
        print("\n--- KÜTÜPHANE YÖNETİM SİSTEMİ ---")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ödünç Ver")
        print("4. Kitap İade Et")
        print("5. Ödünç Alınan Kitapları Listele")
        print("6. Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ")
        
        if secim == '1':
            ad = input("Kitap adını girin: ")
            yazar = input("Yazar adını girin: ")
            yeni_kitap = Kitap(ad, yazar)
            kutuphane.kitap_ekle(yeni_kitap)
        
        elif secim == '2':
            kutuphane.kitaplari_listele()
        
        elif secim == '3':
            kitap_adi = input("Ödünç verilecek kitabın adını girin: ")
            kutuphane.kitap_odunc_ver(kitap_adi)
        
        elif secim == '4':
            kitap_adi = input("İade edilecek kitabın adını girin: ")
            kutuphane.kitap_iade_et(kitap_adi)
        
        elif secim == '5':
            kutuphane.odunc_alinan_kitaplari_listele()
        
        elif secim == '6':
            print("Kütüphane yönetim sisteminden çıkılıyor. İyi günler!")
            break
        
        else:
            print("Geçersiz seçenek. Lütfen 1-6 arasında bir numara seçin.")


def main():
    # Kütüphane nesnesini oluştur
    kutuphane = Kutuphane()

    # Örnek kitaplar ekle
    kutuphane.kitap_ekle(Kitap("1984", "George Orwell"))
    kutuphane.kitap_ekle(Kitap("Savaş ve Barış", "Lev Tolstoy"))
    kutuphane.kitap_ekle(Kitap("Bülbülü Öldürmek", "Harper Lee"))

    # Ana menüyü başlat
    ana_menu(kutuphane)


# Uygulamayı çalıştır
if __name__ == "__main__":
    main()
