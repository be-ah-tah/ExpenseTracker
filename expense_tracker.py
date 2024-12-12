import manual_inputs as mi
import statements_upload as su
import apply_filters as af
import streamlit as st
import pandas as pd
import plotly.express as px

#def filterToDate(df, year, month)

#def filterToType(df, type):
    #if type is None:
        #return df
    #else:
        #return df[df['Type'] != type]

#def filterExprenses(df, year, month, type):
    #return filterToType(filterToDate(df, year, month), type)


def filteringExpenses(df, year, month, type):
    if month and year is None:
        if type is None:
            return df
        else:
            return df[df['Type'] != type]
    elif month == 'All' or month is None:
        year = int(year)
        if type is None:
            return df[df['Year'] == year]
        else:
            return df[(df['Year'] == year) & (df['Type'] != type)]
    elif year is None:
        month = int(month)
        if type is None:
            return df[df['Month'] == month]
        else:
            return df[(df['Month'] == month) & (df['Type'] != type)]
    else:
        month = int(month)
        year = int(year)
        if type is None:
            return df[(df['Year'] == year) & (df['Month'] == month)]
        else:
            return df[(df['Year'] == year) & (df['Month'] == month) & (df['Type'] != type)]


def run_app():
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['Date', 'Year', 'Month', 'Type', 'Amount'])

    if 'file' not in st.session_state:
        st.session_state.file = None

    if 'visual_aid_df' not in st.session_state:
        st.session_state.visual_aid_df = pd.DataFrame(columns=['Year', 'Month', 'Type', 'Sum'])

    option = st.selectbox(
        "How would input your expenses?",
        ("Manually", "Upload Amex", "Upload Aqua", "Upload Lloyds"),
    )

    if option == "Manually":
        amount = st.number_input('Enter amount of your expense: ')

        options = ['Groceries', 'Eating out', 'Tea and coffee out', 'Entertainment', 'Heath and medical costs',
                   'Car and travel cost', 'Holidays', 'Entertainment', 'Mobile', 'Clothing', 'Childcare', 'Housing',
                   'Utilities', 'Insurance', 'Fitness', 'Home and garden', 'Training', 'Miscellaneous']

        tran_type = st.selectbox(
            'Choose your expense type: ',
            options,
        )

        date = st.date_input("Select the date of expense: ", format="DD/MM/YYYY")

        manual_entries = {'Date': date, 'Type': tran_type, 'Amount': amount}

        if st.button("Add the expense"):
            output = mi.format_manual_input(manual_entries)
            st.session_state.df = pd.concat([st.session_state.df, output], ignore_index=True)
            st.write(f"Your expense have been added")

    else:
        filepath = st.file_uploader('Upload your statement:', type='csv')
        st.session_state.file = pd.read_csv(filepath)

        if st.button("Upload"):
            if st.session_state.file is not None:
                if option == "Upload Amex":
                    if not su.verify_key_columns_in_file(st.session_state.file, su.AMEX_KEY_COLUMNS):
                        st.write('WRONG FILE FORMAT: Check your file and try again')
                    output = su.import_creditcard_statement(option, st.session_state.file)
                elif option == "Upload Aqua":
                    if not su.verify_key_columns_in_file(st.session_state.file, su.AQUA_KEY_COLUMNS):
                        st.write('WRONG FILE FORMAT: Check your file and try again')
                    output = su.import_creditcard_statement(option, st.session_state.file)
                else:
                    if not su.verify_key_columns_in_file(st.session_state.file, su.LLOYDS_KEY_COLUMNS):
                        st.write('WRONG FILE FORMAT: Check your file and try again')
                    output = su.import_lloyds_statement(st.session_state.file)
                st.session_state.df = pd.concat([st.session_state.df, output], ignore_index=True)

    df_years_labels = st.session_state.df['Year'].unique().tolist()
    df_months_labels = st.session_state.df['Month'].unique().tolist()
    df_months_labels.append('All')
    df_types_labels = st.session_state.df['Type'].unique().tolist()

    data_years_filter = st.selectbox('Filter by Year:', df_years_labels, index=None)
    data_months_filter = st.selectbox('Filter by Month:', df_months_labels, index=None)
    data_types_filter = st.selectbox('Exclude:', df_types_labels, index=None)

    if st.button("Apply"):

        if data_months_filter == 'All' or data_months_filter is None:
            visual_aid_df = st.session_state.df.groupby(['Year', 'Type'])['Amount'].sum().reset_index(name='Sum')
            visual_aid_df = visual_aid_df.sort_values(by=['Type','Year'])
            visual_aid_df['Previous_Year_Sum'] = visual_aid_df.groupby('Type')['Sum'].shift(1)
            visual_aid_df['Average'] = visual_aid_df.groupby('Type')['Sum'].transform('mean')
            st.session_state.visual_aid_df = af.filter_expenses(visual_aid_df, data_years_filter, data_months_filter, data_types_filter)

        elif data_years_filter is None:
            visual_aid_df = st.session_state.df.groupby(['Month', 'Type'])['Amount'].sum().reset_index(
                name='Sum')
            visual_aid_df = visual_aid_df.sort_values(by=['Type', 'Month'])
            visual_aid_df['Previous_Month_Sum'] = visual_aid_df.groupby('Type')['Sum'].shift(1)
            visual_aid_df['Average'] = visual_aid_df.groupby('Type')['Sum'].transform('mean')
            st.session_state.visual_aid_df = af.filter_expenses(visual_aid_df, data_years_filter, data_months_filter,
                                                               data_types_filter)

        else:
            visual_aid_df = st.session_state.df.groupby(['Year', 'Month', 'Type'])['Amount'].sum().reset_index(
                name='Sum')
            visual_aid_df = visual_aid_df.sort_values(by=['Type', 'Year', 'Month'])
            visual_aid_df['Previous_Month_Sum'] = visual_aid_df.groupby('Type')['Sum'].shift(1)
            visual_aid_df['Average'] = visual_aid_df.groupby('Type')['Sum'].transform('mean')
            st.session_state.visual_aid_df = af.filter_expenses(visual_aid_df, data_years_filter, data_months_filter,
                                                               data_types_filter)

        st.subheader("Your spending composition")
        fig = px.pie(st.session_state.visual_aid_df, values='Sum', names='Type')
        st.plotly_chart(
        fig,
        key="pie_chart",
        )
        st.subheader("Your spending per category compared to previous month and average")
        categories = st.session_state.visual_aid_df['Type'].unique()
        fig = px.line(x=categories, y=st.session_state.visual_aid_df['Average'], color=px.Constant("Average"),
                      labels=dict(x="Category", y="Sum"))

        if data_months_filter == 'All' or data_months_filter is None:
            fig.add_bar(x=categories, y=st.session_state.visual_aid_df['Sum'], name="This year")
            fig.add_bar(x=categories, y=st.session_state.visual_aid_df['Previous_Year_Sum'], name="Previous year")
        else:
            fig.add_bar(x=categories, y=st.session_state.visual_aid_df['Sum'], name="This month")
            fig.add_bar(x=categories, y=st.session_state.visual_aid_df['Previous_Month_Sum'], name="Previous month")
        st.plotly_chart(
            fig,
            key="bar chart",
        )


run_app()

