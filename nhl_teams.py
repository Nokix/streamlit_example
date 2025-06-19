import streamlit as st
import pandas as pd

# CSV laden
df = pd.read_csv("teams.csv")

st.title("NHL Teams")

# Jahr zu int konvertieren (falls nötig)
df["Jahr"] = df["Jahr"].astype(int)

# Seitenleiste: Filter für Teamnamen
team_filter = st.sidebar.text_input("Teamname enthält:", "").strip().lower()

# Seitenleiste: Jahr-Range-Slider
min_year = df["Jahr"].min()
max_year = df["Jahr"].max()
year_range = st.sidebar.slider(
    "Jahresbereich filtern",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Filter anwenden
df_filtered = df[
    df["Jahr"].between(year_range[0], year_range[1])
]

if team_filter:
    df_filtered = df_filtered[
        df_filtered["Team"].str.lower().str.contains(team_filter)
    ]

# Tabelle anzeigen
st.dataframe(df_filtered, use_container_width=True)
