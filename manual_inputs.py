import pandas as pd
def format_manual_input(date, type, amount):
    date = pd.to_datetime(date, dayfirst=True, format='%d/%m/%Y', errors='coerce')
    inputs = {'Date': [date], 'Type': type, 'Amount': amount}
    df = pd.DataFrame(inputs, index=[0])
    return df