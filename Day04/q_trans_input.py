# Copied from Day03 and edited by Aditya Barman; May 09, 2026 @weizmann
# calculating translational partition function using user input

from Calc_q_trans_library import calc_q_trans

m = input("put the value of mass in kg unit: ")
TC = input("Temperature checker, if in Degree Celsius, put 0, if in Fahrenheit, put 1, and if in Kelvin, put 3: ")
T = input("put the value of temperature in your chosen unit: ")
V = input("put the value of volume in m3 unit (if there is no V, put 1): ")

q_trans, error = calc_q_trans(m, TC, T, V)

if error:
          print(error)
else:
   print("The calculated value of translational partition function (using your input) is, ", q_trans)
          

          
