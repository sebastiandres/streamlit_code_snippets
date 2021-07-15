import streamlit as st
import pandas as pd
import numpy as np

DISPLAY_TEXT = "Display Text"
DISPLAY_DATA = "Display Data"
DISPLAY_GRAPHS = "Display Graphs"
USE_MEDIA = "Webcam and Microphone"
DRAWABLE_CANVAS = "Drawable Canvas"
INTERACTIVE_DISPLAY = "Interactive Display"
PROGRESS_AND_STATUS = "Progress and Status"
# Set wide display
st.set_page_config(layout="wide")

# Side Bar
## Create a page dropdown
page = st.sidebar.radio("Choose your page:", 
                          [
                            DISPLAY_TEXT, 
                            DISPLAY_DATA, 
                            PROGRESS_AND_STATUS,
                            INTERACTIVE_DISPLAY,
                            #DISPLAY_GRAPHS, 
                            #DRAWABLE_CANVAS, 
                            #USE_MEDIA, 
                            ]
                        ) 
## Links
links = [
        "* [Streamlit Cheat Sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)",
        "* [Streamlit Gallery](https://streamlit.io/gallery)",
        ]
st.sidebar.markdown("Links:") 
st.sidebar.markdown("\n".join(links)) 
## Autor
st.sidebar.markdown("Created by [sebastiandres](https://sebastiandres.xyz)") 

if page == DISPLAY_TEXT:
    from pages import display_text
    display_text.display_page(DISPLAY_TEXT)
elif page == DISPLAY_DATA:
    from pages import display_data
    display_data.display_page(DISPLAY_DATA)
elif page == DISPLAY_GRAPHS:
    from pages import display_graphs
    display_graphs.display_page(DISPLAY_GRAPHS)
elif page == USE_MEDIA:
    from pages import display_media
    display_media.display_page(DISPLAY_GRAPHS)
elif page == DRAWABLE_CANVAS:
    from pages import drawable_canvas
    drawable_canvas.display_page(DISPLAY_GRAPHS)
elif page == INTERACTIVE_DISPLAY:
    from pages import interactive_widgets
    interactive_widgets.display_page(PROGRESS_AND_STATUS)
elif page == PROGRESS_AND_STATUS:
    from pages import progress_and_status
    progress_and_status.display_page(PROGRESS_AND_STATUS)