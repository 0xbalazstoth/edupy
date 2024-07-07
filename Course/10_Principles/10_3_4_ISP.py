# Interface Segregation Principle (ISP) - Interfészszegregációs elv
# - Az osztályoknak csak azokat a metódusokat kell tartalmazniuk, amelyekre szükségük van.
# - Több specifikus interfész jobb, mint egy nagy általános interfész.
# - Python-ban: Duck typing + ABC = Interfész

from abc import ABC, abstractmethod


# Bad practice
class PrinterInterface(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass


class SimplePrinter(PrinterInterface):
    def print(self):
        print("Printing black and white")

    def scan(self):
        raise NotImplementedError("SimplePrinter does not support scanning")

    def fax(self):
        raise NotImplementedError("SimplePrinter does not support faxing")


class AdvancedPrinter(PrinterInterface):
    def print(self):
        print("Printing with colors")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")


simple_printer = SimplePrinter()
advanced_printer = AdvancedPrinter()

simple_printer.print()

advanced_printer.print()
advanced_printer.scan()
advanced_printer.fax()


# Javított változat
class PrinterFeatureInterface(ABC):
    @abstractmethod
    def print(self):
        pass


class FaxFeatureInterface(ABC):
    @abstractmethod
    def fax(self):
        pass


class ScannerFeatureInterface(ABC):
    @abstractmethod
    def scan(self):
        pass


class SimplePrinter(PrinterFeatureInterface):
    def print(self):
        print("Printing black and white")


class AdvancedPrinter(PrinterFeatureInterface, FaxFeatureInterface):
    def print(self):
        print("Printing with colors")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")


simple_printer = SimplePrinter()
advanced_printer = AdvancedPrinter()

simple_printer.print()

advanced_printer.print()
advanced_printer.scan()
advanced_printer.fax()
