
amount = float(input("Enter total purchase amount: $"))

if amount > 100:
    discount = amount * 0.10
    final_amount = amount - discount
    print("You got a 10% discount!")
elif amount > 50:
    discount = amount * 0.05
    final_amount = amount - discount
    print("You got a 5% discount!")
else:
    discount = 0
    final_amount = amount
    print("No discount applied.")

print("Final amount to pay: $", final_amount)
