import tkinter as tk

def calculate_interest():
    try:
        # Get values from entry widgets
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())
        
        interest = (p * r * t) / 100
        result_label.config(text=f"Interest: {interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

# Principal Input
tk.Label(root, text="Principal:").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

# Rate Input (Was missing in your original snippet)
tk.Label(root, text="Rate (%):").grid(row=1, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

# Time Input (Was missing in your original snippet)
tk.Label(root, text="Time (years):").grid(row=2, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

# Action Buttons and Results
tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, column=1)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1)

root.mainloop()
