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
    st.title("Joke Generator 😂🃏")
    st.write("Click the button to generate a joke")
    if st.button("Generate Joke"):
        joke = joke_generator()
        st.header(joke)

    st.divider()
    st.write("Made with ❤️ by [@samreensaif](https://github.com/samreensaif)")

if __name__ == "__main__":
    main()