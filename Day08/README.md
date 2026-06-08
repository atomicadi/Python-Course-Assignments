# Day 04
This assignment is the continuation of Day 04, in which the translational partition function (q<sub>trans</sub>) is calculated using  web application.
 

After coping the file "Calc_q_trans_library.py" from Day04 folder into Day08, renamed it by "**q_trans_logic.py**" and make it bussiness logic file. In the logic file ```scipy``` and ```math``` external libraries are used to get the constants that are employed in the calculation.\
For more details, see the README file of Day04: https://github.com/atomicadi/Python-Course-Assignments/blob/main/Day04/README.md

 
## 1. Web application
For the web application ```flask``` web framework of python is used here. The file is titled "**q_trans_app.py**".

## 2. Test file
Also a test files for both the logic and app webapplication are ("**test_q_trans_logic.py**", "**test_q_trans_app.py**") generated which will check the code using the python tool ```pytest```.

## 3. Requirements
1. Scipy
2. math
3. flask
4. pytest (for my case, installed by ```pip install pytest```)

- a requirement.txt file will be added with the other files in directory.

## 4. AI Usage 
Generally, tried to write by myself by observing the previous submissions. But sometimes after writting the code, checked them with AI (ChatGpt, Weizamann Institute subscripted version). Here are the promts, that I used:
```sh
How to ignore alphabates in inputs and consider only -ve or +ve digits
```

