# Прямокутник

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Обчислює площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Порівнює два прямокутники за площею."""
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        """Додає два прямокутники, створюючи новий з сумарною площею."""
        if isinstance(other, Rectangle):
            total_square = self.get_square() + other.get_square()
            new_width = math.sqrt(total_square)
            new_height = total_square / new_width
            return Rectangle(new_width, new_height)
        raise TypeError("Можна додавати лише інші прямокутники")

    def __mul__(self, n):
        """Множить площу прямокутника на число n."""
        if isinstance(n, (int, float)) and n > 0:
            new_square = self.get_square() * n
            new_width = math.sqrt(new_square)
            new_height = new_square / new_width
            return Rectangle(new_width, new_height)
        raise TypeError("Множення можливе лише на позитивне число")

    def __str__(self):
        """Повертає рядок з інформацією про прямокутник."""
        return f"Rectangle(width={self.width:.2f}, height={self.height:.2f}, square={self.get_square():.2f})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)


assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'


r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'


r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'


assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Всі тести пройдені!")
