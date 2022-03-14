"""
Area Calculator
"""

print("Starting the calculator...")
option = input("Enter the shape you'd like to find the area for: ")
answer = "The area of your shape is "

if option == 'Circle':
  radius = float(input("Enter radius: "))
  area = 3.14159 * radius**2
  print(answer, str(area))
elif option == 'Triangle':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = .5 * base * height
  print(answer, str(area))
elif option == 'Rectangle':
  width = float(input("Enter width: "))
  length = float(input("Enter length: "))
  area = width * length
  print(answer, str(area))
elif option == 'Trapezoid':
  base1 = float(input("Enter base 1: "))
  base2 = float(input("Enter base 2: "))
  height = float(input("Enter height: "))
  area = ((base1 + base2) / 2) * height
  print(answer, str(area))
elif option == 'Cylinder':
  radius = float(input("Enter radius: "))
  height = float(input("Enter height: "))
  area = (2 * 3.14159 * radius * height) + (2 * 3.14159 * radius**2)
  print(answer, str(area))
else:
  print("You've entered an invalid shape. This program only finds the area of circles, triangles, rectangles, trapezoids, and cylinders.")
print("Solution found!")

# py "C:\Users\Owner\Downloads\AreaCalculator.py"