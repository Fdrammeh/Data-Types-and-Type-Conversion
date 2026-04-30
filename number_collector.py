# Number 1
try:
    num1 = int(input("Enter number 1: "))
except ValueError:
    print("Invalid input for number 1. Defaulting to 0.")
    num1 = 0

try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("Invalid input for number 2. Defaulting to 0.")
    num2 = 0

try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print("Invalid input for number 3. Defaulting to 0.")
    num3 = 0


total = num1 + num2 + num3
average = total / 3
    
    #total = num1 + num2 + num3
   
#average = int(input("total: "))


print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Number 3: {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")

