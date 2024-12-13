class Film:
    #Film bilgilerini saklayan sınıf.
    def __init__(self, ad, yonetmen, yil, tur):

        """
        Film sınıfı için başlatıcı metot.
        :param ad: Filmin adı
        :param yonetmen: Filmin yönetmeni
        :param yil: Filmin çıkış yılı
        :param tur: Filmin türü
        """
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self):
        """Film bilgilerini string olarak döndürür."""
        return f"{self.ad} (Yıl: {self.yil}, Yönetmen: {self.yonetmen}, Tür: {self.tur})"

class FilmYoneticisi:
    #Film yönetimi için ana sınıf.

    def __init__(self):
        """Film listesini başlatır."""
        self.filmler = []

    def film_ekle(self, film):
        """
        Film listesine yeni film ekler.
        :param film: Eklenecek Film nesnesi
        """
        self.filmler.append(film)
        print(f"{film.ad} filmi listeye başarıyla eklendi.")

    def filmleri_listele(self, tur=None, yil=None):
        """
        Filmleri listeler. İsteğe bağlı olarak türe veya yıla göre filtreler.
        :param tur: Filtrelenecek film türü
        :param yil: Filtrelenecek film yılı
        """
        filtrelenmis_filmler = self.filmler

        if tur:
            filtrelenmis_filmler = [film for film in filtrelenmis_filmler if film.tur.lower() == tur.lower()]

        if yil:
            filtrelenmis_filmler = [film for film in filtrelenmis_filmler if film.yil == yil]

        if not filtrelenmis_filmler:
            print("Hiç film bulunamadı.")
            return

        print("--- Filmler ---")
        for film in filtrelenmis_filmler:
            print(film)

    def film_sil(self, ad):
        """
        Belirtilen ada sahip filmi siler.
        :param ad: Silinecek filmin adı
        """
        for film in self.filmler[:]:
            if film.ad.lower() == ad.lower():
                self.filmler.remove(film)
                print(f"{ad} filmi başarıyla silindi.")
                return

        print(f"{ad} adlı film bulunamadı.")

    def film_ara(self, ad):
        """
        Belirtilen isme sahip filmi arar ve döndürür.
        :param ad: Aranacak filmin adı
        :return: Bulunan Film nesnesi veya None
        """
        for film in self.filmler:
            if film.ad.lower() == ad.lower():
                return film
        return None

# Örnek kullanım
def main():
    # Film Yöneticisi oluştur
    yonetici = FilmYoneticisi()

    # Örnek film listesi ekleme
    ornek_filmler = [
        Film("Inception", "Christopher Nolan", 2010, "Bilim Kurgu"),
        Film("Interstellar", "Christopher Nolan", 2014, "Bilim Kurgu"),
        Film("Pulp Fiction", "Quentin Tarantino", 1994, "Suç"),
        Film("Yeşil Yol", "Frank Darabont", 1999, "Drama"),
        Film("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999, "Bilim Kurgu"),
        Film("The Godfather", "Francis Ford Coppola", 1972, "Suç"),
        Film("The Dark Knight", "Christopher Nolan", 2008, "Aksiyon"),
        Film("Forrest Gump", "Robert Zemeckis", 1994, "Drama"),
        Film("Fight Club", "David Fincher", 1999, "Dram"),
        Film("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
    ]

    for film in ornek_filmler:
        yonetici.film_ekle(film)

    while True:
        print("\n1. Film Ekle")
        print("2. Filmleri Listele")
        print("3. Film Sil")
        print("4. Film Ara")
        print("5. Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            ad = input("Film Adı: ")
            yonetmen = input("Yönetmen: ")
            yil = int(input("Çıkış Yılı: "))
            tur = input("Tür: ")
            yonetici.film_ekle(Film(ad, yonetmen, yil, tur))
        elif secim == "2":
            tur = input("Filtrelemek istediğiniz tür (boş bırakabilirsiniz): ")
            yil = input("Filtrelemek istediğiniz yıl (boş bırakabilirsiniz): ")
            yil = int(yil) if yil else None
            yonetici.filmleri_listele(tur if tur else None, yil)
        elif secim == "3":
            ad = input("Silmek istediğiniz filmin adını yazınız: ")
            yonetici.film_sil(ad)
        elif secim == "4":
            ad = input("Aramak istediğiniz filmin adını yazınız: ")
            film = yonetici.film_ara(ad)
            if film:
                print(f"\nAranan Film: {film}")
            else:
                print("\nAradığınız film bulunamadı.")
        elif secim == "5":
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
