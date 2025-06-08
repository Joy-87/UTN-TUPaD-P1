def celsius_a_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32
try:
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para la temperatura.")
