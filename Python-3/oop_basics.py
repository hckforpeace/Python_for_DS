"""
OOP Basics in Python: Constructors, Inheritance, and Abstract Classes
"""

# ============================================================================
# 1. CONSTRUCTORS (__init__)
# ============================================================================

class Person:
    """Basic class demonstrating constructor usage"""
    
    def __init__(self, name, age):
        """Constructor method - called when creating an instance"""
        self.name = name  # Instance attribute
        self.age = age
        print(f"Person created: {name}")
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"


# Creating instances
print("=" * 50)
print("1. CONSTRUCTORS")
print("=" * 50)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(person1.introduce())
print(person2.introduce())
print()


# ============================================================================
# 2. INHERITANCE
# ============================================================================

class Animal:
    """Base/Parent class"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Derived/Child class inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return "Woof! Woof!"
    
    # Additional method specific to Dog
    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    """Another derived class"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture!"


print("=" * 50)
print("2. INHERITANCE")
print("=" * 50)
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())  # Inherited method
print(dog.make_sound())  # Overridden method
print(dog.fetch())  # Dog-specific method
print()
print(cat.info())
print(cat.make_sound())
print(cat.scratch())
print()


# ============================================================================
# 3. ABSTRACT CLASSES
# ============================================================================

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class - cannot be instantiated directly"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Another abstract method"""
        pass
    
    # Concrete method (can be used as-is by subclasses)
    def describe(self):
        return f"I am a {self.color} {self.__class__.__name__}"


class Rectangle(Shape):
    """Concrete class implementing abstract methods"""
    
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Another concrete class"""
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


print("=" * 50)
print("3. ABSTRACT CLASSES")
print("=" * 50)

# This would raise an error:
# shape = Shape("red")  # TypeError: Can't instantiate abstract class

rectangle = Rectangle("blue", 5, 3)
circle = Circle("red", 4)

print(rectangle.describe())
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print()
print(circle.describe())
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")
print()


# ============================================================================
# 4. COMBINING ALL CONCEPTS
# ============================================================================

class Vehicle(ABC):
    """Abstract base class with constructor"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Concrete implementation"""
    
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model}: Engine started with a roar!"
    
    def stop_engine(self):
        self.is_running = False
        return f"{self.brand} {self.model}: Engine stopped"


class ElectricCar(Car):
    """Multi-level inheritance"""
    
    def __init__(self, brand, model, year, num_doors, battery_capacity):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity
    
    # Override parent's implementation
    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model}: Silently powered on (Battery: {self.battery_capacity}kWh)"


print("=" * 50)
print("4. COMBINING ALL CONCEPTS")
print("=" * 50)
my_car = Car("Toyota", "Camry", 2022, 4)
tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

print(my_car.get_info())
print(my_car.start_engine())
print()
print(tesla.get_info())
print(tesla.start_engine())
