from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def estimate_ph(color, smell, taste, temperature):
    # Set base pH value
    ph = 7.0

    # Color-based adjustment
    if color.lower() == "clear":
        ph += 0
    elif color.lower() == "yellowish":
        ph -= 1
    elif color.lower() == "slightly brown":
        ph -= 2
    
    elif color.lower() == "dark":
        ph -= 3
    elif color.lower() == "muddy":
        ph -= 4
    

    # Smell-based adjustment
    if smell.lower() == "none":
        ph += 0
    elif smell.lower() == "chlorine":
        ph += 1
    elif smell.lower() == "rotten egg":
        ph -= 3
    elif smell.lower() == "sewage":
        ph = 1
    elif smell.lower() == "metallic":
        ph += 0.5

    # Taste-based adjustment
    if taste.lower() == "none":
        ph += 0
    elif taste.lower() == "salty":
        ph += 1.5
    elif taste.lower() == "sour":
        ph -= 2
    elif taste.lower() == "bitter":
        ph -= 1.5
    elif taste.lower() == "sweet":
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

    # Clamp pH value between 0 and 14
    ph = max(0, min(14, round(ph, 1)))
    return ph

def classify_ph(ph):
    if ph < 6.5:
        return (Fore.RED + "❌  Acidic and Unsafe")
    elif 6.5 <= ph <= 8.5:
        return (Fore.GREEN + "✅  Neutral and Safe")
    else:
        return (Fore.BLUE + " ❌  Alkaline and Unsafe")

# Get input from user
print(Fore.CYAN + "\n🌊 Tap Water pH Checker 🌊\n")
print(Fore.YELLOW + "Enter the following physical properties of water:\n")

color = input("Water Color (e.g., clear, yellowish , muddy,slightly brown,dark): ")
smell = input("Water Smell (e.g., none, chlorine, rotten egg, sewage, metallic): ")
taste = input("Water Taste (e.g., none, salty, sour, bitter, sweet): ")
temperature = float(input("Water Temperature in Celsius: "))

# Estimate and classify pH
ph = estimate_ph(color, smell, taste, temperature)
status = classify_ph(ph)

# Display the result
print("\n" + Fore.MAGENTA + "----- Water Analysis Result -----")
print(Fore.WHITE + f"Estimated pH value: {Fore.LIGHTYELLOW_EX}{ph}")
print(Fore.WHITE + "Water Condition: " + status)
print(Fore.MAGENTA + "----------------------------------" + Style.RESET_ALL)