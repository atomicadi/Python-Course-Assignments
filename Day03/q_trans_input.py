from Calc_q_trans_library import calc_q_trans

m = input("put the value of mass in kg unit: ")
T = input("put the value of temperature in K unit: ")
V = input("put the value of volume in cm3 unit: ")

q_trans, error = calc_q_trans(m, T, V)

if error:
          print(error)
else:
   print("The calculated value of translational partition function (using your input) is, ", q_trans)
          

          
