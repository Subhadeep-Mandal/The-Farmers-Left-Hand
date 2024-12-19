import requests
from bs4 import BeautifulSoup
import string
import streamlit as st

# Bot to extract data
def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details = soup.find_all('table', {'class': 'infobox'})
    
    result = ""
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading and detail:
                for x, y in zip(heading, detail):
                    result += f"{x.text} :: {y.text}\n"
                    result += "----------------------------\n"
    
    paragraphs = soup.find_all('p')
    for i in range(1, min(3, len(paragraphs))):
        result += paragraphs[i].text + "\n"
    
    return result

# Wikipedia Browser
def wiki_page():
    from wikibot import wikibot
    st.title("📄 WIKIPEDIA INFO FETCHER 🔍")
    st.markdown("""
                ---
                ### ⌨️ INPUT 📌 ONE WORD... 
                ### 📤 OUTPUT 🧾 DESCRIPTION ABOUT THE WORD...
                """
                )
    st.markdown("---")
    # User input
    with st.form("Search"):
        keyword = st.text_input("ENTER YOUR KEY WORD")
        search = st.form_submit_button("Search")
    if search:
        formatted_input = keyword.replace(" ", "_")
        url = "https://en.wikipedia.org/wiki/" + formatted_input
        st.markdown("---")
        # Fetch and display information
        result = wikibot(url)
        st.write(result)
        st.markdown("---")