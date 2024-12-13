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

"""# Basit YapılacakLar Listesi"""

import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        return f"[{'✓' if self.completed else ' '}] {self.name}"

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task_name):
        """Yeni bir görev ekler."""
        task = Task(task_name)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Görev eklendi: {task_name}")

    def list_tasks(self):
        """Tüm görevleri listeler."""
        if not self.tasks:
            print("Herhangi bir görev bulunmuyor.")
            return

        print("\n--- Tamamlanmamış Görevler ---")
        for index, task in enumerate(self.tasks, 1):
            if not task.completed:
                print(f"{index}. {task}")

        print("\n--- Tamamlanmış Görevler ---")
        for index, task in enumerate(self.tasks, 1):
            if task.completed:
                print(f"{index}. {task}")

    def complete_task(self, task_index):
        """Görevi tamamlandı olarak işaretler."""
        try:
            # Dizin 0'dan başladığı için 1 çıkarıyoruz
            task = self.tasks[task_index - 1]
            task.completed = True
            self.save_tasks()
            print(f"Görev tamamlandı: {task.name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def delete_task(self, task_index):
        """Görevi siler."""
        try:
            # Dizin 0'dan başladığı için 1 çıkarıyoruz
            task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Görev silindi: {task.name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def save_tasks(self):
        """Görevleri dosyaya kaydeder."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.completed}\n")

    def load_tasks(self):
        """Görevleri dosyadan yükler."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.tasks = []
                for line in f:
                    name, completed = line.strip().split(',')
                    task = Task(name, completed == 'True')
                    self.tasks.append(task)

def main():
    task_manager = TaskManager()

    # Örnek görev listesi ekleme
    ornek_gorevler = [
        "Alışveriş yap",
        "Evi temizle",
        "Faturaları öde",
        "Projeyi tamamla",
        "Kitap oku"
    ]

    for gorev in ornek_gorevler:
        task_manager.add_task(gorev)

    while True:
        print("\n--- Yapılacaklar Listesi ---")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görevi Tamamla")
        print("4. Görevi Sil")
        print("5. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçiniz (1-5): ")

        if secim == '1':
            task_name = input("Görev adını girin: ")
            task_manager.add_task(task_name)
        elif secim == '2':
            task_manager.list_tasks()
        elif secim == '3':
            task_manager.list_tasks()
            task_index = int(input("Tamamlamak istediğiniz görevin numarasını girin: "))
            task_manager.complete_task(task_index)
        elif secim == '4':
            task_manager.list_tasks()
            task_index = int(input("Silmek istediğiniz görevin numarasını girin: "))
            task_manager.delete_task(task_index)
        elif secim == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1-5 arasında bir numara seçin.")

if __name__ == "__main__":
    main()
