import tkinter as tk

# Create the main window
app = tk.Tk()
app.title("Advanced Grid Layout Example")
app.geometry('400x300')

# Create widgets
label1 = tk.Label(app, text="Label 1", bg="red")
label2 = tk.Label(app, text="Label 2", bg="blue")
label3 = tk.Label(app, text="Label 3", bg="green")
label4 = tk.Label(app, text="Label 4", bg="yellow")
label5 = tk.Label(app, text="Label 5", bg="purple")

# Arrange widgets in the grid
label1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
label2.grid(row=0, column=1, padx=5, pady=5, rowspan=2, sticky="nsew")
label3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
label4.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="nsew")
label5.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Configure column and row weights
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

# Run the application
app.mainloop()

