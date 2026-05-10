# Copied from Day03 and edited by Aditya Barman; May 09, 2026 @weizmann
# calculating translational partition function using command line

import sys
from Calc_q_trans_library import calc_q_trans

if len(sys.argv) < 5:
    print(f"Please, check the readme file to run properly! and tey again")
else:
    m = sys.argv[1]
    TC = sys.argv[2]
    T = sys.argv[3]
    V = sys.argv[4]
    q_trans, error = calc_q_trans(m, TC, T, V)
    if error:
        print(error)
    else:
        print(f"The value of translational partition function is {q_trans:.2e}")
