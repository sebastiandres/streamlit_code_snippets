import streamlit as st

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    st.title(my_title)

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
