import streamlit as st

# ------------------------------------------------------------
# Streamlit Demo App - IMDb Info (Family Matters)
# ------------------------------------------------------------
#   Ziel : Beispiele fur Layout-Elemente wie Tabs, Container,
#          Columns, Metric, Image, Video u.v.m. zeigen.
#          Daten sind hier statisch hinterlegt, damit man sich
#          auf das Platzieren konzentrieren kann.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Helpers / Static Data
# ------------------------------------------------------------
TITLE_DE = "Alle unter einem Dach"
TITLE_EN = "Family Matters"
POSTER_URL = "https://image.tmdb.org/t/p/original/lIIPV3te2mxBQBHw2rfhwkUYsHf.jpg"
YOUTUBE_INTRO = "https://www.youtube.com/watch?v=5bEUmKy1HQg"

INFO = {
    "Jahre": "1989 - 1998",
    "Staffeln": 9,
    "Episoden": 215,
    "Laufzeit": "ca. 30 Min./Episode",
    "IMDb Rating": "6.6 / 10",
    "Stimmen": "ca. 31.000",
}

CAST_MAIN = [
    "Reginald VelJohnson - Carl Winslow",
    "Jaleel White - Steve Urkel / Stefan Urquelle",
    "Kellie Shanygne Williams - Laura Winslow",
    "Darius McCrary - Eddie Winslow",
    "Jo Marie Payton - Harriette Winslow",
    "Rosetta LeNoire - Mother Winslow",
]

SUMMARY = (
    "**Family Matters** ist eine US-amerikanische Sitcom rund um die afroamerikanische "
    "Mittelklasse-Familie Winslow in Chicago. Die Serie kombiniert herzlichen Familienhumor "
    "mit gesellschaftlichen Themen wie Rassismus, Waffengewalt oder Gleichberechtigung. "
    "Zum Kultstatus trug vor allem die Figur **Steve Urkel** bei, deren Erfindungen die "
    "Handlung immer wieder in Science-Fiction-Gefilde abgleiten lassen."
)

# ------------------------------------------------------------
# Layout : Header + Metrics
# ------------------------------------------------------------
with st.container():
    col_poster, col_title = st.columns([1, 2], gap="large")

    with col_poster:
        st.image(POSTER_URL, use_container_width=True)

    with col_title:
        st.title(f"{TITLE_EN} - {TITLE_DE}")
        st.caption(INFO["Jahre"] + " | " + INFO["Laufzeit"])

        m1, m2, m3 = st.columns(3)
        m1.metric("IMDb Rating", INFO["IMDb Rating"], None)
        m2.metric("Staffeln", INFO["Staffeln"])
        m3.metric("Episoden", INFO["Episoden"])

        st.write(SUMMARY)

# ------------------------------------------------------------
# Tabs Section
# ------------------------------------------------------------

overview_tab, cast_tab, media_tab = st.tabs(["Überblick", "Hauptcast", "Media"])

with overview_tab:
    st.subheader("Kurzer Inhalt")
    st.write(
        "Die Winslows sind eine liebenswerte Familie, deren Alltag immer wieder "
        "durch die schrulligen Erfindungen ihres Nachbarn Steve Urkel auf den Kopf "
        "gestellt wird. Trotz verrückter Situationen steht am Ende jeder Episode "
        "der familiäre Zusammenhalt im Mittelpunkt."
    )

    with st.expander("Auszeichnungen (Auszug)"):
        st.markdown("""
        * Emmy-Nominierung für **Beste visuelle Effekte** (Folge *Der doppelte Steve*)  
        * **BMI Film & TV Award** für Bennett Salvay (1991, 1992)  
        * **NAACP Image Awards** für Jaleel White (1994, 1995, 1997)
        """)

with cast_tab:
    st.subheader("Besetzung - Hauptrollen")
    st.write("\n".join([f"- {member}" for member in CAST_MAIN]))

with media_tab:
    st.subheader("Serien-Intro (Video)")
    st.video(YOUTUBE_INTRO)

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.header("📈 Statistik")
    st.metric("IMDb Rating", INFO["IMDb Rating"])

    st.header("🔗 Links")
    st.markdown("* [IMDb-Seite](https://www.imdb.com/title/tt0096579)\n* [Wikipedia-Artikel (de)](https://de.wikipedia.org/wiki/Alle_unter_einem_Dach)")
