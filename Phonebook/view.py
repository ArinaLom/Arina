class PhoneBookView:
    """Класс, отвечающий за отображение информации пользователю."""

    @staticmethod
    def show_contacts(contacts):
        """Отображение списка контактов.
            contacts (list): Список контактов для отображения.
        """
        if not contacts:
            print("Справочник пуст.")
            return
        for contact in contacts:
            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Комментарий: {contact.comment}")

    @staticmethod
    def get_contact_info():
        """Получение информации о контакте от пользователя.
            tuple: Имя, телефон и комментарий контакта.
        """
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        comment = input("Введите комментарий (по желанию): ")
        return name, phone, comment

    @staticmethod
    def get_search_term():
        """Получение строки для поиска от пользователя.
            str: Строка для поиска.
        """
        return input("Введите имя, телефон или комментарий для поиска: ")

    @staticmethod
    def get_contact_id():
        """Получение ID контакта от пользователя.
            int: Уникальный идентификатор контакта.
        """
        return int(input("Введите ID контакта: "))

    @staticmethod
    def show_message(message):
        """Отображение сообщения пользователю.
            message (str): Сообщение для отображения.
        """
        print(message)
