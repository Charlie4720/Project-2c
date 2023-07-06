change = float(input("Enter an amount in cents less than a dollar:"))
remainder_1 = float(change // 25)
remainder_2 = float(change - 25 * remainder_1) // 10
remainder_3 = float(change - 25 * remainder_1- 10 * remainder_2) // 5
remainder_4 = float(change - 25 * remainder_1- 10 * remainder_2 - 5 * remainder_3)

print("Q:", remainder_1)
print("D:", remainder_2)
print("N:", remainder_3)
print("P:", remainder_4)
