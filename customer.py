
def calculate_bill(smartwatch, laptop, smartphone):
    total = "smartwatch" + "laptop" + "smartphone"
    return total


if __name__ == "__main__":
    smartwatch = float(input("Enter smartwatch price: "))
    laptop = float(input("Enter laptop price: "))
    smartphone = float(input("Enter smartphone price: "))

    total = calculate_bill(smartwatch, laptop, smartphone)

    print("Total Bill Amount:", total)
