# Written and edited by Aditya Barman, Date: May 24, 2026; @Weizmann
# Converting .txt file into .xlsx file

import re
import pandas as pd

rows = []

with open("validation.txt", "r") as file:
    for line in file:
        line = line.strip()

        match = re.match(
            r"^(\d{6})\s+(.+?)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)$",
            line
        )

        if match:
            rows.append(match.groups())

df = pd.DataFrame(rows, columns=[
    "Index",
    "Stoichiometry",
    "B3LYP_6-31G(2df,p)",
    "G4MP2",
    "G4",
    "CBS-QB3"
])

for col in df.columns[2:]:
    df[col] = pd.to_numeric(df[col])

df.to_excel("enthalpy_dataset.xlsx", index=False)

print("Normal Termination")
