import streamlit as st

SYMPTOMS = [
    "Running nose",
    "Fever",
    "Headache",
    "Dry cough",
    "Wet cough",
    "Shivering",
    "Rigor",
]


st.title("Welcome to a PocketDoctor")

options = st.multiselect(
    label="Label",
    options=SYMPTOMS,
    placeholder="Start writing your symptoms and then pick from the dropdown list",
    label_visibility="hidden",
)


if st.button(label="Predict", use_container_width=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### :red[Disease]")
        st.write("##### Influenza")
    with col2:
        st.write("### :green[Medication]")
        st.write("##### Ibuprophene")
    with col3:
        st.write("### :blue[Regime]")
        st.write("##### Rest")
