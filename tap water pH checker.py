import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to estimate pH based on input
def estimate_ph(color, smell, taste, temperature):
    ph = 7.0

    # Color-based adjustment
    if color == "Clear":
        ph += 0
    elif color == "Blue":
        ph += 1
    elif color == "Yellow":
        ph -= 1
    elif color == "Slightly Brown":
        ph -= 1.5
    elif color == "Dark":
        ph -= 2
    elif color == "Muddy":
        ph -= 2.5

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

    return round(min(max(ph, 0), 14), 1)

# Classify and return condition and color
def classify_ph(ph):
    if ph < 6.5:
        return "Acidic and Unsafe", "red"
    elif 6.5 <= ph <= 8.5:
        return "Neutral and Safe", "green"
    else:
        return "Alkaline and Unsafe", "blue"

# Plot graph function
def plot_ph_graph(ph_value):
    fig, ax = plt.subplots(figsize=(6, 1))
    colors = ['red'] * 65 + ['green'] * 21 + ['blue'] * 50

    for i in range(len(colors)):
        ax.bar(i / 10, 1, width=0.1, color=colors[i], align='edge')

    ax.axvline(ph_value, color='black', linewidth=2, label=f"Your pH: {ph_value}")
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.legend(loc='upper center')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

# Main logic on button click
def check_ph():
    color = color_var.get()
    smell = smell_var.get()
    taste = taste_var.get()
    try:
        temperature = float(temp_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid temperature.", fg="black")
        return

    ph = estimate_ph(color, smell, taste, temperature)
    condition, color_code = classify_ph(ph)

    result_label.config(text=f"Estimated pH: {ph}\nWater Condition: {condition}", fg=color_code)
    plot_ph_graph(ph)

# --- GUI Setup ---
root = tk.Tk()
root.title("Tap Water pH Checker")
root.geometry("750x600")

# Style
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)

# Title
tk.Label(root, text="Tap Water pH Checker", font=("Helvetica", 18, "bold"), fg="blue").pack(pady=10)

# Input Frame
group = ttk.LabelFrame(root, text="Enter Water Properties")
group.pack(padx=10, pady=10, fill="x")

# Water Color
ttk.Label(group, text="Water Color:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
color_var = tk.StringVar()
color_combo = ttk.Combobox(group, textvariable=color_var, width=30)
color_combo['values'] = ["Clear", "Blue", "Yellow", "Slightly Brown", "Dark", "Muddy"]
color_combo.grid(row=0, column=1, padx=5, pady=5)

# Water Smell
ttk.Label(group, text="Water Smell:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
smell_var = tk.StringVar()
smell_combo = ttk.Combobox(group, textvariable=smell_var, width=30)
smell_combo['values'] = ["None", "Chlorine", "Rotten Egg", "Sewage", "Metallic"]
smell_combo.grid(row=1, column=1, padx=5, pady=5)

# Water Taste
ttk.Label(group, text="Water Taste:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
taste_var = tk.StringVar()
taste_combo = ttk.Combobox(group, textvariable=taste_var, width=30)
taste_combo['values'] = ["None", "Salty", "Sour", "Bitter", "Sweet"]
taste_combo.grid(row=2, column=1, padx=5, pady=5)

# Temperature
ttk.Label(group, text="Temperature (°C):").grid(row=3, column=0, padx=5, pady=5, sticky='w')
temp_entry = tk.Entry(group, width=33)
temp_entry.grid(row=3, column=1, padx=5, pady=5)

# Check Button
ttk.Button(root, text="Check pH", command=check_ph).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start GUI
root.mainloop()
