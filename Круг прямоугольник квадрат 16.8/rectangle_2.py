from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(15,5)

print(rect_1.get_area(), rect_2.get_area())

squar_1=Square(5)
squar_2=Square(7)

print(squar_1.get_square(), squar_2.get_square())

#Переносим все объекты в единую коллекцию

figures = [rect_1, rect_2, squar_1, squar_2]
for i in figures:
    if isinstance(i, Square):
        print("Квадрат", i.get_square())
    else:
        print("Прямоугольник", i.get_area())

circle_1 = Circle(7)
print("Круг", circle_1.get_circle())