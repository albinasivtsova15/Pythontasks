#Задание 1:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, identifier, p1, p2, p3):
        self.identifier = identifier
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def move(self, dx, dy):
        self.p1.x += dx
        self.p1.y += dy
        self.p2.x += dx
        self.p2.y += dy
        self.p3.x += dx
        self.p3.y += dy

    def is_intersect(self, t2):
        return self._check_intersection(self.p1, self.p2, self.p3, t2.p1, t2.p2, t2.p3, t2.p4)

    def _check_intersection(self, p1, p2, p3, q1, q2, q3, q4):
        def sign(p1, p2, p3):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        def intersect(p1, q1, q2):
            return (sign(p1, q1, q2) < 0) != (sign(p2, q1, q2) < 0) and (sign(p1, p2, q1) < 0) != (sign(p1, p2, q2) < 0)

        if intersect(p1, q1, q2) or intersect(p2, q1, q2) or intersect(p3, q1, q2):
            return True
        if intersect(q1, p1, p2) or intersect(q2, p1, p2) or intersect(q3, p1, p2) or intersect(q4, p1, p2):
            return True
        return False

class Pentagon:
    def __init__(self, identifier, p1, p2, p3, p4, p5):
        self.identifier = identifier
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5

    def move(self, dx, dy):
        self.p1.x += dx
        self.p1.y += dy
        self.p2.x += dx
        self.p2.y += dy
        self.p3.x += dx
        self.p3.y += dy
        self.p4.x += dx
        self.p4.y += dy
        self.p5.x += dx
        self.p5.y += dy

    def is_intersect(self, t1):
        return t1.is_intersect(self)

# Пример использования:
p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(0, 4)

triangle = Triangle("triangle_1", p1, p2, p3)
dx, dy = 2, 3
triangle.move(dx, dy)
print(f"Треугольник был перемещен на расстояние ({dx}, {dy}).")

p4 = Point(1, 1)
p5 = Point(5, 1)
p6 = Point(5, 5)
p7 = Point(1, 5)
p8 = Point(3.5, 3.5)

pentagon = Pentagon("pentagon_1", p4, p5, p6, p7, p8)
dx, dy = -1.5, 0.5
pentagon.move(dx, dy)
print(f"Пятиугольник был перемещен на расстояние ({dx}, {dy}).")

if triangle.is_intersect(pentagon):
    print("Объекты пересекаются.")
else:
    print("Объекты не пересекаются.")
