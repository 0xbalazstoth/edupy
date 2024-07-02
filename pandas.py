# pip install pandas
# https://github.com/pandas-dev/pandas
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# Pandas: (big data) Adatok analizálására, feldolgozására használatos package

import pandas as pd

# Két fő adatstruktúrával dolgozik:
# 1. DataFrame:
# - Kétdimenziós, táblázatos adatstruktúra, ami sorokból és oszlopokból áll
# 2. Series: Rendezett, egydimenziós tömb adatok egy indexszel.
# - A sorozatban lévő összes adat azonos adattípusúak.

# DataFrame létrehozása
df = pd.DataFrame(
    {"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]}, index=[1, 2, 3]
)  # Értékek rendelése adott oszlophoz
print(df)

df = pd.DataFrame(
    [[4, 7, 10], [5, 8, 11], [6, 9, 12]],
    index=[1, 2, 3],
    columns=["a", "b", "c"],  # Értékek rendelése adott sorhoz
)
print(df)
