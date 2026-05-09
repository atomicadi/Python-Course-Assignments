# copied from Day03 and edited by Aditya Barman, Date: May 09, 2026; @weizmann
# calculating translational partition function

def calc_q_trans(m, TC, T, V):
    import math
    from scipy import constants

    h = constants.h
    k_B = constants.k

    if not m.isdigit():
        return None, "Oops! you have given either wrong mass or negative mass!"
    else:
        m = int(m)
    
    if not TC.isdigit():
        return None, "Oops! you have given either wrong temperature checker or negative temperature checker!"
    else:
        TC = int(TC)

    if not T.isdigit():
        return None, "Oops! you have given either wrong temperature or negative temperature!"
    else:
        T = int(T)

    if not V.isdigit():
        return None, "Oops! you have given either wrong volume or negative volume!"
    else:
        V = int(V)

    if TC = 0:
        T = T + 273.15
    elif TC = 1:
        T = (T + 459.67)/1.8
    else:
        T = T

    q_trans = ((2 * math.pi * m * k_B * T) / h**2)**(3/2) * V

    return q_trans, None
