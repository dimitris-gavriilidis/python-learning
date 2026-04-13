'''
CS50P Week 0 - Einstein
Calculates energy from mass using E = mc²
'''

mass = int(input("Enter mass in kilograms:"))
speed_of_light = 300000000
energy = mass *speed_of_light**2
print(energy)