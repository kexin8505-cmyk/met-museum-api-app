import requests
import streamlit as st

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

st.title("🎨 Explore Artworks with MET Museum API")

query = st.text_input("Search for artworks:", value="cat")

if st.button("Search") and query.strip():
    search_url = f"{BASE_URL}/search"
    params = {"q": query, "hasImages": "true"}
    res = requests.get(search_url, params=params)
    data = res.json()

    object_ids = data.get("objectIDs") or []
    total = data.get("total", 0)
    st.write(f"Found {total} artworks. Showing first 5 results:")

    for obj_id in object_ids[:5]:
        detail_url = f"{BASE_URL}/objects/{obj_id}"
        detail = requests.get(detail_url).json()
        title = detail.get("title", "Untitled")
        artist = detail.get("artistDisplayName", "Unknown artist")
        year = detail.get("objectDate", "Unknown date")
        img = detail.get("primaryImageSmall", "")

        st.subheader(title)
        st.caption(f"{artist} | {year}")
        if img:
            st.image(img, use_column_width=True)
