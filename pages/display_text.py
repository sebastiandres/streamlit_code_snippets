import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    
    # Title
    with st.beta_expander("Title"):
        with st.echo('below'):
            st.title('My Title')
        documentation("title")
    # Header 
    with st.beta_expander("Header"):
        with st.echo('below'):
            st.header('My Header')
        documentation("header")
    # Header 
    with st.beta_expander("SubHeader"):
        with st.echo('below'):
            st.subheader('My Subheader')
        documentation("subheader")
    # (fixed width) Text
    with st.beta_expander("Text"):
        with st.echo('below'):
            st.text('My fixed width text')
        documentation("text")
    # Markdown
    with st.beta_expander("Markdown"):
        with st.echo('below'):
            st.markdown('This is *Markdown* in all its _glory_')
        breakline()
        with st.echo('below'):
            st.markdown('Markdown but with optional argument', unsafe_allow_html = True)
        breakline()
        with st.echo('below'):
            # Trick for markdown on several lines
            lines = [
                      "This is a multiline markdown comment.",
                      "",
                      "You can even use lists",
                      "* One",
                      "* Two",
                      ]
            st.markdown("\n".join(lines))
        documentation("markdown")
    # Latex
    with st.beta_expander("Latex"):
        with st.echo('below'):
            st.latex(r''' e^{i\pi} + 1 = 0 ''')    
        #breakline()
        #with st.echo('below'):
        #    st.latex(r'''I love small matrice such $\big(\begin{smallmatrix} a & b\\ c & d \end{smallmatrix}\big)$''')
        documentation("latex")

