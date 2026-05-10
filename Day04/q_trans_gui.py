# Copied from Day03 and edited by Aditya Barman; May 09, 2026 @weizmann
# calculating translational partition function using GUI


import tkinter as tk
from tkinter import messagebox
from Calc_q_trans_library import calc_q_trans

def run_calc():
    m = entry.get()
    TC = entry.get()
    T = entry.get()
    V = entry.get()
    q_trans, error = calc_q_trans(m, TC, T, V)
    if error:
        messagebox.showerror("Error", error)
    else:
        label_res.config(text=f"The value of translational partition function is {q_trans:.2e}")

root = tk.Tk()
root.title("Calculating Translational Partition function")
root.geometry("800x400")

tk.Label(root, text="Enter m  in kg:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Enter TC: if temperature is in Degree Celsius, put 0, if temperature is in Fahrenheit, put 1, and if temperature is in Kelvin, put 3:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Enter T  in your chosen unit:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Enter V  in m3 (if no V, put 1):").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=run_calc).pack(pady=10)
label_res = tk.Label(root, text="")
label_res.pack(pady=5)

root.mainloop()
