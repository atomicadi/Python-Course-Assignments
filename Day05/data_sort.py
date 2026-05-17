# Written and edited by Aditya Barman, Date: May 17, 2026; @Weizmann
# Checking the high correlation energy in the molecules


import pandas as pd

df = pd.read_excel("W4-08_q-contri-dataset_Barman.xlsx")
species_col = df.columns[0]
value_col = df.columns[3]

highest = df[value_col].max()
lowest = df[value_col].min()
average = df[value_col].mean()

thres_val = average + 0.5

selected = df[
    (df[value_col] >= thres_val) &
    (df[value_col] <= highest)
]

output = selected[[species_col, value_col]]

output.to_excel("output_static_correlation.xlsx", index=False)

print("Normal termination")