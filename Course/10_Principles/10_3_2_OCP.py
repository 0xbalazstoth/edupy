from abc import ABC, abstractmethod

# Open/Closed Principle (OCP) - Nyitott/zárt elv
# - Egy osztály legyen nyitott a bővítésre, de zárt a módosításra.
# - Új alosztályt vagy egy új metódust felvehetünk, de meglévőt nem írhatunk felül.


# Bad practice
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    # @abstractmethod # Ezt a metódust hozzáadva már nem felel meg az OCP-nek, mert módosítottuk a Shape osztályt.
    # def perimeter(self):
    #     pass


class Circle(Shape):
    def draw(self):
        print("Drawing circle")

    def area(self):
        print("Calculating area of circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing rectangle")

    def area(self):
        print("Calculating area of rectangle")


circle = Circle()
rectangle = Rectangle()

circle.draw()
circle.area()

rectangle.draw()
rectangle.area()


# Javított változat
class PerimeterMixin(ABC):
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape, PerimeterMixin):
    def draw(self):
        print("Drawing circle")

    def area(self):
        print("Calculating area of circle")

    def perimeter(self):
        print("Calculating perimeter of circle")


class Rectangle(Shape, PerimeterMixin):
    def draw(self):
        print("Drawing rectangle")

    def area(self):
        print("Calculating area of rectangle")

    def perimeter(self):
        print("Calculating perimeter of rectangle")


circle = Circle()
rectangle = Rectangle()

circle.draw()
circle.area()
circle.perimeter()

rectangle.draw()
rectangle.area()
rectangle.perimeter()

# A Shape osztályt nem módosítottuk, csak bővítettük a PerimeterMixin osztállyal, így megfelel az OCP-nek.
