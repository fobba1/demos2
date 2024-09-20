import pandas as pd
import streamlit as st

df_orig = pd.read_csv("population.csv", index_col=False, header=0)
df2 = df_orig[['year', 'country', 'pop']]

df = df2.pivot(index="year", columns="country", values="pop")
columns = st.multiselect("Columns: ", df.columns)
st.line_chart(df, y=columns, y_label="Population", x_label="Year")

