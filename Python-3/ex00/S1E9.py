from abc import ABC, abstractmethod


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


# your code here
class Stark(Character):
    """Class Stark"""

    # your code here

    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor of the child class Stark"""
        super().__init__(first_name, is_alive)
