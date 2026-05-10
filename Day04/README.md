# Day 04:
- This assignment is the continuation of Day 03, in which the translational partition function (q<sub>trans</sub>) is calculated using 3 different interfaces using python like previous with some little interesting changes:
1. User input directly (using ```input()``` function)
2. Graphical User Interface (GUI) using (using ```tkinter```)
3. Command-line (using ```sys.argv```)

After coping the file "q_trand-Aditya_Barman.py" from Day02 folder into Day03, renamed it by "Calc_q_trans_library.py" and make it bussiness logic file. In the logic file scipy external library is used to get the constants that are employed in the calculation.\
In this file a liitle modification is added, that is "Temperature checker" (TC). TC will check the digit given by user and then do a short unit conversion to convert ant temperature in Kelvin using unit conversion formula.

- Kelvin to Degree Celsius:
</p>

$$
K = (x^o C + 273.15)
$$
</p>


## 1. User input directly
For user input, nothing has been changed more from the Day02's q_trand-Aditya_Barman.py file, just used as defination (```def```), added error messeges, used the logic file, and saved as a new seperate file, q_trans_input.py.
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
For the calculation of command line, external ```sys.argv``` library is employed where with the program file the user inputs are also provided. The file is saved as "q_trans_cmdline.py". Fot his interface, one have to put the input values with the script file as mentioned below.\
- Mass in kg unit.
- Temp is in K unit.
- Volume is in m<sup>3</sup> unit, if no Volume, put 1.
Command line to run the file:
```sh
python q_trans_cmdline.py <Mass> <Temp> <Volume>
```

- **Test file**\
Also a test file (test_calculate_q_trans.py) is generated which will check the code using the python tool ```pytest```.
Command line to run the file:
```sh
pytest test_calculate_q_trans.py
```

- **Requirements**
1. Scipy
2. tkinter
3. sys.argv
4. pytest (for my case, installed by ```pip install pytest```)

- **AI Usage**\
Generally, tried to write by myself by observing the previous submissions. But sometimes after writting the code, checked them with AI (ChatGpt, Weizamann Institute subscripted version). Here are the promts, that I used:
```sh
Check the code and debug
how to check digit and alphabate
```
