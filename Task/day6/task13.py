'''
Write a program to convert temperature from degree Celsius to Fahrenheit and Kelvin.
fahrenheit = (celsius * 9/5) + 32
'''

temp = float(input("Enter a temperature in degree : "))

fahrenheit = (temp * 9 / 5) + 32
print(f"{temp} degree celsius to fahrenheit is {fahrenheit}")

kelvin = temp + 273.15 
print(f"{temp} degree celsius to kelvin is {kelvin}")
