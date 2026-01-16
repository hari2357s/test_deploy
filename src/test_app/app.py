import streamlit as st
from test_app.services.test_service import return_hello
from test_app.common.container import test_container

st.header("Hello World!")
st.write(return_hello())
st.text(test_container())