amount_due = 50
accepted = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due:", amount_due)
    # Ask user to insert a coin
    coin = input("Insert Coin: ")
    # If coin is accepted, subtract it from the amount due
    if int(coin) in accepted:
        amount_due -= int(coin)

# Print change owed to user
change_owed = amount_due * (-1)
print(f"Change Owed:", change_owed)