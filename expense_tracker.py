import csv
from datetime import datetime

# Function to log expenses to a CSV file
def log_expense(amount, category, description):
    """
    Logs an expense by writing the details into a CSV file.

    Parameters:
    amount (float): The amount of the expense.
    category (str): The category of the expense (e.g., 'Groceries', 'Transport').
    description (str): A brief description of the expense.
    """
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, category, description])

# Function to generate a summary report from the CSV file
def generate_report():
    """
    Reads the expense records from the CSV file and generates a total expense summary.
    """
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            total = 0.0
            expenses_by_category = {}

            for row in reader:
                # Skip empty rows or rows with missing data
                if len(row) != 4:
                    continue

                date_time, amount, category, description = row
                amount = float(amount)

                # Update the total expense
                total += amount

                # Track total expenses by category
                if category in expenses_by_category:
                    expenses_by_category[category] += amount
                else:
                    expenses_by_category[category] = amount

            # Display total expenses
            print(f'\nTotal Expenses: ₱{total:.2f}')

            # Display expenses by category
            print("\nExpenses by Category:")
            for category, total_category in expenses_by_category.items():
                print(f'{category}: ₱{total_category:.2f}')
    
    except FileNotFoundError:
        print('No expenses logged yet.')
    except Exception as e:
        print(f'Error occurred: {e}')

# Example usage of the expense tracker functions
log_expense(150.75, 'Groceries', 'Bought fruits and vegetables')
log_expense(250.00, 'Transportation', 'Taxi ride to work')
log_expense(500.00, 'Entertainment', 'Movie tickets')

# Generate a summary report of logged expenses
generate_report()

print("Generated Report is saved to expenses.csv")
