class User:
    """A simple attempt to model a User"""

    def __init__(self, first, last):
        """Initialize attributes to describe a User."""
        self.first = first
        self.last = last

    def get_full_name(self):
        return f"{self.first} {self.last}"
