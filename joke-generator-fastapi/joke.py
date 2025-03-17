import streamlit as st
import requests




api_url = "http://127.0.0.1:8000/random-jokes"

st.set_page_config(page_title="Joke Generator", page_icon="😂", layout="wide")

st.markdown("""
<h1 style="text-align: center; color:red;">🤣 Joke Generator-Fast Api 🤣</h1>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center;">
        <p style="font-size: 20px; color: green;">
            Click the button below to generate a random joke
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Generate Joke"):

    response = requests.get(api_url)
    if response.status_code == 200:
        joke = response.json()
        
        st.markdown(f"<h1 style='color: blue;'>{joke.get('setup')}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: darkCyan;'>{joke.get('punchline')}</h2>", unsafe_allow_html=True)

    else:
        st.error("Failed to generate joke")


st.divider()
st.markdown(
    """
    <div style="text-align: center;">
        <p style="font-size: 20px; color: green;">
            Enjoy The Jokes 😂🤣😂
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)




