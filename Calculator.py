import tkinter as tk
from tkinter import messagebox

def get_user_input():
    if gui_mode.get() == 1: # Check if GUI mode is enabled
        weight = weight_entry.get()
        height = height_entry.get()

        try:
            weight = float(weight)
            if weight < 0:
                raise ValueError("Weight cannot be negative.")
        except ValueError:
            messagebox.showerror("Error", "Invalid weight input.")
            return None, None

        try:
            height = float(height)
            if height < 0:
                raise ValueError("Height cannot be negative.")
        except ValueError:
            messagebox.showerror("Error", "Invalid height input.")
            return None, None

        return weight, height
    else: # Command-line mode
        while True:
            try:
                weight = float(input("Enter your weight (in kg): "))
                if weight < 0:
                    raise ValueError("Weight cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid weight.")
                continue

            try:
                height = float(input("Enter your height (in meters): "))
                if height < 0:
                    raise ValueError("Height cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid height.")
                continue

            return weight, height

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def display_result(bmi, category):
    if gui_mode.get() == 1: # Check if GUI mode is enabled
        result_label.config(text=f"Your BMI is {bmi:.2f}. You are classified as {category}.")
    else: # Command-line mode
        print(f"Your BMI is {bmi:.2f}. You are classified as {category}.")

def calculate_and_display():
    weight, height = get_user_input()
    if weight is not None and height is not None:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        display_result(bmi, category)

app = tk.Tk()
app.title("BMI Calculator")

weight_label = tk.Label(app, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(app)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(app, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(app)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(app, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2)

gui_mode = tk.IntVar() # Variable to track GUI mode
checkbox = tk.Checkbutton(app, text="Enable GUI Mode", variable=gui_mode)
checkbox.grid(row=4, column=0, columnspan=2)

app.mainloop()

