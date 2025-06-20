import streamlit as st
from random import randint

st.title("Farbspiel")

def create_new_goal():
    st.session_state.goal_r = randint(0, 255)
    st.session_state.goal_g = randint(0, 255)
    st.session_state.goal_b = randint(0, 255)

if "goal_r" not in st.session_state:
    create_new_goal()

cols_colors = st.columns([1,2,1])

# Callbacks definieren – eine pro Farbe und Richtung
def update_slider_r():
    st.session_state.r_slider = st.session_state.r_value
    

def update_number_r():
    st.session_state.r_value = st.session_state.r_slider
    

def update_slider_g():
    st.session_state.g_slider = st.session_state.g_value
    

def update_number_g():
    st.session_state.g_value = st.session_state.g_slider
    

def update_slider_b():
    st.session_state.b_slider = st.session_state.b_value
    

def update_number_b():
    st.session_state.b_value = st.session_state.b_slider
    

with cols_colors[1]:
    col1, col2 = st.columns(2)
    col1.slider("🔴", 0, 255, key="r_slider", on_change=update_number_r)
    col2.number_input(" ", 0, 255, key="r_value", on_change=update_slider_r)
    col1, col2 = st.columns(2)
    col1.slider("🟢", 0, 255, key="g_slider", on_change=update_number_g)
    col2.number_input("  ", 0, 255, key="g_value", on_change=update_slider_g)
    col1, col2 = st.columns(2)
    col1.slider("🔵", 0, 255, key="b_slider", on_change=update_number_b)
    col2.number_input("   ", 0, 255, key="b_value", on_change=update_slider_b)

def circle_div(r, g, b):
    return f"""
        <div style='
            width: 150px;
            height: 150px;
            background-color: rgb({r}, {g}, {b});
            border-radius: 50%;
            margin-top: 20px;
            margin-left: auto;
            margin-right: auto;
        '>
        </div>
        """


with cols_colors[0]:
    st.header("You")
    st.markdown(
        circle_div(st.session_state.r_value, st.session_state.g_value, st.session_state.b_value),
        unsafe_allow_html=True
    )
with cols_colors[2]:
    st.header("Ziel")
    st.markdown(
        circle_div(st.session_state.goal_r, st.session_state.goal_g, st.session_state.goal_b),
        unsafe_allow_html=True
    )

def distance(r1, g1, b1, r2, g2, b2):
    return max(0, 100 - abs(r1 - r2) - abs(g1 - g2) - abs(b1 - b2))

d = distance(st.session_state.r_value, st.session_state.g_value, st.session_state.b_value, st.session_state.goal_r, st.session_state.goal_g, st.session_state.goal_b)
progress_bar = st.progress(d)

if d == 100:
    st.balloons()
    st.success("Gewonnen🎉")

def show_solution():
    cols_colors[0].write(f"{st.session_state.r_value}, {st.session_state.g_value}, {st.session_state.b_value}")
    cols_colors[2].write(f"{st.session_state.goal_r}, {st.session_state.goal_g}, {st.session_state.goal_b}")

st.button("Lösung zeigen", on_click=show_solution)
st.button("Neue Runde", on_click=create_new_goal)
