import manual_inputs as mi
import statements_upload as su
import transform_data as td
import streamlit as st
import pandas as pd
import plotly.express as px

def run_app():
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['Date', 'Type', 'Amount'])

    if 'file' not in st.session_state:
        st.session_state.file = None

    if 'visual_df' not in st.session_state:
        st.session_state.visual_df = pd.DataFrame(columns=['Date', 'Type', 'Sum'])

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

        if st.button("Add the expense"):
            output = mi.format_manual_input(date, tran_type, amount)
            st.session_state.df = pd.concat([st.session_state.df, output], ignore_index=True)
            st.write(f"Your expense have been added")

    else:
        filepath = st.file_uploader('Upload your statement:', type='csv')
        if filepath is not None:
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
                st.write('Your statement has been successfully uploaded')

    if not st.session_state.df.empty:
        print(st.session_state.df.dtypes)
        print(st.session_state.df['Date'].isna().sum())
        years_labels = st.session_state.df['Date'].dt.year.unique().tolist()
        year_filter = st.selectbox('Filter by Year:', years_labels, index=None)

        months_labels = st.session_state.df['Date'].dt.month.unique().tolist()
        months_labels.append('All')
        month_filter = st.selectbox('Filter by Month:', months_labels, index=None)

        types_labels = st.session_state.df['Type'].unique().tolist()
        type_exclusion = st.selectbox('Exclude:', types_labels, index=None)

        if st.button("Apply"):
            st.session_state.visual_df = td.transform_data_for_visualisation(st.session_state.df, year_filter, month_filter, type_exclusion)

            st.subheader("Your spending composition")
            fig = px.pie(st.session_state.visual_df, values='Sum', names='Type')
            st.plotly_chart(
            fig,
            key="pie_chart",
            )

            st.subheader("Your spending per category compared to previous month and average")
            categories = st.session_state.visual_df['Type'].unique()
            fig = px.line(x=categories, y=st.session_state.visual_df['Average'], color=px.Constant("Average"),
                          labels=dict(x="Category", y="Sum"))

            if month_filter == ['All' or None]:
                fig.add_bar(x=categories, y=st.session_state.visual_df['Sum'], name="This year")
                fig.add_bar(x=categories, y=st.session_state.visual_df['Previous_Year_Sum'], name="Previous year")
            else:
                fig.add_bar(x=categories, y=st.session_state.visual_df['Sum'], name="This month")
                fig.add_bar(x=categories, y=st.session_state.visual_df['Previous_Month_Sum'], name="Previous month")

            st.plotly_chart(
                fig,
                key="bar chart",
            )


run_app()

