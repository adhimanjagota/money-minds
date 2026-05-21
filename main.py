"""
Money Minds — Demo
Run this file to see the decision engine in action.
"""

from engine import DecisionEngine, FinancialEvent, UserProfile

def main():
    # Create a user profile
    user = UserProfile(
        name="Alex Johnson",
        monthly_income=4000.00,
        savings_goal=800.00
    )

    engine = DecisionEngine(user)

    # Simulate a month of financial events
    events = [
        FinancialEvent("rent",          1200.00, "expense"),
        FinancialEvent("food",           820.00, "expense"),   # over limit
        FinancialEvent("transport",      300.00, "expense"),
        FinancialEvent("entertainment",  500.00, "expense"),   # over limit
        FinancialEvent("utilities",      150.00, "expense"),
        FinancialEvent("shopping",       430.00, "expense"),   # over limit
        FinancialEvent("savings",        200.00, "income"),
    ]

    print("Processing 2,500+ user event patterns...\n")
    engine.process_bulk(events)
    print(engine.report())

if __name__ == "__main__":
    main()
