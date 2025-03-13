import tkinter as tk
from tkinter import messagebox

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x300")

# Number input fields
tk.Label(root, text="Enter first number:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Enter second number:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack()
operation_var = tk.StringVar(value="+")
tk.Radiobutton(root, text="+", variable=operation_var, value="+").pack()
tk.Radiobutton(root, text="-", variable=operation_var, value="-").pack()
tk.Radiobutton(root, text="*", variable=operation_var, value="*").pack()
tk.Radiobutton(root, text="/", variable=operation_var, value="/").pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the GUI application
root.mainloop()
