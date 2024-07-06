# Konstans
# Konstansokat nagybetűvel szokás írni
# Konstansokat nem szabad módosítani és nem is lehet módosítani
# Konstansokat a program elején szokás definiálni
# Pythonban nincs külön konstans típus.


def const(func):
    name = func.__name__
    value = func()

    class ConstWrapper:
        _const_error = TypeError(f"Cannot modify constant '{name}'")

        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            raise self._const_error

    wrapper = ConstWrapper(value)

    globals()[name] = wrapper  # Konstanst létrehozása a globális névtérben

    return wrapper


@const
def NUM():
    return 10


print(NUM.value)  # Outputs: 10

# Attempt to reassign the constant will raise an error
try:
    NUM.value = 20
except TypeError as e:
    print(e)  # Outputs: Cannot modify constant 'NUM'


@const
def CAR_INFO():
    return {"brand": "Ford", "model": "Mustang"}


print(CAR_INFO.value)

# Attempt to reassign the constant will raise an error
try:
    CAR_INFO.value = {"brand": "Toyota", "model": "Corolla"}
except TypeError as e:
    print(e)
