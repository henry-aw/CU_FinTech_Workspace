# Initial imports
import csv
from pathlib import Path


# This function loads a CVS file from the filepath defined in `csvpath`
def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# This function loads a CSV file with the list of banks and available loans information
# from the file defined in `file_path`
def load_bank_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)



# This function is the main execution point of the application. It triggers all the business logic.
def run():
    # Set the file path of the CVS file with the banks and loans information
    file_path = Path("./data/daily_rate_sheet.csv")
    # Load the latest Bank data
    bank_data = load_bank_data(file_path)

    # This print statement will display all of the bank data that is provided.
    print(f"bank_data: {bank_data}")

    # These print statements will detail the information available for the first bank in the list (index position 0):
    print(f"Accessing the first bank's Lender Name: {bank_data[0][0]}")
    print(f"Accessing the first bank's Max Loan Amount: {bank_data[0][1]}")
    print(f"Accessing the first bank's Max LTV (loan to value ratio): {bank_data[0][2]}")
    print(f"Accessing the first bank's Max DTI (debit to income ratio): {bank_data[0][3]}")
    print(f"Accessing the first bank's Min Credit Score: {bank_data[0][4]}")
    print(f"Accessing the first bank's Interest Rate: {bank_data[0][5]}")


# Run the application
run()
