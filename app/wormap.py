import streamlit as st
from streamlit_folium import folium_static
import folium
from pygbif import occurrences
from Bio import Entrez

# Set your email for NCBI Entrez
Entrez.email = "your_email@example.com"

def get_scientific_name(common_name):
    search = Entrez.esearch(term=common_name, db="taxonomy", retmode="xml")
    record = Entrez.read(search)
    if record["IdList"]:
        tax_id = record["IdList"][0]
        fetch = Entrez.efetch(id=tax_id, db="taxonomy", retmode="xml")
        data = Entrez.read(fetch)
        return data[0]["ScientificName"]
    return None

def map_page():
    st.title("🌍 WORLD NATURE NAVIGATOR ")
    
    # Initialize session state for common name and scientific name
    if 'common_name' not in st.session_state:
        st.session_state.common_name = ''
    if 'scientific_name' not in st.session_state:
        st.session_state.scientific_name = ''

    with st.form("Map"):
        # Get common name from the user
        common_name = st.text_input("ENTER THE SPECIES TO BE SHOWN IN MAP")
        search = st.form_submit_button("Search")
        
        if search and common_name:
            # Get the scientific name from the common name
            scientific_name = get_scientific_name(common_name)
            st.session_state.common_name = common_name
            st.session_state.scientific_name = scientific_name

    # Display the map outside the form
    if st.session_state.scientific_name:
        st.write(f"Scientific name: {st.session_state.scientific_name}")

        # Search for species occurrences using the scientific name
        occurrences_data = occurrences.search(scientificName=st.session_state.scientific_name)

        # Create a Folium map with default OpenStreetMap tiles
        map = folium.Map(
            location=[20.5937, 78.9629],  # Centered on India
            zoom_start=4,
        )

        # Add markers for each occurrence with three shades of green
        colors = ['darkgreen', 'green', 'lightgreen']
        for i, occurrence in enumerate(occurrences_data['results']):
            if 'decimalLatitude' in occurrence and 'decimalLongitude' in occurrence:
                lat, lon = occurrence["decimalLatitude"], occurrence["decimalLongitude"]
                tooltip = st.session_state.common_name
                color = colors[i % len(colors)]
                popup_text = f"Scientific Name: {st.session_state.scientific_name}<br>Latitude: {lat}<br>Longitude: {lon}"
                folium.Marker(
                    location=[lat, lon],
                    popup=popup_text,
                    icon=folium.Icon(color=color, icon='tree', prefix='fa', icon_color='black'),
                    tooltip=tooltip
                ).add_to(map)
        
        folium_static(map)
        st.write("Map displaying occurrences of", st.session_state.common_name)
    elif st.session_state.common_name:
        st.write("No scientific name found for the given common name.")
