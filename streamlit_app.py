import streamlit as st
import pandas as pd

data = {
    "Name": ["Anna", "Ben", "Clara", "David"],
    "Alter": [28, 34, 25, 42],
    "Stadt": ["Berlin", "München", "Hamburg", "Köln"],
}
df = pd.DataFrame(data)

st.title("Einfache Tabelle mit Streamlit und Pandas")
st.dataframe(df)
