# Day 03:
This assignment is the continuation of Day 02, in which the translational partition function (q<sub>trans</sub>) is calculated using 3 different interfaces using puthon:
1. User input directly (using ```input()``` function)
2. Graphical User Interface (GUI) using (using ```tkinter```)
3. Command-line (using ```sys.argv```)

After coping the file "q_trand-Aditya_Barman.py" from Day02 folder into Day03, renamed it by "Calc_q_trans_library.py" and make it bussiness logic file. In the logic file scipy external library is used to gater the constants that are employed in the calculations.

## 1. User input directly
For user input, nothing has been changed more from the Day02's q_trand-Aditya_Barman.py file, just used as defination (```def```), add error messeges, used the logic file, and saved as a new seperate file (q_trans_input).
Command line to run the file:
```sh
python q_trans_input.py
```

## 2. Graphical User Interface (GUI)
For the Graphical User Interface, external ```tkinter``` library is used to set up the graphics for the calculations. The file is saved as "q_trans_gui.py".
Command line to run the file:
```sh
python q_trans_gui.py
```

## 3. Command-line
For the calculation cmmand line, external ```sys.argv``` library is employed where with the prohram file the user inputs are also provided. The file is saved as "q_trans_cmdline.py".
Command line to run the file:
```sh
python q_trans_cmdline.py
```

**pytest**\\
Also a test file (test_calculate_q_trans.py) is generated which will check the code using the python tool ```pytest```.
Command line to run the file:
```sh
pytest test_calculate_q_trans.py
```
