# Day05
In this assignment, a small snapshot (Weizmann-4 (W4)) of a full ESI dataset from a published paper (https://doi.org/10.1021/acs.jpca.6c00467?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) of our group is used. The dataset is stored in an excel sheet and contains the species names (molecules), their Total Atomization Energy (TAE) at CCSDT/cc-pwCVTZ and CCSDT(Q)/cc-pwCVTZ level of throry.
Then the difference between CCSDT(Q)-CCSDT level have been shown which is indicating the (Q) contributions in the different molecules.

For this assignment, the highest (Q) contribution and the lowest contribution are checked and then the average of them is calculated. In the next step, 0.5 is added with average value and considered as thereshold value. So, the (Q) contribution which is lied in between thereshold to highest, considered as highly correlated system (system with high correlation energy).

- **Correlation Energy**\
In quantum chemistry, correlation energy is the difference between the exact nonrelativistic electronic energy and the Hartree–Fock (HF) energy.

Mathematically:

E<sub>_corr_</sub> = E<sub>_exact_</sub>-E<sub>_HF_</sub>

Since the Hartree–Fock method approximates electrons as moving independently in an average field, it misses the instantaneous electron–electron interactions. Correlation energy measures the energy lowering obtained when these interactions are treated more accurately.

## 1. Requirement(s)
1. For handeling the large dataset, "pandas" library is used here. One can install that using "pip":\
```pip install pandas```
2. Here, the dataset is in Excel format and output is also generated as Excel dataset. To, read/write Excel dataset, "openpyxl" library is used. One can install that using "pip":\
```pip install openpyxl```     

## 2. How to run
The excel file (W4-08_q-contri-dataset_Barman.xlsx) and the python script (data_sort.py) should be in same folder. The pyhton script can be run, using:

```python data_sort.py```

It will generate a output file (output_static_correlation.xlsx) that conatins the species with high correlation energy with their (Q) contributions.


## 3. AI usage
The prompt I used for this in ChatGpt (Weizmann Institute subscripted version):\
```I have generated the dataset file and now i want that it will check column 4, fine the highest value and lowest vale, then take the average and add +0.5 with that average and then check if the value is bw average+0.5 to highest then it will open a output and add that species name from column 1 and put that on the output with the coulmn 4 value```
