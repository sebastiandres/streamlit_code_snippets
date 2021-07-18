import streamlit as st

def page_header(header):
    st.title(":sparkles: Streamlit Code Snippets :sparkles:")
    st.header(header)
    return

def breakline():
    st.markdown("---")
    return    

def documentation(function):
    breakline()
    st.markdown(f"[Streamlit API documentation](https://docs.streamlit.io/en/stable/api.html#streamlit.{function})")
    return
