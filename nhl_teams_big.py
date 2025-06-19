
import streamlit as st
import pandas as pd

# CSV laden
df = pd.read_csv("teams.csv")

st.title("NHL Teams")

# Jahr sicherstellen als int
df["Jahr"] = df["Jahr"].astype(int)

# Seitenleiste: Multiselect für Teamnamen
team_names = sorted(df["Team"].unique())
selected_teams = st.multiselect(
    "Wähle Teamnamen",
    options=team_names,
    default=team_names[:3] 
)

# Seitenleiste: Jahresbereich mit Slider
min_year = df["Jahr"].min()
max_year = df["Jahr"].max()
year_range = st.slider(
    "Jahresbereich filtern",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Filter anwenden
df_filtered = df[
    (df["Team"].isin(selected_teams)) &
    (df["Jahr"].between(year_range[0], year_range[1]))
]

# Tabelle anzeigen
st.expander("Datensatz anzeigen").dataframe(df_filtered, use_container_width=True)

# Dropdown für die Metrikauswahl
st.markdown("## Trendanalyse als Liniendiagramm")
metric_options = ["GF", "AF", "Siege", "Niederlagen"]
selected_metric = st.selectbox(
    "Wähle die Metrik für das Liniendiagramm",
    options=metric_options,
)

import plotly.express as px
# Liniendiagramm mit Plotly
if df_filtered.empty:
    st.info("Keine Daten für die gewählten Filter.")
else:
    fig = px.line(
        df_filtered,
        x="Jahr",
        y=selected_metric,
        color="Team",
        markers=True,
        title=f"Verlauf von {selected_metric}"
    )
    fig.update_layout(legend_title_text='Team')
    st.plotly_chart(fig, use_container_width=True)
