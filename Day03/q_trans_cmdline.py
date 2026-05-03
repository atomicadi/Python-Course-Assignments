! Writtenn by Aditya Barman; May 03, 2026 @weizmann

import sys
from Calc_q_trans_library import calc_q_trans

if len(sys.argv) < 4:
    print(f"Please, check the readme file to run properly! and tey again")
else:
    m = sys.argv[1]
    T = sys.argv[2]
    V = sys.argv[3]
    q_trans, error = calc_q_trans(m, T, V)
    if error:
        print(error)
    else:
        print(f"The value of translational partition function is {q_trans:.2e}")
