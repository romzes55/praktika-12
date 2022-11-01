#Создайте метод, который возвращает атрибуты прямоугольника
#как строку ( постарайтесь применить магический метод __str__). Для
#объекта прямоугольника со значениями атрибута a = 5, b = 10, c = 50, d = 100
#метод должен вернуть строку Rectangle : 5, 10, 50, 100.
# Найти площадь прямоугольника

class Rect:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f'Rect: {self.a}, {self.b}, {self.c}, {self.d}'
    def get_area(self):
       return self.a * self.b

rect_1=Rect(5,10,50,100)
print(rect_1, "Площадь прямоугольника", rect_1.get_area())