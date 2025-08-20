import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv


st.set_page_config (page_title="Anime Recommendation", layout="wide")

load_dotenv()

@st.cache_resource
def get_pipeline():
    return AnimeRecommendationPipeline()

pipeline = get_pipeline()
st.title("Anime Recommendation System")
query = st.text_input("Enter your favorite anime or genre:")

if query: 
    with st.spinner("Generating recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommended Animes:")
        st.write(response)
