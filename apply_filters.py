def filter_to_date(df, year, month):
    if month and year is None:
        return df
    elif month == 'All' or month is None:
        year = int(year)
        return df[df['Date'].dt.year == year]
    elif year is None:
        month = int(month)
        return df[df['Date'].dt.month == month]
    else:
        month = int(month)
        year = int(year)
        return df[(df['Date'].dt.year == year) & (df['Date'].dt.month == month)]


def filter_to_type(df, type):
    if type is None:
        return df
    else:
        return df[df['Type'] != type]

def filter_expenses(df, year, month, type):
    return filter_to_type(filter_to_date(df, year, month), type)