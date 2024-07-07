# Statikus metódus
# - A statikus metódusokat a @staticmethod dekorátorral jelöljük.
# - A statikus metódusok nem férnek hozzá az osztály példányváltozóihoz és metódusaihoz.
# - A statikus metódusokat az osztály neve segítségével érjük el.
# - Példányosítás nélkül is hívhatóak.


class Nationality:
    def __init__(self, name: str, language: str):
        self.name = name
        self.language = language

    @staticmethod
    def speak(language: str) -> str:
        if language == "Hungarian":
            return "Szia!"
        elif language == "English":
            return "Hello!"
        elif language == "German":
            return "Hallo!"
        else:
            return "I don't know this language."


hungarian = Nationality.speak("Hungarian")
print(hungarian)

english = Nationality.speak("English")
print(english)

german = Nationality.speak("German")
print(german)

unknown = Nationality.speak("French")
print(unknown)
