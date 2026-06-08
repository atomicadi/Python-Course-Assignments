# copied from Day04 and edited by Aditya Barman, Date: June 07, 2026; @weizmann
# calculating translational partition function

def calc_q_trans(m, TC, T, V):
    import math
    from scipy import constants

    h = constants.h
    k_B = constants.k

    if not m.replace('.', '', 1).lstrip('+-').isdigit():
        return None, "Oops! you have given either wrong mass or negative mass!"
    else:
        m = float(m)

    if not TC.isdigit():
        return None, "Oops! you have given either wrong temperature checker or negative temperature checker!"
    else:
        TC = int(TC)
        
    if not T.replace('.', '', 1).lstrip('+-').isdigit():
        return None, "Oops! you have given an invalid temperature!"
    else:
        T = float(T)

    if not V.replace('.', '', 1).lstrip('+-').isdigit():
        return None, "Oops! you have given either wrong volume or negative volume!"
    else:
        V = float(V)

    if TC == 0:
        T = T + 273.15
    elif TC == 1:
        T = ((T -32) / 1.8) + 273.15

    q_trans = ((2 * math.pi * m * k_B * T) / h**2)**(3/2) * V

    return q_trans, None