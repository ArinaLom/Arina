import unittest
from unittest.mock import patch, mock_open
import json
import os
from model import PhoneBook, ContactNotFoundError

class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        # Этот метод выполняется перед каждым тестом
        self.test_file = 'test_contacts.json'  # Имя файла для тестов
        self.phonebook = PhoneBook(self.test_file)  # Создаем новый телефонный справочник

    def tearDown(self):
        # Этот метод выполняется после каждого теста
        if os.path.exists(self.test_file):
            os.remove(self.test_file)  # Удаляем файл, если он существует

    def test_add_contact(self):
        # Проверяем, что контакт добавляется правильно
        self.phonebook.add_contact("Иван Иванов", "123456789", "Друг")
        self.assertEqual(len(self.phonebook.contacts), 1)  # Должен быть 1 контакт
        self.assertEqual(self.phonebook.contacts[0].name, "Иван Иванов")  # Проверяем имя

    def test_find_contact_by_name(self):
        # Проверяем поиск контакта по имени
        self.phonebook.add_contact("Иван Иванов", "123456789", "Друг")
        found_contacts = self.phonebook.find_contact("Иван Иванов")
        self.assertEqual(len(found_contacts), 1)  # Должен быть найден 1 контакт
        self.assertEqual(found_contacts[0].name, "Иван Иванов")  # Проверяем имя

    def test_update_contact(self):
        # Проверяем обновление контакта
        self.phonebook.add_contact("Иван Иванов", "123456789", "Друг")
        self.phonebook.update_contact(1, "Петр Петров", "987654321", "Лучший друг")
        self.assertEqual(self.phonebook.contacts[0].name, "Петр Петров")  # Проверяем новое имя
        self.assertEqual(self.phonebook.contacts[0].phone, "987654321")  # Проверяем новый телефон

    def test_delete_contact(self):
        # Проверяем удаление контакта
        self.phonebook.add_contact("Иван Иванов", "123456789", "Друг")
        self.phonebook.delete_contact(1)
        self.assertEqual(len(self.phonebook.contacts), 0)  # Должен быть 0 контактов

    def test_load_contacts(self):
        # Проверяем загрузку контактов из файла
        mock_data = json.dumps([{"id": 1, "name": "Иван Иванов", "phone": "123456789", "comment": "Друг"}])
        with patch("builtins.open", mock_open(read_data=mock_data)):
            self.phonebook.load_contacts()  # Загружаем контакты
            self.assertEqual(len(self.phonebook.contacts), 1)  # Должен быть 1 контакт
            self.assertEqual(self.phonebook.contacts[0].name, "Иван Иванов")  # Проверяем имя

    def test_save_contacts(self):
        # Проверяем сохранение контактов в файл
        self.phonebook.add_contact("Иван Иванов", "123456789", "Друг")
        with patch("builtins.open", mock_open()) as mocked_file:
            self.phonebook.save_contacts()  # Сохраняем контакты
            mocked_file.assert_called_once_with(self.test_file, 'w', encoding='utf-8')  # Проверяем, что файл открыт правильно
            handle = mocked_file()
            handle.write.assert_called_once_with(json.dumps([{"id": 1, "name": "Иван Иванов", "phone": "123456789", "comment": "Друг"}], ensure_ascii=False, indent=4))  # Проверяем, что данные записаны правильно

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты
