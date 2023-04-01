unit = input("Is the input is in Celsius or Fahrenheit (C/F): ").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    # Formula: (Temp * 9 / 5) - 32
    temp = round((temp * 9 / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is:  {temp}°F")
elif unit == "f":
    # Formula: (temp - 32) * 5 / 9
    temp = round((temp - 32) * 5 / 9)
    print(f"The temperature in Celsius is:  {temp}°C")
else:
    print(f"{unit} is not valid!")
