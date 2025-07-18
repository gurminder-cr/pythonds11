import streamlit as st 
import pandas as pd
import plotly.express as px

st.header("Superstore Visualization")

df= pd.read_excel('SuperStoreUS-2015.xlsx')

st.write(df)
# st.table(df)

figure= px.bar(df,x='Product Category', y='Sales', color='Product Sub-Category')
st.plotly_chart(figure)


fig2_values= df.loc[:,'Product Sub-Category'].value_counts().values
fig2_names= df.loc[:,'Product Sub-Category'].value_counts().index


figure2= px.pie(names=fig2_names, values=fig2_values)

st.plotly_chart(figure2)