import sys
from Calc_q_trans_library import q_trans

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <put your sequence here>")
    print(f"Example: python {sys.argv[0]} GATCGATCGATCGATCGATC")
else:
    seq = sys.argv[1]
    result, error = calculate_tm(seq)
    if error:
        print(error)
    else:
        print(f"Tm: {result['tm']:.2f}°C using {result['method']}")
