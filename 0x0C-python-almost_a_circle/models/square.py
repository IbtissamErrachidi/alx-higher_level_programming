#!/usr/bin/python3
"""class Square"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """custom __str__ method for Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates values of the Square instance from args or kwargs"""
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the Square instance"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        pass

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw shapes"""
        pass
