import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    
    # Code
    with st.beta_expander("Code"):
        with st.echo('below'):
            st.code('print("Hello world")')
        breakline()
        with st.echo('below'):
            multiline_code = [
                              "a,b = 1.2344, 4.52",
                              "print(a+b)",
                              ]
            st.code('\n'.join(multiline_code))
        documentation("code")

    # Echo
    with st.beta_expander("Echo"):
        with st.echo("below"):
            st.markdown("Example _text_ for **markdown**")
            st.info("Use it wisely")
        st.markdown("Results and code displayed are obtained with the following code:")
        multiline_code2 = [
                            'with st.echo("below"):',
                            '    st.markdown("Example text for markdown")',
                            '    st.info("Use it wisely")',
                            'st.markdown("The above result is obteined with the following code")',
                         ]
        st.code("\n".join(multiline_code2))
        st.markdown("Options: above or below.")
        documentation("echo")