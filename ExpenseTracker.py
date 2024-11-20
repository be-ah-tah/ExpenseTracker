import streamlit as st
import pick
import pandas as pd

def manualInputExpense():
    amount = input('Enter amount of your expense: ')
    print(amount)

    type_title = 'Choose your expense type: '
    options = ['Groceries', 'Eating out', 'Tea and coffee out', 'Entertainment', 'Heath and medical costs', 'Car and travel cost', 'Holidays', 'Entertainment', 'Mobile', 'Clothing', 'Childcare', 'Housing', 'Insurance', 'Fitness', 'Home and garden', 'Training', 'Miscellaneous']
    type, type_index = pick(options, type_title, indicator='=>', default_index=1)

    month_title = 'Choose month of the expense: '
    options = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month, month_index = pick(options, month_title, indicator='=>', default_index=1)

    year = input('Enter year of the expense : ')

    inputs = {'Year': year, 'Month': month, 'Type': type, 'Amount': amount}
    data = pd.DataFrame(inputs)
    return data

def clarifyingImportedExpenses(description):
    types_dict = {
        "ocado": "Groceries",
        "waitrose": "Groceries",
        "asda": "Groceries",
        "bakery": "Groceries",
        "butchers": "Groceries",
        "outdoorwear": "Clothing",
        "craghoppers": "Clothing",
        "jojo": "Clothing",
        "vinted": "Clothing",
        "marks & spencer": "Home and garden",
        "google": "Mobile",
        "bambino mio": "Childcare",
        "itsu": "Eating out",
        "la chingada": "Eating out",
        "trainline": "Car and travel cost",
        "dvsa": "Car and travel cost",
        "driver and vehicle": "Car and travel cost",
        "aa driving": "Car and travel cost",
        "coffee": "Tea and coffee out",
        "cafe": "Tea and coffee out",
        "debenhams": "Home and garden",
        "hotel chocolate": "Tea and coffee out",
        "john lewis": "Home and garden",
        "dunelm": "Home and garden",
        "tfl": "Car and travel cost",
        "taxis": "Car and travel cost",
        "amazon": "Miscellaneous",
        "b & m": "Home and garden",
        "b&m": "Home and garden",
        "t.k.maxx": "Home and garden",
        "oxfam": "Home and garden",
        "dogs trust": "Home and garden",
        "robert dyas": "Home and garden",
        "brooker": "Home and garden",
        "starbucks": "Tea and coffee out",
        "deliveroo": "Eating out",
        "wagamama": "Eating out",
        "nando's": "Eating out",
        "groundworks": "Eating out",
        "ice cream": "Eating out",
        "fussey & baer": "Eating out",
        "beershophq.uk": "Eating out",
        "cineworld": "Home and garden",
        "ebay": "Home and garden",
        "tea people": "Tea and coffee out",
        "linkedin": "Training",
        "abebooks": "Entertainment",
        "360 play": "Entertainment",
        "audible": "Entertainment",
        "steam": "Entertainment",
        "mamababyplay": "Entertainment",
        "everyone active": "Entertainment",
        "science museum": "Entertainment",
        "kazoku": "Entertainment",
        "fossa": "Entertainment",
        "sea life": "Entertainment",
        "david lloyd": "Entertainment",
        "the works": "Entertainment",
        "zettle": "Entertainment",
        "square inc": "Entertainment",
        "sumup": "Entertainment",
        "triangle garden": "Entertainment",
        "climbing centre": "Entertainment",
        "stem discovery": "Entertainment",
        "elemis": "Heath and medical costs",
        "boots": "Heath and medical costs",
        "pharmacy": "Heath and medical costs",
        "sephora": "Heath and medical costs",
        "superdrug": "Heath and medical costs",
        "hairdressing": "Heath and medical costs",
        "wickes": "Home and garden",
        "toolstation": "Home and garden",
        "cook": "Groceries",
    }
    lower_description = description.lower()
    for key in types_dict:
        if lower_description.find(key) != -1:
            return types_dict[key]
    return "Miscellaneous"

def importAmexStatement(filename):
    data = pd.read_csv(f'/Users/beata/Library/CloudStorage/GoogleDrive-beata.b.anton@gmail.com/My Drive/Career/Python/Job Exercises/{filename}')
    data['Type'] = data['Description'].apply(clarifyingImportedExpenses)

    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    data['Month'] = data['Date'].dt.month_name().str[:3]
    data['Year'] = data['Date'].dt.strftime('%Y')

    return data[['Year', 'Month', 'Type', 'Amount']]

def importAquaStatement(filename):
    data = pd.read_csv(f'/Users/beata/Library/CloudStorage/GoogleDrive-beata.b.anton@gmail.com/My Drive/Career/Python/Job Exercises/{filename}')
    data['Type'] = data['Description'].apply(clarifyingImportedExpenses)

    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    data['Month'] = data['Date'].dt.month_name().str[:3]
    data['Year'] = data['Date'].dt.strftime('%Y')
    data['Amount'] = data['Amount(GBP)']

    data = data[~data['Description'].str.contains('payment received', case=False, na=False)]

    return data[['Year', 'Month', 'Type', 'Amount']]

def run_app():
    option = st.selectbox(
        "How would input your expenses?",
        ("Manually", "Upload Amex", "Upload Aqua"),
    )

    st.write("You selected:", option)





importAmex = importAmexStatement('activity.csv')
importAqua = importAquaStatement('2024-08-13-2024-11-13.csv')
combined = pd.concat([importAmex, importAqua], ignore_index=True)
grouped = combined.groupby(['Year', 'Month', 'Type'])['Amount'].sum().reset_index()
print(grouped)
combined.to_csv('output.csv', index=False)

if __name__ == '__main__':

