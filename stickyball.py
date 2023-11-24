from ball import Ball


class StickyBall(Ball):
    def __init__(
        self, x: int, y: int, radius: int, color: tuple, special_attribute: str
    ):
        super().__init__(x, y, radius, color)
        self.special_attribute = special_attribute

    def special_method(self):
        print(f"This is a special ball with attribute: {self.special_attribute}")
