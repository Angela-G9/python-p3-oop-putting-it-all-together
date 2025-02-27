class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition

    # Property for size with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    # Method to repair the shoe
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")