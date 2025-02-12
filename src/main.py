class DataProcessor:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def get_item(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def process_data(self):
        return [item for item in self.data if item['active']]

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b
