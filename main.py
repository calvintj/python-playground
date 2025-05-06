import math

class Tier:
    def __init__(self, membership, discount, benefits, expense, income):
        self.membership = membership
        self.discount = discount
        self.benefits = benefits if isinstance(benefits, list) else [benefits]
        self.expense = expense
        self.income = income

class silver(Tier):
    def __init__(self):
        benefits = ["Voucher Makanan",]
        super().__init__("Silver", 8, benefits, 5, 7)

class gold(Tier):
    def __init__(self):
        silver_tier = silver()
        benefits = ["Voucher Ojek Online",]
        all_benefits = silver_tier.benefits + benefits
        super().__init__("Gold", 10, all_benefits, 6, 10)

class platinum(Tier):
    def __init__(self):
        gold_tier = gold()
        benefits = [
            "Voucher Liburan",
            "Cashback max. 30%"
        ]
        all_benefits = gold_tier.benefits + benefits
        super().__init__("Platinum", 15, all_benefits, 8, 15)

def menu():
    while True:  # Add infinite loop
        print("1. Show all tier and membership details")
        print("2. Show monthly expense and income requirements")
        print("3. User tiers prediction")
        print("4. Calculate total shopping amounts")
        print("5. My membership details ")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tier_and_membership_details()
        elif choice == "2":
            show_monthly_expense_and_income_requirements()
        elif choice == "3":
            user_tiers_prediction()
        elif choice == "4":
            calculate_total_shopping_amounts()
        elif choice == "5":
            my_membership_details()
        elif choice == "6":
            exit()
        else:
            print("Invalid choice")

def show_tier_and_membership_details():
    tiers = [silver(), gold(), platinum()]
    for tier in tiers:
        print(f"\n{tier.membership} Tier:")
        print(f"Discount: {tier.discount}%")
        print("Benefits:")
        for benefit in tier.benefits:
            print(f"- {benefit}")
        print("-" * 30)

def show_monthly_expense_and_income_requirements():
    tiers = [silver(), gold(), platinum()]
    for tier in tiers:
        print(f"\n{tier.membership} Tier:")
        print(f"Monthly Expense: {tier.expense} juta")
        print(f"Monthly Income: {tier.income} juta")
        print("-" * 30)

# Euclidian Distance
def user_tiers_prediction():
    expense = float(input("Enter your monthly expense: "))
    income = float(input("Enter your monthly income: "))

    tiers = [silver(), gold(), platinum()]

    silver_distance = math.sqrt((expense - tiers[0].expense)**2 + (income - tiers[0].income)**2)
    gold_distance = math.sqrt((expense - tiers[1].expense)**2 + (income - tiers[1].income)**2)
    platinum_distance = math.sqrt((expense - tiers[2].expense)**2 + (income - tiers[2].income)**2)

    membership = min(silver_distance, gold_distance, platinum_distance)
    if membership == silver_distance:
        print("You are predicted to be a Silver tier member.")
    elif membership == gold_distance:
        print("You are predicted to be a Gold tier member.")
    else:
        print("You are predicted to be a Platinum tier member.")

def calculate_total_shopping_amounts():
    expense = float(input("Enter your shopping expense: "))
    membership = input("Enter your membership: ")
    tiers = [silver(), gold(), platinum()]
    if membership == "silver":
        shopping_amount = expense * (1 - tiers[0].discount/100)
    elif membership == "gold":
        shopping_amount = expense * (1 - tiers[1].discount/100)
    elif membership == "platinum":
        shopping_amount = expense * (1 - tiers[2].discount/100)
    print(f"Total shopping amounts: {shopping_amount} juta")

menu()
