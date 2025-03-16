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
    label="",
    options=SYMPTOMS,
    placeholder="Start writing your symptoms and then pick from the dropdown list",
)


if st.button(label="Predict", use_container_width=True):
    st.write("### Influenza")
