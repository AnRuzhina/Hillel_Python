# person.py
from datetime import datetime


class Person:
    def __init__(self, first_name, last_name='', middle_name='', birth_date='', death_date=None, gender=''):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender

    @staticmethod
    def parse_date(date_string):
        """Парсинг дати з кількох форматів."""
        if not date_string:
            return None
        for fmt in ('%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y', '%d %m %Y'):
            try:
                return datetime.strptime(date_string, fmt)
            except ValueError:
                continue
        raise ValueError(f"Неправильний формат дати: {date_string}")

    @property
    def age(self):
        """Розрахунок віку людини на основі дати народження та дати смерті або поточної дати."""
        if not self.birth_date:
            return None
        end_date = self.death_date if self.death_date else datetime.now()
        age = end_date.year - self.birth_date.year - (
                (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def to_dict(self):
        """Перетворення об'єкта Person на словник для серіалізації."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'birth_date': self.birth_date.strftime('%d.%m.%Y') if self.birth_date else None,
            'death_date': self.death_date.strftime('%d.%m.%Y') if self.death_date else None,
            'gender': self.gender
        }

    def __str__(self):
        """Виведення інформації про людину."""
        gender_description = 'чоловік' if self.gender == 'm' else 'жінка'
        birth_description = "Народився" if self.gender == 'm' else "Народилася"
        death_description = "Помер" if self.gender == 'm' else "Померла"

        # Format death_info only if death_date exists
        death_info = f"{death_description}: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ''

        # Add middle name if it exists
        middle_name_info = f"{self.middle_name} " if self.middle_name else ''

        # Calculate age if birth_date exists
        age_info = f", {self.age} років" if self.age is not None else ""

        # Return the complete string representation
        return (
            f"{self.first_name} {middle_name_info} {self.last_name} {age_info}, {gender_description}."
            f"{birth_description}:"
            f"{self.birth_date.strftime('%d.%m.%Y')}.{death_info}")

    def matches(self, search_str):
        """Перевірка на відповідність пошуковому запиту."""
        full_name = f"{self.first_name} {self.middle_name} {self.last_name}".lower()
        return search_str.lower() in full_name
