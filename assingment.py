first_number =float(input("First Number"))
second_number = float(input("Second Number"))
operation = input("Arithmetic Operation +, -, *, or /")
if operation == "+":
  print(first_number, " + ", second_number, " = ", first_number + second_number)
elif operation == "-":
  print(first_number, " - ", second_number, " = ", first_number - second_number)
elif operation == "*":
  print(first_number, " * ", second_number, " = ", first_number * second_number)
else operation == "/":
print(first_number, " / ", second_number, " = ", first_number / second_number)
