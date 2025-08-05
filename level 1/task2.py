unit=input("is the tempuraturein celsius or fahrenheit (C/F): ").lower()
temp=float(input("enter the temperature: "))
if unit=="c":
    temp=(9*temp)/5+32
    print(f"the temperature in Farenheit is:  {temp} F")
elif unit=="f":
    temp=(temp-32)*5/9
    print(f"the temperature in celsius is:  {temp} C")

else:
    print(f"{unit} is an  invalid unit of measurement")
