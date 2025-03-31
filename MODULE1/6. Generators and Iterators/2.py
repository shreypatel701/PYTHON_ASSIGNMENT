class IntegerIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# Example usage
numbers = [10, 20, 30, 40, 50]
iterator = IntegerIterator(numbers)

for num in iterator:
    print(num)
