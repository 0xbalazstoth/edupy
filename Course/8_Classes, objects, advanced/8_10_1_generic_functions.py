# Generikusság
# Egy általános osztályt hozhatunk létre, amelyet később különböző típusokkal használhatunk.
# A generikusok segítségével a kód újrafelhasználható és biztonságosabb.

from typing import List, TypeVar

T = TypeVar("T")  # T: bármilyen típus


def get_last_item(items: List[T]) -> T:
    return items[-1]


numbers = [1, 2, 3]
print(get_last_item(numbers))

fruits = ["apple", "banana", "cherry"]
print(get_last_item(fruits))
