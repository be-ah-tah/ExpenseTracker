import apply_filters as af

def transform_data_for_visualisation(df, year, month, type):
    input_df = df.copy()
    if month in [None, 'All']:
        df = input_df.groupby([input_df['Date'].dt.year,'Type'])['Amount'].sum().reset_index(name='Sum')

    elif year is None:
        df = input_df.groupby([input_df['Date'].dt.month, 'Type'])['Amount'].sum().reset_index(name='Sum')

    else:
        input_df['Date'] = input_df['Date'].dt.to_period('M')
        df = input_df.groupby(['Date', 'Type'])['Amount'].sum().reset_index(name='Sum')

    df = df.sort_values(by=['Type', 'Date'])

    if month == 'All' or month is None:
        df['Previous_Year_Sum'] = df.groupby('Type')['Sum'].shift(1)
    else:
        df['Previous_Month_Sum'] = df.groupby('Type')['Sum'].shift(1)

    df['Previous_Month_Sum'] = df.groupby('Type')['Sum'].shift(1)
    df['Average'] = df.groupby('Type')['Sum'].transform('mean')
    df = af.filter_expenses(df, year, month, type)
    return df