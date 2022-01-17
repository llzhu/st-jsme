# Import the wrapper function from your package
from st_jsme import st_jsme
import streamlit as st

st.title("JSME Test")
smiles = st_jsme('500px', '300px', 'C')
st.write(smiles)