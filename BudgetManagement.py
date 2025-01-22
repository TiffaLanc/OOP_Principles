class BudgetCategory:
    def __init__(self, category_name: str, allocated_budget: float) -> None:
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self) -> str:
        return self.__category_name
    
    def set_category_name(self, category_name: str) -> None:
        self.__category_name = category_name

    def get_allocated_budget(self) -> float:
        return self.__allocated_budget
    
    def set_allocated_budget(self, budget: float) -> None:
        if isinstance(budget, (int, float)) and budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            raise ValueError("Allocated budget amount must be positive. ")
        
    def add_expense(self, expense: float) -> None:
        if expense > 0 and expense <= self.__remaining_budget:
            self.__remaining_budget -= expense
        elif expense > self.__remaining_budget:
           raise ValueError("This expense exceeds the remaining budget")         
        else:
            raise ValueError("This expense amount must be positive")

           
    def get_remaining_budget(self) -> float:
        return self.__remaining_budget
    


    def display_budget_details(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget:  ${self.__remaining_budget}")

