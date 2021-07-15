import streamlit as st

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    st.title(my_title)
    with st.echo():
        from streamlit_drawable_canvas import st_canvas
        # Specify canvas parameters in application
        col1, col2, col3 = st.beta_columns(3)
        stroke_width = col1.slider("Stroke width: ", 1, 25, 3)
        stroke_color = col2.color_picker("Stroke color hex: ")
        bg_color = col3.color_picker("Background color hex: ", "#eee")
        drawing_mode = st.selectbox(
            "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform", "polygon")
        )
        # Create a canvas component
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            background_image=None,
            update_streamlit=True,
            height=500,
            #drawing_mode=drawing_mode,
            #display_toolbar=st.sidebar.checkbox("Display toolbar", True),
            #key="full_app",
        )

        # Do something interesting with the image data and paths
        """
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data)
        if canvas_result.json_data is not None:
            st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))
        """