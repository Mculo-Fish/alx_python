#!/usr/bin/env python3
# convert_to_celsius = __import__('2-temperature').convert_to_celsius

def convert_to_celsius(fahrenheit):
    celcius =(5/9)*(fahrenheit-32)
    return celcius

print(convert_to_celsius(100), end='\n')
print(convert_to_celsius(-40), end='\n')
print(convert_to_celsius(-459.67), end='\n')
print(convert_to_celsius(32) , end='\n')