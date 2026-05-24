# Day06
This dataset contains enthalpies of atomization for 100 randomly selected molecules from the GDB9 molecular database, calculated using different electronic structure methods: DFT/B3LYP/6-31G(2df,p), G4MP2, G4, and CBS-QB3. The purpose of the study is to compare the accuracy and agreement of these computational chemistry methods in predicting molecular energies. B3LYP is a density functional theory (DFT) method that is computationally efficient, while G4MP2, G4, and CBS-QB3 are higher-level composite methods that generally provide more accurate results but require significantly greater computational cost. By comparing the differences between the calculated enthalpies, one can analyze which high-level method most closely matches the DFT results and evaluate the reliability of DFT for predicting thermochemical properties of molecules.

## 1. Requirement(s)
1. For handeling the large dataset, "pandas" library is used here. One can install that using "pip":\
```pip install pandas```
2. Here, the dataset is in Excel format and output is also generated as Excel datasheet. To, read/write Excel dataset, "openpyxl" library is used. One can install that using "pip":\
```pip install openpyxl``` 
