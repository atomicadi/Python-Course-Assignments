# Written and edited by Aditya Barman, Date: May 24, 2026; @Weizmann
# Checking the closer value bw DFT and composite methods

import pandas as pd

df = pd.read_excel("enthalpy_dataset.xlsx")
index_col = df.columns[0]
stoicho_col = df.columns[1]
B3LYP_col = df.columns[2]
G4MP2_col = df.columns[3]
G4_col = df.columns[4]
CBS_QBS_col = df.columns[5]


df["diff_B3LYP_frm_G4MP2"] = df[B3LYP_col] - df[G4MP2_col]
df["diff_B3LYP_frm_G4"] = df[B3LYP_col] - df[G4_col]
df["diff_B3LYP_frm_CBS_QBS"] = df[B3LYP_col] - df[CBS_QBS_col]


cols_to_keep = [
    index_col, stoicho_col, B3LYP_col,
    G4MP2_col, G4_col, CBS_QBS_col
]

cond_G4MP2 = (
    (df["diff_B3LYP_frm_G4MP2"].abs() < df["diff_B3LYP_frm_G4"].abs()) &
    (df["diff_B3LYP_frm_G4MP2"].abs() < df["diff_B3LYP_frm_CBS_QBS"].abs())
)

cond_G4 = (
    (df["diff_B3LYP_frm_G4"].abs() < df["diff_B3LYP_frm_G4MP2"].abs()) &
    (df["diff_B3LYP_frm_G4"].abs() < df["diff_B3LYP_frm_CBS_QBS"].abs())
)

cond_CBS = (
    (df["diff_B3LYP_frm_CBS_QBS"].abs() < df["diff_B3LYP_frm_G4MP2"].abs()) &
    (df["diff_B3LYP_frm_CBS_QBS"].abs() < df["diff_B3LYP_frm_G4"].abs())
)

output_G4MP2 = df.loc[cond_G4MP2, cols_to_keep]
output_G4 = df.loc[cond_G4, cols_to_keep]
output_CBS = df.loc[cond_CBS, cols_to_keep]

output_G4MP2.to_excel("output_G4MP2.xlsx", index=False)
output_G4.to_excel("output_G4.xlsx", index=False)
output_CBS.to_excel("output_CBS_QBS.xlsx", index=False)

print("Normal termination")
