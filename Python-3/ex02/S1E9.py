from abc import ABC, abstractmethod
from typing import override


class Character(ABC):
    """Class Character"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor of the abstract class Character"""
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kills character"""
        self.is_alive = False

    @override
    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @override
    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Stark(Character):
    """Class Stark"""

    # your code here

    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor of the child class Stark"""
        super().__init__(first_name, is_alive, "brown", "dark", "Stark")
        self.eyes = "brown"
        self.hairs = "dark"
        self.family_name = "Stark"
