import tkinter as tk
from tkinter import ttk

# Function to estimate pH
def estimate_ph(color, smell, taste, temperature):
    ph = 7.0  # Start at neutral

    # Color-based adjustment
    if color == "Clear":
        ph += 0
    elif color == "Blue":
        ph += 1
    elif color == "Yellow":
        ph -= 1
    elif color == "Brown":
        ph -= 2
    elif color == "Black":
        ph -= 3
    elif color == "White":
        ph += 0.5

    # Smell-based adjustment
    if smell == "None":
        ph += 0
    elif smell == "Chlorine":
        ph += 1
    elif smell == "Rotten Egg":
        ph -= 2
    elif smell == "Sewage":
        ph -= 3
    elif smell == "Metallic":
        ph += 0.5

    # Taste-based adjustment
    if taste == "None":
        ph += 0
    elif taste == "Salty":
        ph += 1.5
    elif taste == "Sour":
        ph -= 2
    elif taste == "Bitter":
        ph -= 1.5
    elif taste == "Sweet":
        ph += 2

    # Temperature-based adjustment
    if temperature < 10:
        ph -= 0.5
    elif 10 <= temperature <= 25:
        ph += 0
    elif 26 <= temperature <= 35:
        ph += 0.5
    else:
        ph += 1

    # Clamp between 0 and 14
    return round(min(max(ph, 0), 14), 1)

# Function to classify condition
def classify_ph(ph):
    if ph < 6.5:
        return "❌ Acidic and Unsafe", "red"
    elif 6.5 <= ph <= 8.5:
        return " ✅Neutral and Safe", "green"
    else:
        return " ❌ Alkaline and Unsafe", "blue"

# Button callback
def check_ph():
    color = color_var.get()
    smell = smell_var.get()
    taste = taste_var.get()

    try:
        temperature = float(temp_entry.get())
    except ValueError:
        result_label.config(text="❌ Enter a valid temperature!", fg="red")
        return

    ph = estimate_ph(color, smell, taste, temperature)
    condition, color_code = classify_ph(ph)
    result_label.config(text=f"Estimated pH: {ph}\nWater Condition: {condition}", fg=color_code)

# GUI Setup
root = tk.Tk()
root.title("Tap Water pH Checker")
root.geometry("400x300")
root.resizable(False, False)

# Color
tk.Label(root, text="Water Color:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
color_var = ttk.Combobox(root, values=["Clear", "Blue", "Yellow", "Brown", "Black", "White"])
color_var.grid(row=0, column=1)

# Smell
tk.Label(root, text="Water Smell:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
smell_var = ttk.Combobox(root, values=["None", "Chlorine", "Rotten Egg", "Sewage", "Metallic"])
smell_var.grid(row=1, column=1)

# Taste
tk.Label(root, text="Water Taste:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
taste_var = ttk.Combobox(root, values=["None", "Salty", "Sour", "Bitter", "Sweet"])
taste_var.grid(row=2, column=1)

# Temperature
tk.Label(root, text="Water Temperature (°C):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
temp_entry = tk.Entry(root)
temp_entry.grid(row=3, column=1)

# Button to Check
tk.Button(root, text="Check pH", command=check_ph).grid(row=4, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2)

# Start the app
root.mainloop()