# Mi az a CSV?

- A CSV (Comma-Separated Values) fájl egy egyszerű szöveges fájlformátum, amelyet az adatok tárolására és megosztására használnak.
- Minden sor egy adatrekordot képvisel, és az egyes mezők (oszlopok) vesszővel (vagy más elválasztó karakterrel) vannak elválasztva.

```csv
word,language
apple,English
casa,Spanish
livre,French
```

# Mi az a JSON?

- A JSON (JavaScript Object Notation) egy könnyen olvasható szöveges formátum, amelyet adatstruktúrák és objektumok tárolására és továbbítására használnak.

## JSON objektumok és tömbök

- Egy JSON objektum egy kulcs-érték párokból álló gyűjtemény, ahol a kulcsok stringek, és az értékek lehetnek különböző típusú adatok, mint stringek, számok, boolean értékek, tömbök, vagy akár más objektumok.

```json
{
      "word": "apple",
      "language": "English"
},
```

```json
{
  "words": [
    {
      "word": "apple",
      "language": "English"
    },
    {
      "word": "manzana",
      "language": "Spanish"
    },
    {
      "word": "pomme",
      "language": "French"
    },
    {
      "word": "Apfel",
      "language": "German"
    }
  ]
}
```
