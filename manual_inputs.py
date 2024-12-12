import pandas as pd
def format_manual_input(manual_entries):
    date = pd.Timestamp(manual_entries['Date'])
    month = date.month
    year = date.year

    inputs = {'Date': [date], 'Year': [year], 'Month': [month], 'Type': [manual_entries['Type']], 'Amount': [manual_entries['Amount']]}
    data = pd.DataFrame(inputs)
    return data