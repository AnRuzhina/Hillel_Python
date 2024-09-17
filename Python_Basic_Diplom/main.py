# main.py
from database import Database
from person import Person


def print_menu():
    print("\nМеню:")
    print("1. Ввести нову людину")
    print("2. Пошук записів")
    print("3. Завантажити з файлу")
    print("4. Зберегти у файл")
    print("5. Показати всі записи")
    print("6. Вийти")


def main():
    db = Database()

    while True:
        print_menu()
        choice = input("Виберіть опцію: ").strip()

        if choice == '1':
            first_name = input("Введіть ім'я: ").strip()
            last_name = input("Введіть прізвище (необов'язково): ").strip()
            middle_name = input("Введіть по-батькові (необов'язково): ").strip()
            birth_date = input("Введіть дату народження (формат: дд.мм.рррр): ").strip()
            death_date = input("Введіть дату смерті (необов'язково, формат: дд.мм.рррр): ").strip()
            gender = input("Введіть стать (m/f): ").strip()

            person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
            db.add_person(person)
            print("Запис додано.")

        elif choice == '2':
            search_str = input("Введіть рядок для пошуку: ").strip()
            results = db.search_people(search_str)
            for person in results:
                print(person)
            if not results:
                print("Нічого не знайдено.")

        elif choice == '3':
            filename = input("Введіть ім'я файлу для завантаження: ").strip()
            db.load_from_file(filename)
            print("Дані завантажено.")

        elif choice == '4':
            filename = input("Введіть ім'я файлу для збереження: ").strip()
            db.save_to_file(filename)
            print("Дані збережено.")

        elif choice == '5':
            print(db)

        elif choice == '6':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
