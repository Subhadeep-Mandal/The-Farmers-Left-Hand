import streamlit as st
import requests

def img_page():
    st.markdown("<h1 style='text-align: center;'>🏞️ FIND YOUR IMAGE HERE</h1>", unsafe_allow_html=True)

    with st.form("Search"):
        keyword = st.text_input("SEARCH ANY IMAGE")
        search = st.form_submit_button("Search")

    if search:
        access_key = "4mNPhWbnHsDY8Ups9SjYV2byRWR1dcBu8DWsf8bogn4"  # Replace with your Unsplash API access key
        url = f"https://api.unsplash.com/search/photos?query={keyword}&client_id={access_key}&per_page=12"
        response = requests.get(url)

        if response.status_code == 200:
            images = response.json()["results"]

            # Create three columns for displaying images
            col1, col2, col3 = st.columns(3)

            for i, img in enumerate(images):
                img_url = img["urls"]["small"]
                caption = img["alt_description"] or "No Description"

                # Display images in separate columns
                if i % 3 == 0:
                    col1.image(img_url, caption=f"Image {i+1}: {caption}", use_column_width=True)
                elif i % 3 == 1:
                    col2.image(img_url, caption=f"Image {i+1}: {caption}", use_column_width=True)
                else:
                    col3.image(img_url, caption=f"Image {i+1}: {caption}", use_column_width=True)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
        st.divider()


