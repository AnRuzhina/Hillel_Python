# Виняток користувача


class GroupLimitError(Exception):
    def __init__(self, message="В групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.append(student)

    def delete_student(self, last_name):
        self.group = [student for student in self.group if student.last_name != last_name]

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група {self.number}:\n{all_students}'


st1 = Student('Чоловік', 20, 'Іван', 'Петров', 'AN142')
st2 = Student('Жінка', 21, 'Олена', 'Іванова', 'AN145')
st3 = Student('Чоловік', 19, 'Дмитро', 'Сидоров', 'AN146')
st4 = Student('Жінка', 22, 'Марія', 'Коваль', 'AN147')
st5 = Student('Чоловік', 20, 'Олег', 'Шевченко', 'AN148')
st6 = Student('Жінка', 23, 'Наталя', 'Кузьменко', 'AN149')
st7 = Student('Чоловік', 19, 'Володимир', 'Тарасов', 'AN150')
st8 = Student('Жінка', 20, 'Галина', 'Дмитренко', 'AN151')
st9 = Student('Чоловік', 21, 'Борис', 'Литвин', 'AN152')
st10 = Student('Жінка', 22, 'Світлана', 'Романенко', 'AN153')
st11 = Student('Чоловік', 23, 'Максим', 'Гончар', 'AN154')


group = Group('PD1')

#
try:
    group.add_student(st1)
    group.add_student(st2)
    group.add_student(st3)
    group.add_student(st4)
    group.add_student(st5)
    group.add_student(st6)
    group.add_student(st7)
    group.add_student(st8)
    group.add_student(st9)
    group.add_student(st10)
    group.add_student(st11)
except GroupLimitError as e:
    print(f"Помилка: {e}")


print(group)
