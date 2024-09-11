# main.py
from student import Student
from group import Group, GroupLimitError



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)


print(gr)


assert gr.find_student('Jobs') == st1, 'Test1: Пошук студента Steve Jobs'
assert gr.find_student('Jobs2') is None, 'Test2: Студент не знайдений'


gr.delete_student('Taylor')
print(gr)


try:
    for i in range(11):
        gr.add_student(Student(f'Gender{i}', 20 + i, f'First{i}', f'Last{i}', f'AN{i}'))
except GroupLimitError as e:
    print(e)
