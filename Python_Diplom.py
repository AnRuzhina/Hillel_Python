import datetime
import re
import json


class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.gender = gender

    def parse_date(self, date_str):
        if date_str:
            formats = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]
            for fmt in formats:
                try:
                    return datetime.datetime.strptime(date_str, fmt).date()
                except ValueError:
                    pass
        return None

    def calculate_age(self):
        today = datetime.date.today()
        if self.death_date:
            end_date = self.death_date
        else:
            end_date = today
        if self.birth_date:
            age = end_date.year - self.birth_date.year - (
                        (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None

    def __str__(self):
        age = self.calculate_age()
        gender_str = "чоловік" if self.gender == 'm' else "жінка"
        death_str = f"Помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ""
        return f"{self.first_name} {self.last_name or ''} {self.middle_name or ''} {age} років, {gender_str}. Народився: {self.birth_date.strftime('%d.%m.%Y')}. {death_str}"


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        results = []
        query_lower = query.lower()
        for person in self.people:
            if (query_lower in (person.first_name or '').lower() or
                    query_lower in (person.last_name or '').lower() or
                    query_lower in (person.middle_name or '').lower()):
                results.append(person)
        return results

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([person.__dict__ for person in self.people], file, ensure_ascii=False, default=str)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.people = [Person(**person) for person in data]

    def __str__(self):
        return "\n".join(str(person) for person in self.people)


def main():
    db = Database()
    while True:
        print("1. Додати людину")
        print("2. Пошук людини")
        print("3. Зберегти дані у файл")
        print("4. Завантажити дані з файлу")
        print("5. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            first_name = input("Ім'я: ")
            last_name = input("Прізвище: ")
            middle_name = input("По-батькові: ")
            birth_date = input("Дата народження (дд.мм.рррр): ")
            death_date = input("Дата смерті (дд.мм.рррр) або пропустіть: ")
            gender = input("Стать (m/f): ")
            person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
            db.add_person(person)

        elif choice == '2':
            query = input("Введіть ім'я або прізвище для пошуку: ")
            results = db.search(query)
            if results:
                for person in results:
                    print(person)
            else:
                print("Збігів не знайдено.")

        elif choice == '3':
            filename = input("Введіть ім'я файлу для збереження: ")
            db.save_to_file(filename)
            print("Дані збережено.")

        elif choice == '4':
            filename = input("Введіть ім'я файлу для завантаження: ")
            db.load_from_file(filename)
            print("Дані завантажено.")

        elif choice == '5':
            print("До побачення!")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
