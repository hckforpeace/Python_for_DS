from S1E9 import Character


class Baratheon(Character):
    """Character Baratheon"""

    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    """Character Lannister"""

    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """Creates a Lannister Character"""
        return Lannister(first_name, is_alive)
