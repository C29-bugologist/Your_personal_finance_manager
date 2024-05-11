class PersonalFinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description):
        self.transactions.append({"Amount": amount, "Category": category, "Description": description})
        print("Transaction added successfully!")

    def calculate_total(self):
        total_income = 0
        total_expense = 0
        for transaction in self.transactions:
            if transaction["Amount"] > 0:
                total_income += transaction["Amount"]
            else:
                total_expense += abs(transaction["Amount"])
        return total_income, total_expense
    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"Amount: ${transaction['Amount']}, Category: {transaction['Category']}, Description: {transaction['Description']}")


def main():
    manager = PersonalFinanceManager()

    while True:
        print("\nPersonal Finance Manager Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            description = input("Enter transaction description: ")
            manager.add_transaction(amount, category, description)
        elif choice == "2":
            manager.view_transactions()
        elif choice == "3":
            print("Exiting Personal Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
