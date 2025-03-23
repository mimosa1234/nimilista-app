import streamlit as st

def valitse_toiminto():
    st.title("Nimilista- ja ryhmätyökalu")
    return st.radio("Valitse toiminto:", ["HKP Excel", "Sunnuntai Kela"])
