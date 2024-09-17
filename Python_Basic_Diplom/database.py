# database.py
import json
from person import Person


class Database:
    def __init__(self):
        self.people = []

    def load_from_file(self, filename):
        """Завантаження даних з файлу."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.people = [Person(**person) for person in data]
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        except json.JSONDecodeError:
            print("Помилка читання файлу JSON.")

    def save_to_file(self, filename):
        """Збереження даних у файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([person.to_dict() for person in self.people], file, ensure_ascii=False, indent=4)

    def add_person(self, person):
        """Додати нову людину до бази даних."""
        self.people.append(person)

    def search_people(self, search_str):
        """Пошук людей по рядку."""
        return [person for person in self.people if person.matches(search_str)]

    def __str__(self):
        """Виведення всіх записів у базі даних."""
        return "\n".join(str(person) for person in self.people)
