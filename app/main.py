import streamlit as st
from home import home_page
from about import about_us
from predict import predict_page
from wikibot import wiki_page
from imgbot import img_page
from wormap import map_page
from medplant import med_page
from faq import faq_page
from usrhelp import q_page
from loco import local_page

def main():
    
    st.sidebar.title("⚙️ DASHBOARD")

    with st.sidebar:
        selectbox1=st.sidebar.selectbox("☰ CHOOSE AN OPTION",("🏠 HOME","🔍 PREDICTOR","📢 FAQ","🧑🏽‍🦱 ABOUT US","📱 HELP"))
        
    st.sidebar.markdown("---")

    st.sidebar.title("🔍 BROWSE IT")

    with st.sidebar:
        selectbox2=st.sidebar.selectbox("☰ CHOOSE AN OPTION",("🔍 SEARCH","🖼️ IMAGE","🗺️ SHOW MAP","🧪 MED PLANTS","🌾 LOCO CROP"))
        
    if selectbox1 == "🏠 HOME":
        home_page()  # Call your home_page() function
    elif selectbox1 == "🧑🏽‍🦱 ABOUT US":
        about_us()  # Call your about_us() function
    elif selectbox1 == "🔍 PREDICTOR":
        predict_page()
    elif selectbox1 == "📱 HELP":
        q_page()
    elif selectbox1 == "📢 FAQ":
        faq_page()

    st.divider()

    if selectbox2 == "🔍 SEARCH":
        wiki_page()  # Call your wiki_page() function
    elif selectbox2 == "🖼️ IMAGE":
        img_page()  # Call your img_page() function
    elif selectbox2 == "🗺️ SHOW MAP":
        map_page()
    elif selectbox2 == "🧪 MED PLANTS":
        med_page()
    elif selectbox2 == "🌾 LOCO CROP":
        local_page()

main()
