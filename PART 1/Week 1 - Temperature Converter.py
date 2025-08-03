# Temperature Converter Program
# This program converts temperatures between Celsius and Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("🌡️  Welcome to the Temperature Converter 🌡️\n")

while True:
    print("Choose conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        temp = input("Enter temperature in Celsius: ").strip()
        try:
            c = float(temp)
            f = celsius_to_fahrenheit(c)
            print(f"\n🌡️  {c}°C is equal to {round(f, 2)}°F\n")
        except ValueError:
            print("⚠️ Please enter a valid number!\n")
            
    elif choice == "2":
        temp = input("Enter temperature in Fahrenheit: ").strip()
        try:
            f = float(temp)
            c = fahrenheit_to_celsius(f)
            print(f"\n🌡️  {f}°F is equal to {round(c, 2)}°C\n")
        except ValueError:
            print("⚠️ Please enter a valid number!\n")
            
    else:
        print("❌ Invalid choice! Please enter 1 or 2.\n")

    # Ask to continue
    again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("\n👋 Thank you for using the Temperature Converter!")
        break
