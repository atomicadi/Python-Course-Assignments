# copied from Day02 and edited by Aditya Barman, Date: May. 03, 2026; @weizmann
# calculating translational partition function

def calc_q_trans(m, T, V):
    import math
    from scipy import constants

    h = constants.h
    k_B = constants.k

    if not m.isdigit():
        return None, "Oops! you have given either wrong mass or negative mass!"
    else:
        m = int(m)

    if not T.isdigit():
        return None, "Oops! you have given either wrong temperature or negative temperature!"
    else:
        T = int(T)

    if not V.isdigit():
        return None, "Oops! you have given either wrong volume or negative volume!"
    else:
        V = int(V)

    q_trans = ((2 * math.pi * m * k_B * T) / h**2)**(3/2) * V

    return q_trans, None
