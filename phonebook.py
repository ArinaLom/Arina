import os

class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        contact_id = int(parts[0])
                        name = parts[1]
                        phone = parts[2]
                        comment = parts[3] if len(parts) > 3 else ''
                        self.contacts.append({"id": contact_id, "name": name, "phone": phone, "comment": comment})

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for contact in self.contacts:
                file.write(f"{contact['id']},{contact['name']},{contact['phone']},{contact.get('comment', '')}\n")

    def show_contacts(self):
        if not self.contacts:
            print("Справочник пуст.")
            return
        for contact in self.contacts:
            print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact.get('comment', '')}")

    def create_contact(self):
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        comment = input("Введите комментарий (по желанию): ")
        contact_id = len(self.contacts) + 1
        self.contacts.append({"id": contact_id, "name": name, "phone": phone, "comment": comment})
        print("Контакт добавлен.")

    def find_contact(self):
        search_term = input("Введите имя, телефон или комментарий для поиска: ")
        found_contacts = [c for c in self.contacts if search_term in c['name'] or search_term in c['phone'] or search_term in c.get('comment', '')]
        if found_contacts:
            for contact in found_contacts:
                print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact.get('comment', '')}")
        else:
            print("Контакты не найдены.")

    def update_contact(self):
        contact_id = int(input("Введите ID контакта для изменения: "))
        for contact in self.contacts:
            if contact['id'] == contact_id:
                contact['name'] = input("Введите новое имя: ")
                contact['phone'] = input("Введите новый телефон: ")
                contact['comment'] = input("Введите новый комментарий (по желанию): ")
                print("Контакт обновлен.")
                return
        print("Контакт не найден.")

    def delete_contact(self):
        contact_id = int(input("Введите ID контакта для удаления: "))
        self.contacts = [c for c in self.contacts if c['id'] != contact_id]
        print("Контакт удален.")

    def run(self):
        while True:
            print("\nТелефонный справочник")
            print("1. Показать все контакты")
            print("2. Создать контакт")
            print("3. Найти контакт")
            print("4. Изменить контакт")
            print("5. Удалить контакт")
            print("6. Открыть файл")
            print("7. Сохранить файл")
            print("8. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_contacts()
            elif choice == '2':
                self.create_contact()
            elif choice == '3':
                self.find_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                self.load_contacts()
                print("Файл открыт и контакты загружены.")
            elif choice == '7':
                self.save_contacts()
                print("Контакты сохранены в файл.")
            elif choice == '8':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    phonebook = PhoneBook("contacts.txt")
    phonebook.run()
