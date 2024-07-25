from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.__is_valid(value):
            raise ValueError(f'{value} is not a valid phone number')

        super().__init__(value)

    def __is_valid(self, value: str):
        return bool(re.match('^[0-9]{10}$', value))


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def find_phone(self, number: str):
        phones = list(filter(lambda phone: phone.value == number, self.phones))
        if len(phones) == 0:
            return None

        return phones[0]

    def remove_phone(self, number: str):
        phone = self.find_phone(number)
        if phone is not None:
            self.phones.remove(phone)

    def edit_phone(self, number: str, new_number: str):
        phone = self.find_phone(number)
        if phone is not None:
            phone.value = new_number

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name not in self.data:
            return None

        return self.data[name]

    def delete(self, name: str):
        if name not in self.data:
            return

        del self.data[name]
