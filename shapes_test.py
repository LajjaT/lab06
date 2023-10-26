import shapes

def test_circle():
    circle = shapes.Circle(4)

    assert abs(circle.get_area() - 50.26548245744) < 0.0001
    assert abs(circle.get_perimeter() - 25.13274122872) < 0.0001

def test_rectangle():
    rect = shapes.Rectangle(3, 5)
    assert abs(rect.get_area() - 15) < 0.0001
    assert abs(rect.get_perimeter() - 16) < 0.0001
