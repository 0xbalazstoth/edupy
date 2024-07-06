# Generikusság
# Egy általános osztályt hozhatunk létre, amelyet később különböző típusokkal használhatunk.
# A generikusok segítségével a kód újrafelhasználható és biztonságosabb.

from typing import Generic, List, TypeVar

T = TypeVar("T")  # T: bármilyen típus


class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, items: T):
        self.items.append(items)

    def pop(self) -> T:
        return self.items.pop()


stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())

stack = Stack[str]()
stack.push("Hello")
stack.push("World")
print(stack.pop())
print(stack.pop())
