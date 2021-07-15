import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    

    with st.beta_expander("Microphone"):
        with st.echo():
            st.code("FIX ME")

    with st.beta_expander("Webcam"):
        with st.echo("Code"):
            from streamlit_webrtc import (
                AudioProcessorBase,
                ClientSettings,
                VideoProcessorBase,
                WebRtcMode,
                webrtc_streamer,
            )
