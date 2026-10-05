print("Area Calculator")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Choose a shape (1-3): "))

if choice == 1:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    area = width * length
    print("Area =", area)

elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area =", area)

elif choice == 3:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area =", area)

else:
    print("Invalid choice")
