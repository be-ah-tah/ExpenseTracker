import pandas as pd
from rapidfuzz import process


AMEX_KEY_COLUMNS = ['Date', 'Description', 'Amount']
AQUA_KEY_COLUMNS = ['Date', 'Description', 'Amount(GBP)']
LLOYDS_KEY_COLUMNS = ['Transaction Date', 'Transaction Description', 'Debit Amount', 'Credit Amount']

def verify_key_columns_in_file(data, expected_columns):
    actual_columns = list(data.columns)

    if set(expected_columns).issubset(actual_columns):
        return True
    return False

def assign_transation_to_category(description):
    categories = pd.read_csv('~/Library/CloudStorage/GoogleDrive-beata.b.anton@gmail.com/My Drive/Career/GitHub Projects/ExpenseTracker/categories.csv')
    best_match = process.extractOne(description, categories['Key'])
    if best_match[1] < 50:
        return "Miscellaneous"
    value = categories.iloc[best_match[2]]['Value']
    return value

def import_creditcard_statement(type, data):
    data['Description'] = data['Description'].str.replace('*', ' ')
    data['Description'] = data['Description'].str.lower()
    data['Type'] = data['Description'].apply(assign_transation_to_category)

    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, format='%d/%m/%Y', errors='coerce')

    if type == 'Upload Aqua':
        data['Amount'] = data['Amount(GBP)']
        data = data[~data['Description'].str.contains('payment received|loyalty award', case=False, na=False)]

    return data[['Date', 'Type', 'Amount']]

def credit_and_debit_to_amount(row):
    if pd.isna(row['Debit Amount']):
        return 0 - float(row['Credit Amount'])
    else:
        return row['Debit Amount']

def import_lloyds_statement(data):
    data['Type'] = data['Transaction Description'].apply(assign_transation_to_category)

    data['Date'] = pd.to_datetime(data['Transaction Date'], dayfirst=True, format='%d/%m/%Y', errors='coerce')
    data['Amount'] = data.apply(credit_and_debit_to_amount, axis=1)

    data = data[data['Type'] != "Miscellaneous"]

    return data[['Date', 'Type', 'Amount']]




