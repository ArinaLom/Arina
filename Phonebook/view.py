
class PhoneBookView:
    @staticmethod
    def show_contacts(contacts):
        if not contacts:
            print("Справочник пуст.")
            return
        for contact in contacts:
            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Комментарий: {contact.comment}")

    @staticmethod
    def get_contact_info():
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        comment = input("Введите комментарий (по желанию): ")
        return name, phone, comment

    @staticmethod
    def get_search_term():
        return input("Введите имя, телефон или комментарий для поиска: ")

    @staticmethod
    def get_contact_id():
        return int(input("Введите ID контакта: "))

    @staticmethod
    def show_message(message):
        print(message)
