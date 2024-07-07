# Single Responsibility Principle (SRP) - Egységbe zárás elve
# - Egy osztálynak csak egy felelőssége lehet.


# Bad practice
class DataProcessor:
    def read_input(self):
        return [1, 2, 3, 4, 5]

    def modify_data(self, data):
        return [x + 1 for x in data]

    def filter_data(self, data):
        return [x for x in data if x % 2 == 0]

    def write_output(self, data):
        print("Final data:", data)

    def process(self):
        data = self.read_input()
        data = self.modify_data(data)
        data = self.filter_data(data)
        self.write_output(data)


processor = DataProcessor()
processor.process()


# Javított változat
class DataHandler:
    def read_input(self):
        return [1, 2, 3, 4, 5]

    def write_output(self, data):
        print("Final data:", data)


class DataProcessor:
    def modify_data(self, data):
        return [x + 1 for x in data]

    def filter_data(self, data):
        return [x for x in data if x % 2 == 0]


class Controller:
    def __init__(self, handler, processor):
        self.handler = handler
        self.processor = processor

    def process(self):
        data = self.handler.read_input()
        data = self.processor.modify_data(data)
        data = self.processor.filter_data(data)
        self.handler.write_output(data)


# Create instances of each component
handler = DataHandler()
processor = DataProcessor()

# Create and run the controller
controller = Controller(handler, processor)
controller.process()
