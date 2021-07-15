import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    page_header(my_title)
    
    with st.beta_expander("Progress"):
        clicked_progress_button = st.button("Run progress")
        if clicked_progress_button:
            with st.echo("below"):
                import time
                my_bar = st.progress(0)
                for i in range(0,101,10):
                    my_bar.progress(i)
                    time.sleep(.3)
            st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.progress)")

    with st.beta_expander("Spinner"):
        clicked_spinner_button = st.button("Run spinner")
        if clicked_spinner_button:
            with st.echo("below"):
                import time
                with st.spinner('Computing some important for 5 seconds...'):
                    time.sleep(5)
                st.success('Done')            
            st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.spinner)")

    with st.beta_expander("Ballons"):
        with st.echo():
            st.balloons()
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.balloons)")

    with st.beta_expander("Error message"):
        with st.echo():
            st.error('This is an Error message')
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.error)")

    with st.beta_expander("Warning message"):
        with st.echo():
            st.warning('This is a Warning message')
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.warning)")

    with st.beta_expander("Info message"):
        with st.echo():
            st.info('This is Info message')
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.info)")

    with st.beta_expander("Success message"):
        with st.echo():
            st.success('This is a Success message')
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.success)")

    with st.beta_expander("This is an Exception"):
        with st.echo():
            try:
                1/0
            except Exception as e:
                st.exception(e)
        st.markdown("Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.exception)")