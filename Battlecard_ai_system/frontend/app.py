import streamlit as st
import requests

st.title("AI-Powered Battlecard Generator")

competitor_name = st.text_input("Enter Competitor Name")
product_info = st.text_area("Enter Product Info")

if st.button("Generate Battlecard"):
    response = requests.post(
        "http://127.0.0.0.0:8000/generate_battlecard/",
        json={"competitor_name": competitor_name, "product_info": product_info}
    )
    
    if response.status_code == 200:
        st.success("Battlecard generated!")
        st.image("battlecard.png")
    else:
        st.error("Error generating battlecard.")
