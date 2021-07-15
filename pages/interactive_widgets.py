import streamlit as st

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    st.title(my_title)

    with st.beta_expander("Button"):
        with st.echo():
            b = st.button('Hit me')
            st.write(b, type(b))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.button)")

    with st.beta_expander("Checkbox selection"):
        with st.echo():
            c = st.checkbox('Check me out')
            st.write(c, type(c))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.checkbox)")

    with st.beta_expander("Radio selection"):
        with st.echo():
            r = st.radio('Radio', [1, "2", "three"], help="This is a radio button")
            st.write(r, type(r))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.radio)")

    with st.beta_expander("Single selection"):
        with st.echo():
            sb = st.selectbox('Select', [1, "2", "three"], help="This is a single selection")
            st.write(sb, type(sb))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.selectbox)")

    with st.beta_expander("Multiple selection"):
        with st.echo():
            ms = st.multiselect('Multiselect', [1, "2", "three"], help="This is a multiple selection")
            st.write(ms, type(ms))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.multipleselect)")

    with st.beta_expander("Slider"):
        with st.echo():
            s = st.slider('Slide me', min_value=0, max_value=10)
            st.write(s, type(s))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.slider)")

    with st.beta_expander("Select Slider"):
        with st.echo():
            ss = st.select_slider('Slide to select', options=[1, "2", "three"])
            st.write(ss, type(ss))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.select_slider)")

    with st.beta_expander("Text input"):
        with st.echo():
            ti = st.text_input('Enter some text')
            st.write(ti, type(ti))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.text_input)")

    with st.beta_expander("Number input"):
        with st.echo():
            ni = st.number_input('Enter a number')
            st.write(ni, type(ni))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.select_slider)")

    with st.beta_expander("Text area"):
        with st.echo():
            ta = st.text_area('Area for textual entry')
            st.write(ta, type(ta))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.text_area)")

    with st.beta_expander("Date input"):
        with st.echo():
            di = st.date_input('Date input')
            st.write(di, type(di))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.date_input)")

    with st.beta_expander("Time input"):
        with st.echo():
            te = st.time_input('Time entry')
            st.write(te, type(te))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.text_entry)")

    with st.beta_expander("File upload"):
        with st.echo():
            fu = st.file_uploader('File uploader')
            st.write(fu, type(fu))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.file_uploader)")

    with st.beta_expander("Color Picker"):
        with st.echo():
            cp = st.color_picker('Pick a color')
            st.write(cp, type(cp))
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.color_picker)")
