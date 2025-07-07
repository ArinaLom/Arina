from model import PhoneBook, ContactNotFoundError
from view import PhoneBookView

class PhoneBookController:
    """Контроллер для управления телефонным справочником."""

    def __init__(self, filename):
        """Инициализация контроллера с заданным файлом для хранения контактов."""
        self.phonebook = PhoneBook(filename)
        self.view = PhoneBookView()

    def run(self):
        """Запуск основного цикла управления телефонным справочником."""
        running = True
        while running:
            print("\nТелефонный справочник")
            print("1. Показать все контакты")
            print("2. Создать контакт")
            print("3. Найти контакт")
            print("4. Изменить контакт")
            print("5. Удалить контакт")
            print("6. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.view.show_contacts(self.phonebook.contacts)
            elif choice == '2':
                name, phone, comment = self.view.get_contact_info()
                self.phonebook.add_contact(name, phone, comment)
                self.view.show_message("Контакт добавлен.")
            elif choice == '3':
                search_term = self.view.get_search_term()
                found_contacts = self.phonebook.find_contact(search_term)
                self.view.show_contacts(found_contacts)
            elif choice == '4':
                contact_id = self.view.get_contact_id()
                name, phone, comment = self.view.get_contact_info()
                try:
                    self.phonebook.update_contact(contact_id, name, phone, comment)
                    self.view.show_message("Контакт обновлен.")
                except ContactNotFoundError as e:
                    self.view.show_message(str(e))
            elif choice == '5':
                contact_id = self.view.get_contact_id()
                self.phonebook.delete_contact(contact_id)
                self.view.show_message("Контакт удален.")
            elif choice == '6':
                print("Выход из программы.")
                running = False  # Устанавливаем условие выхода
            else:
                self.view.show_message("Неверный выбор. Пожалуйста, попробуйте снова.")
