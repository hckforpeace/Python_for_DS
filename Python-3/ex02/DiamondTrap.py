from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        self.eyes = color

    def set_hairs(self, color) -> None:
        self.hairs = color

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs
