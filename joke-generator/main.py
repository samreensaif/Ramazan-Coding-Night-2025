import requests
import streamlit as st

def joke_generator():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']}\n\n{data['punchline']}"
        else:
            return f"Error: {response.status_code}"
            
    except Exception as e:
        
        return "why u not get error"

def main():
    st.markdown("<h1 style='text-align:center; color:orange; font-size:80px; font-weight:bold; '>Joke Generator <br>😂🃏</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:green; font-size:20px; font-weight:bold; '>Click the button to generate a joke</h3>", unsafe_allow_html=True)
        

    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        border: none;
    }
    .stButton>button:hover {
        background-color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    # Generate Joke Button
    if st.button("Generate Joke"):
        joke = joke_generator()
        st.header(joke)
    
    st.markdown("""
    
    <div style ="text-align:center; color:red; font-size:20px; font-weight:bold; ">

    <p>Made with ❤️ by <a href="https://github.com/samreensaif">Samreen Saif</a></p>

    </div>
    
     """, 
        unsafe_allow_html=True)

if __name__ == "__main__":
    main()