# «Правильний дріб»

import math


class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути рівним 0")

        gcd = math.gcd(a, b)
        self.a = a // gcd
        self.b = b // gcd

        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def __add__(self, other):
        """Додавання дробів."""
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Віднімання дробів."""
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Множення дробів."""
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Перевірка на рівність дробів."""
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        """Менше ніж для дробів."""
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        """Більше ніж для дробів."""
        return self.a * other.b > other.a * self.b

    def __str__(self):
        """Строкове представлення дробу."""
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)


f_c = f_a + f_b
assert str(f_c) == 'Fraction: 7, 6', f"Expected 'Fraction: 7, 6', but got {str(f_c)}"


f_d = f_a * f_b
assert str(f_d) == 'Fraction: 1, 3', f"Expected 'Fraction: 1, 3', but got {str(f_d)}"


f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', f"Expected 'Fraction: 1, 6', but got {str(f_e)}"


assert f_d < f_c, "Expected f_d < f_c"
assert f_d > f_e, "Expected f_d > f_e"
assert f_a != f_b, "Expected f_a != f_b"


f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2, "Expected f_1 == f_2"

print('OK')
