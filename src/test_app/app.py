import streamlit as st
from test_app.services.test_service import return_hello

st.header("Hello World!")
st.write(return_hello())