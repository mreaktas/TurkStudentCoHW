class Sehir:
    """
    Şehir bilgilerini ve sıcaklık verilerini tutan sınıf.

    Özellikleri:
    - ad: Şehrin adı
    - sicaklik: Şehrin sıcaklığı
    """
    def __init__(self, ad, sicaklik):
        """
        Yeni bir şehir nesnesi oluşturur.

        :param ad: Şehrin adı
        :param sicaklik: Şehrin sıcaklığı
        """
        self.ad = ad
        self.sicaklik = sicaklik


class HavaDurumu:
    """
    Şehirlerin hava durumu bilgilerini yöneten sınıf.

    Özellikleri:
    - sehirler: Kayıtlı şehirlerin listesi
    """
    def __init__(self):
        # Boş bir HavaDurumu nesnesi oluşturur.

        self.sehirler = []

    def sehir_ekle(self, sehir):
        """
        Yeni bir şehir ekler.
        :param sehir: Eklenecek Sehir nesnesi
        """
        self.sehirler.append(sehir)

    def sehir_sorgula(self, ad):
        """
        Verilen ada sahip şehri bulur.
        :param ad: Sorgulanacak şehrin adı
        :return: Bulunan şehir nesnesi veya None
        """
        for sehir in self.sehirler:
            if sehir.ad.lower() == ad.lower():
                return sehir
        return None

    def tum_sehirleri_listele(self):
        # Sistemde kayıtlı tüm şehirleri listeler.

        print("\nKayıtlı Şehirler:")
        for i, sehir in enumerate(self.sehirler, 1):
            print(f"{i}. {sehir.ad} - {sehir.sicaklik}°C")

    def sicaklik_guncelle(self, ad, yeni_sicaklik):
        """
        Belirli bir şehrin sıcaklığını günceller.
        :param ad: Şehrin adı
        :param yeni_sicaklik: Yeni sıcaklık değeri
        """
        sehir = self.sehir_sorgula(ad)
        if sehir:
            sehir.sicaklik = yeni_sicaklik
            print(f"{sehir.ad} şehrinin sıcaklığı {yeni_sicaklik}°C olarak güncellendi.")
        else:
            print(f"{ad} şehri bulunamadı.")

    def hava_tahmini(self, ad):
        """
        Belirli bir şehir için hava durumu tahmini ve önerisi verir.
        :param ad: Şehrin adı
        :return: Hava durumu tahmini ve giyim önerisi
        """
        sehir = self.sehir_sorgula(ad)
        if sehir:
            print(f"\n{sehir.ad} şehri için hava durumu:")
            print(f"Sıcaklık: {sehir.sicaklik}°C")

            # Sıcaklığa göre tavsiye verme
            if sehir.sicaklik < 0:
                print("Öneriler: Soğuk, sıkı giyinin.")
            elif 0 <= sehir.sicaklik < 15:
                print("Öneriler: Serin, mont almayı unutmayın.")
            else:
                print("Öneriler: Hava güzel, rahat giyin.")
        else:
            print(f"{ad} şehri bulunamadı.")

    def yeni_sehir_ekle(self):
        # Kullanıcıdan yeni bir şehir bilgisi alarak sisteme ekler.

        ad = input("Şehrin adını giriniz: ")
        while True:
            try:
                sicaklik = float(input("Sıcaklığı giriniz (°C): "))
                break
            except ValueError:
                print("Hata: Lütfen geçerli bir sıcaklık değeri giriniz.")

        yeni_sehir = Sehir(ad, sicaklik)
        self.sehir_ekle(yeni_sehir)
        print(f"{ad} şehri başarıyla eklendi.")


def ana_menu(hava_durumu):
    """
    Kullanıcı için ana menü ve etkileşim fonksiyonu.
    :param hava_durumu: HavaDurumu sınıfı nesnesi
    """
    while True:
        print("\n--- HAVA DURUMU UYGULAMASI ---")
        print("1. Şehir Sorgula")
        print("2. Tüm Şehirleri Listele")
        print("3. Yeni Şehir Ekle")
        print("4. Sıcaklık Güncelle")
        print("5. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin (1-5): ")

        if secim == '1':
            ad = input("Hava durumunu sorgulamak istediğiniz şehrin adını girin: ")
            hava_durumu.hava_tahmini(ad)

        elif secim == '2':
            hava_durumu.tum_sehirleri_listele()

        elif secim == '3':
            hava_durumu.yeni_sehir_ekle()

        elif secim == '4':
            ad = input("Sıcaklığını güncellemek istediğiniz şehrin adını girin: ")
            while True:
                try:
                    yeni_sicaklik = float(input("Yeni sıcaklığı girin (°C): "))
                    break
                except ValueError:
                    print("Hata: Lütfen geçerli bir sıcaklık değeri giriniz.")
            hava_durumu.sicaklik_guncelle(ad, yeni_sicaklik)

        elif secim == '5':
            print("Uygulamadan çıkılıyor. İyi günler!")
            break

        else:
            print("Geçersiz seçenek. Lütfen 1-5 arasında bir numara seçin.")


def main():
    # HavaDurumu nesnesini oluştur
    hava_durumu = HavaDurumu()

    # Varsayılan şehirler ekle
    ornek_sehirler = [
        Sehir("İstanbul", 12),
        Sehir("Ankara", -3),
        Sehir("İzmir", 22),
        Sehir("Bursa", 15),
        Sehir("Antalya", 25)
    ]

    for sehir in ornek_sehirler:
        hava_durumu.sehir_ekle(sehir)

    # Ana menüyü başlat
    ana_menu(hava_durumu)


# Uygulamayı çalıştır
if __name__ == "__main__":
    main()
