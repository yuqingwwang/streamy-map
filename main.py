import streamlit as st
import folium
from folium.plugins import Draw, MousePosition
from streamlit_folium import st_folium
from folium.features import ClickForLatLng, ClickForMarker

# Create the Folium map using your create_map function
def create_map(center):
    m = folium.Map(
        location=center,
        zoom_start=12,
        control_scale=True,
        tiles="OpenStreetMap",
        attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
    )
    Draw(
        export=False,
        position="topleft",
        draw_options={
            "polyline": False,
            "poly": False,
            "circle": False,
            "polygon": False,
            "marker": False,
            "circlemarker": False,
            "rectangle": True,
        }).add_to(m)
    #MousePosition()
    #ClickForLatLng()
    return m

# Streamlit app
st.title("Folium Map with Rectangle")

# Create the Folium map
initial_center = [51.5328, -0.0769]
m = create_map(initial_center)

# Add a button to capture the rectangle coordinates
if st.button("Get Rectangle Coordinates"):
    drawn_features = m.to_dict()
    st.write(drawn_features)

# Display the Folium map using st_folium
st_folium(m)
