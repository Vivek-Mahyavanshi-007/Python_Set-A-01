fileh = open("Output.txt", 'w')

temp = int(input("""Select your choice to enter the temperature in respected degree:
1. Fahrenheit
2. Celsius
Enter your choice (1 or 2): """))

if temp == 1:
    Fa = int(input("Enter the temp in Fahrenheit:"))
    C = (Fa - 32) * 5 / 9
    fileh.write(f"{Fa} Degrees Fahrenheit is equal to {C} Degrees Celsius")

elif temp == 2:
    ce = int(input("Enter the temp in Celsius: "))
    F = (9 / 5) * ce + 32
    fileh.write(f"{ce} Degrees Celsius is equal to {F} Degrees Fahrenheit")

else:
    fileh.write("Invalid choice")

fileh.close()
