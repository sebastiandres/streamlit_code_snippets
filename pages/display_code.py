import streamlit as st

from .shared_functions import page_header, documentation, breakline, what4, examples

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    st.write("Methods used to display code.")

    # Code
    with st.beta_expander("Code"):
        what4("You can write dataframes")
        examples()
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
        what4("To show the code used in certain part of your app.")
        examples()
        with st.echo("below"):
            if st.button("Click here for free ballons"):
                st.balloons()
        st.markdown("All of above code is simply obtained by conveniently wrapping with the echo method")
        multiline_code2 = [
                            'with st.echo("below"):',
                            '    if st.button("Click here for free ballons"):',
                            '        st.balloons()',
                         ]
        st.code("\n".join(multiline_code2))
        st.markdown('`st.echo()` admits values "above" or "below".')
        documentation("echo")