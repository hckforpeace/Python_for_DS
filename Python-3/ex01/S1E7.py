from S1E9 import Character


class Baratheon(Character):
    """Character Baratheon"""

    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, "Baratheon", "brown", "dark", is_alive)


class Lannister(Character):
    """Character Lannister"""

    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, "Lannister", "blue", "light", is_alive)
        # self.eyes = "blue"
        # self.hair = "light"

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """Creates a Lannister Character"""
        return Lannister(first_name, is_alive)
