class RentalProperty:
    def __init__(self, property_price, rental_income, operating_expenses, financing_costs):
        self.property_price = property_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.financing_costs = financing_costs

    def calculate_roi(self):
        net_operating_income = self.rental_income - self.operating_expenses
        cash_flow = net_operating_income - self.financing_costs
        total_investment = self.property_price + self.financing_costs
        roi = (cash_flow / total_investment) * 100
        return roi

property_price = float(input("Enter property price: "))
rental_income = float(input("Enter rental income: "))
operating_expenses = float(input("Enter operating expenses: "))
financing_costs = float(input("Enter financing costs: "))

property_instance = RentalProperty(property_price, rental_income, operating_expenses, financing_costs)
roi = property_instance.calculate_roi()

print(f"The Return on Investment (ROI) for the rental property is: {roi:.2f}%")