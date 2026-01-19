def bill_splitter():
    print("=== Bill Splitter ===")

    # Total bill
    total_bill = float(input("Enter total bill amount: ₹ "))

    # Tip
    add_tip = input("Do you want to add tip? (yes/no): ").lower()
    tip_amount = 0

    if add_tip == "yes":
        tip_percent = float(input("Enter tip percentage: "))
        tip_amount = (tip_percent / 100) * total_bill

    final_bill = total_bill + tip_amount

    # Number of people
    people = int(input("Enter number of people: "))

    # Split
    split_amount = round(final_bill / people, 2)

    print("\n----- Bill Summary -----")
    print(f"Bill Amount   : ₹ {total_bill}")
    print(f"Tip Amount    : ₹ {round(tip_amount, 2)}")
    print(f"Total Bill    : ₹ {round(final_bill, 2)}")
    print(f"People        : {people}")
    print(f"Each Pays     : ₹ {split_amount}")
    print("------------------------")


if __name__ == "__main__":
    bill_splitter()
