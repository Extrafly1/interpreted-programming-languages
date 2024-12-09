# Синьков Д В, Вариант 11, лр 9
# Задание 1. Написать программу, демонстрирующую работу с объектами двух типов T1 и T2,
# для чего создать систему соответствующих классов. Каждый объект должен иметь
# идентификатор (в виде произвольной строки символов) и одно или несколько полей для
# хранения состояния (текущего значения) объекта.
# Перечень типов объектов:
# Квадрат (Quad),
# Прямоугольник (Rectangle).
# Перечень дополнительных методов:
# - compare(T1 t1, T2 t2) сравнение объектов по площади.
# - is_intersect(T1 t1, T2 t2) определяет факт пересечения объектов.
# Задание по варианту:
#   T1         T2    методы
#   Rectangle  Quad  is_intersect, compare
# Задание 2. Необходимо предусмотреть генерацию и обработку исключений для
# возможных ошибочных ситуаций.

class ShapeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Rectangle:
    def __init__(self, identifier, width, height, x=0, y=0):
        if width <= 0 or height <= 0:
            raise ShapeError("Ширина и высота должны быть положительными.")
        self.identifier = identifier
        self.width = width
        self.height = height
        self.x = x  # Положение по X
        self.y = y  # Положение по Y

    def area(self):
        return self.width * self.height

    def is_intersect(self, quad):
        # Проверка пересечения прямоугольника и квадрата
        return (self.x < quad.x + quad.side_length and
                self.x + self.width > quad.x and
                self.y < quad.y + quad.side_length and
                self.y + self.height > quad.y)

class Quad:
    def __init__(self, identifier, side_length, x=0, y=0):
        if side_length <= 0:
            raise ShapeError("Длина стороны должна быть положительной.")
        self.identifier = identifier
        self.side_length = side_length
        self.x = x  # Положение по X
        self.y = y  # Положение по Y

    def area(self):
        return self.side_length ** 2

    def is_intersect(self, rectangle):
        # Проверка пересечения квадрата и прямоугольника
        return (self.x < rectangle.x + rectangle.width and
                self.x + self.side_length > rectangle.x and
                self.y < rectangle.y + rectangle.height and
                self.y + self.side_length > rectangle.y)

def compare(shape1, shape2):
    """Сравнение двух фигур по площади."""
    area1 = shape1.area()
    area2 = shape2.area()
    if area1 > area2:
        return f"{shape1.identifier} больше {shape2.identifier}."
    elif area1 < area2:
        return f"{shape2.identifier} больше {shape1.identifier}."
    else:
        return "Площади равны."

try:
    rectangle = Rectangle("Rect1", 4, 5, x=1, y=1)
    quad = Quad("Quad1", 3, x=2, y=2)

    print(f"Площадь прямоугольника: {rectangle.area()}")
    print(f"Площадь квадрата: {quad.area()}")

    # Сравнение площадей
    print(compare(rectangle, quad))

    # Проверка на пересечение
    if rectangle.is_intersect(quad):
        print(f"{rectangle.identifier} и {quad.identifier} пересекаются.")
    else:
        print(f"{rectangle.identifier} и {quad.identifier} не пересекаются.")

except ShapeError as e:
    print(f"Ошибка: {e}")
