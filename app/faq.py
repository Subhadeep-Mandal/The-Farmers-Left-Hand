import streamlit as st

def faq_page():
    # List of plants
    plants = ["Snake Plant", "Spider Plant", "ZZ Plant", "Aloe Vera", "Jade Plant"]

    # Selectbox for plant selection
    selected_plant = st.selectbox("WHAT PLANTS CAN PEOPLE GROW IN HOME WITH MINIMUM EFFORT", plants)

    # Dictionary with plant details
    plant_details = {
        "Snake Plant": "Known for its tall, sturdy leaves, this plant thrives in low light and requires infrequent watering.",
        "Spider Plant": "This resilient plant is easy to grow and can tolerate a variety of conditions.",
        "ZZ Plant": "This plant is very forgiving and can survive with little water and low light.",
        "Aloe Vera": "Besides being low-maintenance, it also has medicinal properties.",
        "Jade Plant": "This succulent requires minimal watering and does well in direct sunlight."
    }

    # Display plant details
    st.write(f"**{selected_plant}**: {plant_details[selected_plant]}")
