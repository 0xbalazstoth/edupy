# Lasagne kód
# - Túl sok absztrakciós réteggel rendelkezik, ami nehezíti az érthetőséget és a karbantarthatóságot.
# Absztrakciós réteg: Az absztrakciós réteg egy olyan réteg, amely elrejti a részleteket, és csak azokat az információkat jeleníti meg,
#                     amelyek szükségesek a felhasználó számára.


class InputReader:
    def read_input(self):
        return [1, 2, 3, 4, 5]


class DataModifier:
    def modify_data(self, data):
        return [x + 1 for x in data]


class DataFilter:
    def filter_data(self, data):
        return [x for x in data if x % 2 == 0]


class OutputWriter:
    def write_output(self, data):
        print("Final data:", data)


class DataProcessingPipeline:
    def __init__(self):
        self.reader = InputReader()
        self.modifier = DataModifier()
        self.filter = DataFilter()
        self.writer = OutputWriter()

    def process(self):
        data = self.reader.read_input()
        data = self.modifier.modify_data(data)
        data = self.filter.filter_data(data)
        self.writer.write_output(data)


pipeline = DataProcessingPipeline()
pipeline.process()


# Javított változat
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
