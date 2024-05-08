def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Strip the leading $ sign
    d = d.lstrip("$")
    # Convert string to float
    df = float(d)
    return df


def percent_to_float(p):
    # Strip the training % sign
    p = p.rstrip("%")
    # Convert to float
    pf = float(p)
    # Divide by 100
    pf = pf / 100
    return pf

main()