import streamlit as st

from .shared_functions import page_header, documentation, breakline, what4, examples

def display_page(my_title):
    page_header(my_title)
    st.write("Methods used to indicate progress bar or messages.")
    
    with st.beta_expander("Progress"):
        what4("This is a progress bar used to indicate progress on a activity. The button starts an animation.")
        examples()
        clicked_progress_button = st.button("Run progress")
        if clicked_progress_button:
            with st.echo("below"):
                import time
                my_bar = st.progress(0)
                for i in range(0,101,10):
                    my_bar.progress(i)
                    time.sleep(.3)
            documentation("progress")

    with st.beta_expander("Spinner"):
        what4("This is placeholder text shown while some activity is taken place. The button starts an animation.")
        examples()
        clicked_spinner_button = st.button("Run spinner")
        if clicked_spinner_button:
            with st.echo("below"):
                import time
                with st.spinner('Computing some important for 3 seconds...'):
                    time.sleep(3)
                st.success('Done')            
            documentation("spinner")

    with st.beta_expander("Ballons"):
        what4("This throws some ballons. Because why not.")
        examples()
        with st.echo("below"):
            st.balloons()
        breakline()
        with st.echo("below"):
            if st.button("Click here for free ballons"):
                st.balloons()
        documentation("balloons")

    with st.beta_expander("Info message"):
        what4("To display an information message in a blue box.")
        examples()
        with st.echo():
            st.info('This is Info message')
        breakline()
        with st.echo("below"):
            info_text = st.text_input("Write your own info message here!",
                                         value="My custom info message")
            st.info(info_text)
        documentation("info")

    with st.beta_expander("Success message"):
        what4("To display a success message in a green box.")
        examples()
        with st.echo():
            st.success('This is a SUCCESS message')
        breakline()
        with st.echo("below"):
            success_text = st.text_input("Write your own success message here!",
                                         value="My custom success message")
            st.success(success_text)
        documentation("success")

    with st.beta_expander("Warning message"):
        what4("To display an warning message in a yellow box.")
        examples()
        with st.echo():
            st.warning('This is a warning message')
        breakline()
        with st.echo("below"):
            warning_text = st.text_input("Write your own warning message here!",
                                         value="My custom warning message")
            st.warning(warning_text)
        documentation("warning")

    with st.beta_expander("Error message"):
        what4("To display an error message in a red box.")
        examples()
        with st.echo():
            st.error('This is an Error message')
        breakline()
        with st.echo("below"):
            error_text = st.text_input("Write your own error message here!",
                                       value="My custom error message")
            st.error(error_text)
        documentation("error")

    with st.beta_expander("This is an Exception"):
        what4("To display an exception message in a red box with the error traceback.")
        examples()
        with st.echo("below"):
            try:
                1/0
            except Exception as e:
                st.exception(e)
        breakline()
        with st.echo("below"):
            exception_text = st.text_input("Write a python that throws an error!",
                                         value="1 + 0")
            try:
                eval(exception_text)
                st.success("No error, try harder!")
            except Exception as e:
                st.exception(e)
        documentation("exception")
