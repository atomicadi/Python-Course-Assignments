import tkinter as tk
from tkinter import messagebox
from Calc_q_trans_library import calc_q_trans

def run_calc():
    m = entry.get()
    T = entry.get()
    V = entry.get()
    q_trans, error = calc_q_trans(m, T, V)
    if error:
        messagebox.showerror("Error", error)
    else:
        label_res.config(text=f"Tm: {q_trans['tm']:.2f}°C\n({result['method']})")
        
root = tk.Tk()
root.title("Calculating Translational Partition function")
root.geometry("300x200")

tk.Label(root, text="Enter m  in kg:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Enter T  in K:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Enter V  in m3:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=run_calc).pack(pady=10)
label_res = tk.Label(root, text="")
label_res.pack(pady=5)

root.mainloop()
