class Urun:
    def __init__(self, ad, fiyat, miktar, kategori=None):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar
        self.kategori = kategori

    def toplam_fiyat(self):
        return self.fiyat * self.miktar

class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        # Sepete ürün ekler
        self.urunler.append(urun)
        print(f"{urun.ad} sepete eklendi.")

    def urun_cikar(self, urun_adi):
        # Sepetten ürün çıkarır
        for urun in self.urunler[:]:  # Kopya üzerinde dolaşarak silme işlemi yapılır
            if urun.ad.lower() == urun_adi.lower():
                self.urunler.remove(urun)
                print(f"{urun_adi} sepetten çıkarıldı.")
                return
        print(f"{urun_adi} sepette bulunamadı.")

    def sepeti_listele(self):
        # Sepetteki ürünleri listeler
        if not self.urunler:
            print("Sepet boş.")
            return

        print("\n--- Sepet İçeriği ---")
        for urun in self.urunler:
            print(f"Ürün: {urun.ad}, Miktar: {urun.miktar}, Birim Fiyat: {urun.fiyat} TL, Toplam: {urun.toplam_fiyat()} TL")

    def urunleri_detayli_listele(self):
        # Ürünleri detaylı olarak listeler
        if not self.urunler:
            print("Sepet boş.")
            return

        print("\n--- Detaylı Ürün Listesi ---")
        # Kategori bazında gruplandırma
        kategoriler = {}
        for urun in self.urunler:
            kategori = urun.kategori or "Kategorisiz"
            if kategori not in kategoriler:
                kategoriler[kategori] = []
            kategoriler[kategori].append(urun)

        # Kategorilere göre listeleme
        for kategori, urunler in kategoriler.items():
            print(f"\n{kategori.upper()} KATEGORİSİ:")
            for urun in urunler:
                print(f"- {urun.ad}")
                print(f"  Miktar: {urun.miktar}")
                print(f"  Birim Fiyat: {urun.fiyat} TL")
                print(f"  Toplam Fiyat: {urun.toplam_fiyat()} TL")

    def toplam_tutar(self):
        # Sepetteki toplam tutarı hesaplar
        return sum(urun.toplam_fiyat() for urun in self.urunler)

def menuyu_goster():
    # Kullanıcı menüsünü gösterir
    print("\n--- ALIŞVERİŞ SEPETİ UYGULAMASI ---")
    print("1. Ürün Ekle")
    print("2. Sepeti Görüntüle")
    print("3. Detaylı Ürün Listesi")
    print("4. Ürün Çıkar")
    print("5. Toplam Tutarı Göster")
    print("6. Çıkış")

def main():
    # Sepet oluşturma
    sepet = Sepet()

    # Örnek ürün listesi ekleme
    ornek_urunler = [
        Urun("Elma", 35.5, 10, "Meyve"),
        Urun("Ekmek", 20.0, 5, "Gıda"),
        Urun("Süt", 40.0, 2, "İçecek"),
        Urun("Deterjan", 150.0, 1, "Temizlik"),
        Urun("Çikolata", 5.0, 3, "Atıştırmalık")
    ]

    for urun in ornek_urunler:
        sepet.urun_ekle(urun)

    while True:
        # Menüyü göster
        menuyu_goster()

        # Kullanıcıdan seçim alma
        try:
            secim = input("Yapmak istediğiniz işlemi seçin (1-6): ")

            if secim == '1':
                # Ürün ekleme
                ad = input("Ürün adını girin: ")

                # Fiyat için doğrulama
                while True:
                    try:
                        fiyat = float(input("Ürün birim fiyatını girin (TL): "))
                        break
                    except ValueError:
                        print("Lütfen geçerli bir sayı girin.")

                # Miktar için doğrulama
                while True:
                    try:
                        miktar = int(input("Ürün miktarını girin: "))
                        break
                    except ValueError:
                        print("Lütfen geçerli bir tam sayı girin.")

                # Kategori için optional girdi
                kategori = input("Ürünün kategorisini girin (isteğe bağlı, boş bırakabilirsiniz): ").strip()

                # Yeni ürün oluşturma ve sepete ekleme
                yeni_urun = Urun(ad, fiyat, miktar, kategori if kategori else None)
                sepet.urun_ekle(yeni_urun)

            elif secim == '2':
                # Sepeti listeleme
                sepet.sepeti_listele()

            elif secim == '3':
                # Detaylı ürün listesi
                sepet.urunleri_detayli_listele()

            elif secim == '4':
                # Ürün çıkarma
                ad = input("Çıkarmak istediğiniz ürünün adını girin: ")
                sepet.urun_cikar(ad)

            elif secim == '5':
                # Toplam tutarı gösterme
                print(f"Toplam Tutar: {sepet.toplam_tutar()} TL")

            elif secim == '6':
                # Çıkış
                print("Uygulamadan çıkılıyor. İyi günler!")
                break

            else:
                print("Geçersiz seçim. Lütfen 1 ile 6 arasında bir seçim yapın.")

        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# Programı çalıştırma
if __name__ == "__main__":
    main()
