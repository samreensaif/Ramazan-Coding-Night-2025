import streamlit as st
import random
import string


def generate_password(length,use_digits,use_specials):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits  #add digits
    
    if use_specials:
        characters += string.punctuation  #add special characters
    
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔑 Password Generator")

length = st.slider("Passsword Length", min_value=6,max_value=20, value=12)

use_digits = st.checkbox("include digits")

use_specials = st.checkbox("include special characters")

if st.button("generate password"):
    password = generate_password(length,use_digits,use_specials)
    st.write(f"Generated Password:{password}")

st.write("---------------")
st.write ("Made with 🍒❤ | Samreen Saif")