import streamlit as st

from .shared_functions import page_header, documentation, breakline, what4, examples

def display_page(my_title):
    page_header(my_title)
    st.write("Methods to interact with the user.")
    st.write("You can use the selected value to control the flow of action")

    with st.beta_expander("Button"):
        what4("To put a button")
        examples()
        with st.echo("below"):
            b = st.button('Click me')
            st.write("type:", type(b))
            st.write("value:", b)
        breakline()
        with st.echo("below"):
            button_clicked = st.button("Click me", key="unique_specific_key", 
                                 help="This is a button", 
                                 )
            if button_clicked:
                st.balloons()
            st.write("type:", type(b))
            st.write("value:", b)
        documentation("button")

    with st.beta_expander("Checkbox selection"):
        what4("To put a checkbox")
        examples()
        with st.echo("below"):
            c = st.checkbox('Check me!')
            st.write("type:", type(c))
            st.write("value:", c)
        breakline()
        with st.echo("below"):
            checkbox_selected = st.checkbox('Check me out!')
            if checkbox_selected:
                st.info("Great choice")
            st.write("type:", type(checkbox_selected))
            st.write("value:", checkbox_selected)
        documentation("checkbox")

    with st.beta_expander("Radio selection"):
        what4("To put a radio buttons with multiple options")
        examples()
        with st.echo("below"):
            r = st.radio('Radio', [1, "2", "three"])
            st.write("type:", type(r))
            st.write("value:", r)
        breakline()
        with st.echo("below"):
            radio_button = st.radio('Select how to be congratulated:', 
                                    ["info message", "success message", "balloons"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="balloons":
                st.balloons()
            elif radio_button=="info message":
                st.info("Good choice")
            elif radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("radio")

    with st.beta_expander("Single selection"):
        what4("To put a dropdown menu with a **single** selection from multiple options")
        examples()
        with st.echo("below"):
            sb = st.selectbox('Select', [1, "2", "three"], help="This is a single selection")
            st.write(sb, type(sb))
        breakline()
        with st.echo("bellow"):
            radio_button = st.selectbox('Select how to be congratulated:', 
                                    ["info message", "success message", "balloons"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="balloons":
                st.balloons()
            elif radio_button=="info message":
                st.info("Good choice")
            elif radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("selectbox")

    with st.beta_expander("Multiple selection"):
        what4("To put a dropdown menu with a **multiplle** selection from multiple options")
        examples()
        with st.echo("below"):
            ms = st.multiselect('Multiselect', [1, "2", "three"], help="This is a multiple selection")
            st.write(ms, type(ms))
        breakline()
        with st.echo("below"):
            radio_button = st.selectbox('Select how to be congratulated:', 
                                    ["info message", "success message", "nothing"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="nothing":
                st.error("You should congratulate yourself!")
            if radio_button=="info message":
                st.info("Good choice")
            if radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("multipleselect")

    with st.beta_expander("Slider - Integer selection"):
        what4("To allow for number selection with a slider.")
        examples()
        with st.echo("below"):
            s = st.slider('Slide me', min_value=0, max_value=100)
            st.write("type:", type(s))
            st.write("value:", s)
        breakline()
        with st.echo("below"):
            x = st.slider('Select a value to know the square', min_value=-10, max_value=+10)
            st.write(f"The square of {x} is {x**2}")
        documentation("slider")

    with st.beta_expander("Select Slider - Arbitrary selection"):
        what4("To do a arbirary selection with a slider.")
        examples()
        with st.echo("below"):
            ss = st.select_slider('Slide to select', 
                                  options=["one", "two", "three"])
            st.write("type:", type(ss))
            st.write("value:", ss)
        breakline()
        with st.echo("below"):
            w = st.select_slider('Select a word to know how many letters', 
                                  options=["one", "two", "three"])
            st.write(f"The word {w} has {len(w)} letters")
        documentation("select_slider")

    with st.beta_expander("Text input"):
        what4("To receive text from user.")
        examples()
        with st.echo("below"):
            ti = st.text_input('Enter some text')
            st.write("type:", type(ti))
            st.write("value:", ti)
        breakline()
        with st.echo("below"):
            my_text = st.text_input('Enter some text and prepare to be suprised', value="This is incredible!")
            my_new_text = "".join( c.lower() if i%2==0 else c.upper() for i,c in enumerate(my_text))
            st.info(my_new_text)
        documentation("text_input")

    with st.beta_expander("Number input"):
        what4("To ...")
        examples()
        with st.echo("below"):
            ni = st.number_input('Enter a number')
            st.write("type:", type(ni))
            st.write("value:", ni)
        breakline()
        with st.echo("below"):
            number = st.number_input('Please provide a number')
        documentation("number_input")

    with st.beta_expander("Text area"):
        what4(".")
        examples()
        with st.echo("below"):
            ta = st.text_area('Area for textual entry')
            st.write("type:", type(ta))
            st.write("value:", ta)
        breakline()
        with st.echo("below"):
            answer = st.text_area('What was the name of your first pet?')
        documentation("text_area")

    with st.beta_expander("Date input"):
        what4(".")
        examples()
        with st.echo("below"):
            di = st.date_input('Date input')
            st.write("type:", type(di))
            st.write("value:", di)
        breakline()
        with st.echo("below"):
            birthdate = st.date_input('Please provide your birthdate')
        documentation("date_input")

    with st.beta_expander("Time input"):
        what4(".")
        examples()
        with st.echo("below"):
            te = st.time_input('Time entry')
            st.write("type:", type(te))
            st.write("value:", te)
        breakline()
        with st.echo("below"):
            ttb = st.time_input('At what time do you go to bed?')
            ttb = st.time_input('How early do you rise?')
        documentation("text_entry")

    with st.beta_expander("File upload"):
        what4("To allow the user to upload a file")
        examples()
        with st.echo("below"):
            fu = st.file_uploader('File uploader')
            st.write("type:", type(fu))
            st.write("value:", fu)
        breakline()
        with st.echo("below"):
            uploaded_file = st.file_uploader('Upload an image file')
            if uploaded_file:
                st.image(uploaded_file)
        documentation("file_uploader")

    with st.beta_expander("Color Picker"):
        what4("To make the user pick a color")
        examples()
        with st.echo("below"):
            cp = st.color_picker('Pick a color')
        documentation("color_picker")
