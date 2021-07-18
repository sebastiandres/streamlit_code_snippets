import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    
    with st.beta_expander("Button"):
        with st.echo("below"):
            b = st.button('Click me')
            st.write("type:", type(b))
            st.write("value:", b)
        breakline()
        with st.echo("below"):
            b = st.button("Click me", key="unique_specific_key", 
                                 help="This is a button", 
                                 #on_click=st.balloons
                                 )
            st.write("type:", type(b))
            st.write("value:", b)
        
        
        documentation("button")

    with st.beta_expander("Checkbox selection"):
        with st.echo("below"):
            c = st.checkbox('Check me out')
            st.write("type:", type(c))
            st.write("value:", c)
        documentation("checkbox")

    with st.beta_expander("Radio selection"):
        with st.echo():
            r = st.radio('Radio', [1, "2", "three"], help="This is a radio button")
            st.write(r, type(r))
        documentation("radio")

    with st.beta_expander("Single selection"):
        with st.echo():
            sb = st.selectbox('Select', [1, "2", "three"], help="This is a single selection")
            st.write(sb, type(sb))
        documentation("selectbox")

    with st.beta_expander("Multiple selection"):
        with st.echo():
            ms = st.multiselect('Multiselect', [1, "2", "three"], help="This is a multiple selection")
            st.write(ms, type(ms))
        documentation("multipleselect")

    with st.beta_expander("Slider"):
        with st.echo():
            s = st.slider('Slide me', min_value=0, max_value=10)
            st.write(s, type(s))
        documentation("slider")

    with st.beta_expander("Select Slider"):
        with st.echo():
            ss = st.select_slider('Slide to select', options=[1, "2", "three"])
            st.write(ss, type(ss))
        documentation("select_slider")

    with st.beta_expander("Text input"):
        with st.echo():
            ti = st.text_input('Enter some text')
            st.write(ti, type(ti))
        documentation("text_input")

    with st.beta_expander("Number input"):
        with st.echo():
            ni = st.number_input('Enter a number')
            st.write(ni, type(ni))
        documentation("select_slider")

    with st.beta_expander("Text area"):
        with st.echo():
            ta = st.text_area('Area for textual entry')
            st.write(ta, type(ta))
        documentation("text_area")

    with st.beta_expander("Date input"):
        with st.echo():
            di = st.date_input('Date input')
            st.write(di, type(di))
        documentation("date_input")

    with st.beta_expander("Time input"):
        with st.echo():
            te = st.time_input('Time entry')
            st.write(te, type(te))
        documentation("text_entry")

    with st.beta_expander("File upload"):
        with st.echo():
            fu = st.file_uploader('File uploader')
            st.write(fu, type(fu))
        documentation("file_uploader")

    with st.beta_expander("Color Picker"):
        with st.echo():
            cp = st.color_picker('Pick a color')
            st.write(cp, type(cp))
        documentation("color_picker")
