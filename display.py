from BudgetManagement import BudgetCategory

def budget_management():
    try: 
        food_category = BudgetCategory("Food", 600)
        food_category.add_expense(100) #Chinese takeout
        food_category.add_expense(350) #Groceries
        food_category.display_budget_details()


        utilities_category = BudgetCategory ("Utilities", 500)
        utilities_category.add_expense(50) #Water/Sewer
        utilities_category.add_expense(150) #Electric
        utilities_category.display_budget_details()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to our Budget Management System! ")
    budget_management()
    print("\nThank you for using the application! ")

if __name__ == "__main__":
    main()