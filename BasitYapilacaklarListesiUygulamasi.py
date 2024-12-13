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
