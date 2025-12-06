"""Financial Calculator for:"""
# - Investment (simple or compound interest)
# - Home loan (bond) repayments

import math


def get_positive_float(prompt):
    """
    Prompt the user for a positive floating-point number.

    Parameters
    ----------
    prompt : str
        The message will be displayed to the user.

    Returns
    -------
    float
        A positive floating-point number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a greater number than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numeric value.")


def get_interest_rate(prompt):
    """
    Prompt the user for a valid interest rate (numeric only,
    without the '%' symbol).

    Parameters
    ----------
    prompt : str
        The message will be displayed to the user.

    Returns
    -------
    float
        The interest rate entered by the user (as a numeric percentage).
    """
    while True:
        rate_input = input(prompt).strip()
        if "%" in rate_input:
            print("Do not include the '%' symbol.")
            print("Enter numbers only (i.e. 8 for 8%).")
            continue
        try:
            rate = float(rate_input)
            if rate <= 0:
                print("Please enter interest rate greater than zero.")
            else:
                return rate
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_simple_interest(principal, rate, years):
    """
    Calculate total amount for simple interest.

    Parameters
    ----------
    principal : float
        The initial investment amount.
    rate : float
        The annual interest rate (in percentage).
    years : float
        The number of years the money is invested.

    Returns
    -------
    float
        The total accumulated amount after interest.
    """
    return principal * (1 + (rate / 100) * years)


def calculate_compound_interest(principal, rate, years):
    """
    Calculate total amount for compound interest.

    Parameters
    ----------
    principal : float
        The initial investment amount.
    rate : float
        The annual interest rate (in percentage).
    years : float
        The number of years the money is invested.

    Returns
    -------
    float
        The total accumulated amount after compound interest.
    """
    return principal * math.pow((1 + (rate / 100)), years)


def calculate_bond_repayment(house_value, annual_rate, months):
    """
    Calculate monthly repayment amount for a bond (loan).

    Parameters
    ----------
    house_value : float
        The present value of the house or loan amount.
    annual_rate : float
        The annual interest rate (in percentage).
    months : int
        The number of months over which the bond will be repaid.

    Returns
    -------
    float
        The monthly repayment amount.
    """
    monthly_rate = (annual_rate / 100) / 12
    denom = 1 - math.pow(1 + monthly_rate, -months)
    repayment = (monthly_rate * house_value) / denom
    return repayment


def handle_investment():
    """
    Handle user input and display results for investment calculations.

    Prompts the user for deposit amount, interest rate,
    and investment duration.
    Allows user to choose between simple or compound interest and displays the
    final investment value.
    """
    print("\nInvestment Calculator:")
    principal = get_positive_float("Enter the amount you want to Deposit: £")
    rate = get_interest_rate("Enter the interest rate (i.e. 8 for 8%): ")
    years_prompt = "Enter the number of years you want to invest: "
    years = get_positive_float(years_prompt)

    while True:
        prompt = "Do you want 'simple' or 'compound' interest?: "
        interest_type = input(prompt).strip().lower()
        if interest_type in ("simple", "compound"):
            break
        print("Invalid choice. Please enter 'simple' or 'compound'.")

    if interest_type == 'simple':
        total = calculate_simple_interest(principal, rate, years)
    else:
        total = calculate_compound_interest(principal, rate, years)

    print(
        f"\nAfter {years:.0f} years, your investment will be worth: "
        f"£{total:,.2f}\n"
    )


def handle_bond():
    """
    Handle user input and display bond repayment calculation results.

    Prompts the user for the value of the house, annual interest rate, and
    number of months for repayment.
    Calculates and displays the monthly repayment.
    """
    print("\nBond Repayment Calculator:")
    house_value = get_positive_float("Enter current value of the house: £")
    rate = get_interest_rate("Enter annual interest rate (i.e. 7 for 7%): ")
    months_prompt = "Enter how many months you want to repay the bond: "
    months = get_positive_float(months_prompt)

    if months <= 0 or rate <= 0:
        print("Invalid input: months and interest rate must be > 0.")
        return

    repayment = calculate_bond_repayment(house_value, rate, int(months))
    print(f"\nYour monthly repayment will be: £{repayment:,.2f}\n")


def main():
    """
    Display the main program menu and handle user selections.

    Provides a text-based menu allowing the user to:
    - Calculate investment returns
    - Calculate home loan (bond) repayments
    - Exit the calculator
    """
    print("Welcome to your Financial Calculator!\n")

    while True:
        print("Please type your option:")
        print("Investment - Calculate investment returns")
        print("Bond       - Calculate home loan repayments")
        print("Exit       - Exit calculator")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "investment":
            handle_investment()
        elif choice == "bond":
            handle_bond()
        elif choice == "exit":
            print("\nThank you for using Financial Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
