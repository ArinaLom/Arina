
import json
import os

class ContactNotFoundError(Exception):
    """Исключение, выбрасываемое при отсутствии контакта."""
    pass

class Contact:
    def __init__(self, contact_id, name, phone, comment=''):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.comment = comment

class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.contacts = [Contact(**contact) for contact in data]

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, ensure_ascii=False, indent=4)

    def add_contact(self, name, phone, comment=''):
        contact_id = len(self.contacts) + 1
        new_contact = Contact(contact_id, name, phone, comment)
        self.contacts.append(new_contact)
        self.save_contacts()

    def find_contact(self, search_term):
        return [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone or search_term in contact.comment]

    def update_contact(self, contact_id, name, phone, comment=''):
        for contact in self.contacts:
            if contact.id == contact_id:
                contact.name = name
                contact.phone = phone
                contact.comment = comment
                self.save_contacts()
                return
        raise ContactNotFoundError("Контакт не найден.")

    def delete_contact(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact.id != contact_id]
        self.save_contacts()
